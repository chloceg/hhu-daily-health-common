#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from datetime import timezone
from datetime import timedelta
from datetime import datetime
import hhu
import os


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


# In[3]:

if os.environ.get('SCKEY', '') != '':
    SCKEY = os.environ['SCKEY']
url='https://sc.ftqq.com/{}.send?text={},打卡成功了！'.format(SCKEY, year+'年'+month+'月'+day+'日'+timestr)


# In[4]:


if hhu.hhu()=='Success!':
    requests.get(url)

