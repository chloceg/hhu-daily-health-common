#!/usr/bin/env python
# coding: utf-8

# In[1]:
from datetime import timezone
from datetime import timedelta
from datetime import datetime
import hhu


# In[2]:
utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
sh_tz = timezone(timedelta(hours=8),name='Asia/Shanghai')
beijing_now = utc_time.astimezone(sh_tz)

datestr = datetime.strftime(beijing_now,'%F')
timestr = datetime.strftime(beijing_now,'%H:%M:%S')
year = datestr[0:4]
month = datestr[5:7]
day = datestr[8:10]
time = timestr


hhu.hhu()
