"""
You are designing a log storage system that allows users to store logs with timestamps and retrieve logs within a given time range with a specified granularity.

Implement a class LogSystem that supports the following functions:
void put(int id, string timestamp): Store a log with a given ID and timestamp.
List<Integer> retrieve(String start, String end, String granularity): Retrieve log IDs within the given timestamp range at a specified level of granularity.
Granularity Levels:
The timestamp format is "YYYY:MM:DD:HH:MM:SS" (Year, Month, Day, Hour, Minute, Second), and the granularity levels are:
logSystem = LogSystem()
logSystem.put(1, "2017:01:01:23:59:59")
logSystem.put(2, "2017:01:01:22:59:59")
logSystem.put(3, "2017:01:02:00:00:00")
logSystem.retrieve("2017:01:01:23:00:00", "2017:01:02:00:00:00", "Hour")
[1, 3]

"""


class LogSystem:
    def __init__(self):
        self.logs = []  # Store logs as (id, timestamp)
        self.granularity_map = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str):
        index = self.granularity_map[granularity]  # Get the truncation index
        start = start[:index]  # Truncate start timestamp
        end = end[:index]  # Truncate end timestamp

        # Filter logs based on truncated timestamp comparison
        result = []
        for id, timestamp in self.logs:
            if start <= timestamp[:index] <= end:
                result.append(id)

        return result
log_system = LogSystem()
log_system.put(1, "2017:01:01:23:59:59")
log_system.put(2, "2017:01:01:22:59:59")
log_system.put(3, "2017:01:02:00:00:00")
print(log_system.retrieve("2017:01:01:23:00:00", "2017:01:02:00:00:00", "Hour"))