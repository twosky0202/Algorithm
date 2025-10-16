from datetime import datetime, timedelta, timezone

tz = timezone(timedelta(hours=9))
now = datetime.now(tz).date()

print(now)