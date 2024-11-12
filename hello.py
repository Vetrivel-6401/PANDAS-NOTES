from datetime import datetime
from pytz import utc,timezone

utc_now = datetime.now(utc)
pst_now=utc_now.astimezone(timezone('Europe/Paris'))
tz=pst_now.isoformat().split('+')[1]
print(utc_now)
print(pst_now)
print(tz)