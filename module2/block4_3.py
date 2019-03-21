from datetime import datetime , timedelta
py27_days_left = (datetime(day=1, month=1, year=2020) - datetime.now()).days
print (py27_days_left )