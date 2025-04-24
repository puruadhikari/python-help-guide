"""
healthcare_age_ingest.py
Populate an Apache‑AGE graph (‘health_graph’) from healthcare.csv
-----------------------------------------------------------------
pip install psycopg2‑binary python‑dotenv
"""

import csv
import json
import os
from dotenv import load_dotenv

import psycopg2
from psycopg2 import sql

# ── 1. ENVIRONMENT ──────────────────────────────────────────────
load_dotenv()          # .env keeps secrets out of the source tree

PG_HOST      = os.environ["PG_HOST"]          # e.g. 127.0.0.1
PG_PORT      = int(os.getenv("PG_PORT", 5432))
PG_USER      = os.environ["PG_USER"]
PG_PASSWORD  = os.environ["PG_PASSWORD"]
PG_DATABASE  = os.environ["PG_DATABASE"]      # normal Postgres DB
GRAPH_NAME   = os.getenv("AGE_GRAPH", "health_graph")

# ── 2. CONNECT & PREPARE AGE ────────────────────────────────────
conn = psycopg2.connect(
    host=PG_HOST,
    port=PG_PORT,
    user=PG_USER,
    password=PG_PASSWORD,
    dbname=PG_DATABASE,
)
conn.autocommit = False       # explicit commits keep things clear

with conn.cursor() as cur:
    # Make sure the extension is ready (no‑ops if it already exists)
    cur.execute("CREATE EXTENSION IF NOT EXISTS age;")
    cur.execute("LOAD 'age';")
    cur.execute("SET search_path = ag_catalog, \"$user\", public;")
    # Create the graph only if it hasn’t been created before
    cur.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM ag_catalog.ag_graph
                WHERE name = %s
            ) THEN
                PERFORM create_graph(%s);
            END IF;
        END
        $$;
        """,
        (GRAPH_NAME, GRAPH_NAME),
    )
conn.commit()

# ── 3. HELPER — run any Cypher with optional parameters ─────────
def execute_query(cypher_query: str, parameters: dict | None = None):
    """
    Wraps Apache‑AGE’s cypher(graph, query, params_json) function.
    Parameters are passed safely as JSONB.
    """
    params_json = json.dumps(parameters or {})

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT *
            FROM cypher(%s, %s, %s::jsonb) AS (result agtype);
            """,
            (GRAPH_NAME, cypher_query, params_json),
        )
    conn.commit()


# ── 4. GRAPH‑BUILDING FUNCTIONS (same Cypher, just AGE‑ready) ───
def create_healthcare_provider(provider, bio):
    query = """
    MERGE (hp:HealthCareProvider {name:$provider, bio:$bio})
    """
    execute_query(query, {"provider": provider, "bio": bio})


def create_patient_node(patient, patient_age, patient_gender, patient_condition):
    query = """
    MERGE (p:Patient {
        name:$patient,
        age:$patient_age,
        gender:$patient_gender,
        patientCondition:$patient_condition
    })
    """
    execute_query(
        query,
        {
            "patient": patient,
            "patient_age": int(patient_age),
            "patient_gender": patient_gender,
            "patient_condition": patient_condition,
        },
    )


def create_specialisation_node(specialisation):
    query = "MERGE (s:Specialisation {name:$specialisation})"
    execute_query(query, {"specialisation": specialisation})


def create_location_node(location):
    query = "MERGE (l:Location {name:$location})"
    execute_query(query, {"location": location})


def create_relationships(provider, patient, specialisation, location):
    query = """
    MATCH (hp:HealthCareProvider {name:$provider}),
          (p:Patient {name:$patient})
    MERGE (hp)-[:TREATS]->(p)
    WITH hp
    MATCH (s:Specialisation {name:$specialisation})
    MERGE (hp)-[:SPECIALIZES_IN]->(s)
    WITH hp
    MATCH (l:Location {name:$location})
    MERGE (hp)-[:LOCATED_AT]->(l)
    """
    execute_query(
        query,
        {
            "provider": provider,
            "patient": patient,
            "specialisation": specialisation,
            "location": location,
        },
    )


# ── 5. INGEST the CSV ───────────────────────────────────────────
CSV_PATH = "healthcare.csv"

with open(CSV_PATH, newline="", encoding="utf‑8") as file:
    reader = csv.DictReader(file)
    print("Reading file…")
    for row in reader:
        create_healthcare_provider(row["provider"], row["bio"])
        create_patient_node(
            row["patient"],
            row["patient_age"],
            row["patient_gender"],
            row["patient_condition"],
        )
        create_specialisation_node(row["spcialisation"])
        create_location_node(row["location"])
        create_relationships(
            row["provider"],
            row["patient"],
            row["spcialisation"],
            row["location"],
        )

print("✅  Graph created successfully")
conn.close()
