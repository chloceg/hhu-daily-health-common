#!/usr/bin/env python
# coding: utf-8

# In[3]:
import requests
from datetime import timezone
from datetime import timedelta
from datetime import datetime
import re
import json


# In[4]:
def hhu(username: str, password: str):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    data = {
        'IDToken1':'{}'.format(username),
        'IDToken2':'{}'.format(password),
    }
    
    s = requests.session()
    # get HHU Cookie
    _ = s.post('http://ids.hhu.edu.cn/amserver/UI/Login',
        data=data,
        headers=headers)
    if s.cookies.get("iPlanetDirectoryPro") == None:
        print("can't login")
        raise requests.RequestException("can't login") # wrong account info or others...
    
    # get healthreport Cookie
    _ = s.get('http://form.hhu.edu.cn/pdc/form/list',
        headers=headers)
    if s.cookies.get("JSESSIONID", domain="form.hhu.edu.cn") == None:
        print("can't access healthreport website")
        raise requests.RequestException("can't access healthreport website")

    # get post history
    res = s.get('http://form.hhu.edu.cn/pdc/formDesignApi/S/gUTwwojq',
        headers=headers)
    history = parseFormData(res.text)
    if not history:
        print("can't get formdata")
        raise requests.RequestException("can't get formdata")
    
    history.pop('CLRQ') # delete key
    history['DATETIME_CYCLE'] = CstTime()

    purl = 'http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid=A335B048C8456F75E0538101600A6A04&userId={}'.format(username)
    pheaders = {
        "Accept": "application/json, text/javascript, */*; q=0.01","Accept-Encoding": "gzip, deflate","Accept-Language": "en-us",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    pr = s.post(purl, data=history, headers=pheaders)
    pr.text
    if pr.text[10:14]=='true':
        print('Success!')
    ok='Success!'
    return ok

# get history
def parseFormData(res: str):
    data = re.findall(r'fillDetail = \[({.+?})', res)
    if len(data) == 0:
        return False
    return json.loads(data[0])

# get China Standard Time
def CstTime() ->str:
    utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    sh_tz = timezone(timedelta(hours=8),name='Asia/Shanghai')
    beijing_now = utc_time.astimezone(sh_tz)
    
    return beijing_now.strftime('%Y/%m/%d') # format: YYYY/MM/DD