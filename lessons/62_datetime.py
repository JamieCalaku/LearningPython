import datetime

# Set a date (year, month, day)
birthday = datetime.datetime(2011, 6, 25)

# Get the date
today = datetime.date.today()

# Set a time
time = datetime.time(12, 30, 0)

# Get the current time and format specify it
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")

# Example
target_datetime = datetime.datetime(2032, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

print(now)
