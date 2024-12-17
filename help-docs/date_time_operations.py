from datetime import datetime, date, time, timedelta

current_time = "10:00"
mid_night = "00:00"

current_time_formated = datetime.strptime("10:00","%H:%M")
mid_night_formated = datetime.strptime("00:00","%H:%M")

duration = current_time_formated-mid_night_formated
print(duration.seconds)

# Current Date and Time
now = datetime.now()             # Get current date and time
today = date.today()             # Get current date
now.strftime("%Y-%m-%d %H:%M:%S") # Format datetime as string

# Creating Date and Time Objects
dt = datetime(2024, 9, 7, 12, 30, 45)  # Create specific datetime
d = date(2024, 9, 7)                   # Create specific date
t = time(12, 30, 45)                   # Create specific time

# Parsing Strings to DateTime
dt_str = "2024-09-07 12:30:45"

dt_parsed = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")  # Parse string to datetime

# Date Arithmetic
tomorrow = today + timedelta(days=1)   # Add days to date
yesterday = today - timedelta(days=1)  # Subtract days from date
one_hour_later = now + timedelta(hours=1)  # Add hours to datetime

# Date and Time Components
year = now.year                       # Get year
month = now.month                     # Get month
day = now.day                         # Get day
hour = now.hour                       # Get hour
minute = now.minute                   # Get minute
second = now.second                   # Get second

# Difference Between Dates
delta = tomorrow - today              # Difference between dates
delta.days                            # Number of days in difference

# Time Zone Handling
from datetime import timezone

utc_now = datetime.now(timezone.utc)  # Get current UTC time
local_now = utc_now.astimezone()      # Convert UTC to local time

# ISO 8601 Format
iso_format = now.isoformat()          # Convert datetime to ISO 8601 string
iso_parsed = datetime.fromisoformat(iso_format)  # Parse ISO 8601 string to datetime