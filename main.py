# import datetime

# myDate = datetime.date(year=2022, month=12, day= 7)

# print(myDate)

# # This code outputs '2022-12-07'

# import datetime

# today = datetime.date.today()

# print(today)

# # This code outputs the current date from your computer's clock.

# import datetime

# day = int(input("Day: ")) # Get all input as numbers. We're not at text input for months yet.
# month = int(input("Month: "))
# year = int(input("Year: "))

# date = datetime.date(year, month, day)

# print(date)

# import datetime

# today = datetime.date.today() # Today's date

# difference = datetime.timedelta(days=14) # The difference I want

# newDate = today + difference # Add today to the delta difference to see the date in 14 days time.

# print(newDate)

# import datetime

# today = datetime.date.today() # Today's date

# holiday = datetime.date(year = 2022, month = 11, day = 13) # The date of my holiday

# if holiday > today: # If my holiday is in the future
#   print("Coming soon")
# elif holiday < today: #If my holiday date has passed
#   print("Hope you enjoyed it")
# else: # If my holiday date is today
#   print("HOLIDAY TIME!")

# import datetime

# today = datetime.date.today()

# print(today)

# import datetime

# today = datetime.date(day = 1, month =11, year = 2023)

# print(today)

# import datetime

# today = datetime.date.today()

# holiday = datetime.date(year = 2022, day = 20, month = 11)

# if holiday > today:
#   print("Coming soon")
# elif holiday < today:
#   print("Hope you enjoyed it")
# else:
#   print("HOLIDAY TIME!")

import datetime

today = datetime.date.today()

print("2023 COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference > 0:
  print(f"{difference} days to go")
elif difference < 0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")

else:
  print("🥳🥳🥳🥳🥳🥳🥳 Today!")
