

from datetime import datetime

now = datetime.now()
print("now:", now)


# 创建datetime类
dt = datetime(2022, 6, 13, 12, 00)
print(dt)

# 时间戳转换成时间
ts = 1521167218
print(datetime.fromtimestamp(ts))
print(datetime.utcnow())

# 格式化日期

day = datetime.strptime('2011-6-13 12:22:2', '%Y-%m-%d %H:%M:%S')
print(day)

print(now.strftime(' %a, %b %d %H: %M'))

# 时间的加减
from datetime import timedelta

added = now + timedelta(hours=10)
print('added:', added)
reduced = now - timedelta(days=5, hours=1, minutes=10, seconds=10)
print('reduced:', reduced)

# 本地时间转换为UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
# 本地时间
now = datetime.now()
print("utc zero:", now)
utc_8 = now.replace(tzinfo=tz_utc_8)
print("utc 8:", utc_8)

# 时区转换
now = datetime.now()

tokyo_dt = now.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
