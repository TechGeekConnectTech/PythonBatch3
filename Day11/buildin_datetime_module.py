from datetime import datetime,timedelta,timezone

print("Current date and time:", datetime.now())

future_date= datetime.now()+timedelta(days=2)
print("Future date (2 days later):", future_date)

past_date= datetime.now()-timedelta(weeks=3)
print("Past date (3 weeks earlier):", past_date)

specific_date= datetime(2023,12,25,10,30)
print("Specific date and time:", specific_date)

todays_date= datetime.now()
print("Today's date:", todays_date.date())
print("Year:", todays_date.year)
print("Month:", todays_date.month)
print("Day:", todays_date.day)
print("Hour:", todays_date.hour)
print("Minute:", todays_date.minute)
print("Second:", todays_date.second)
formatted_date= todays_date.strftime("%d/%m/%Y %H:%M:%S")
print("Formatted date and time:", formatted_date)

import time
# show UKT timezone time
print(time.strftime("Current UK Time: %H:%M:%S", time.localtime())) 

print("UTC time:", datetime.now(timezone.utc))