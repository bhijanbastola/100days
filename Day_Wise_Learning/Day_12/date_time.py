from datetime import datetime, timedelta

today = datetime.now()
print(today)

year_5 = timedelta(days=5 * 365)

future_date = today + year_5

print(future_date.strftime("%a-%d-%b %Y"))