#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from datetime import timezone
from datetime import timedelta
from datetime import datetime
from urllib import parse
import configparser


# In[4]:


def hhu():
    url = 'http://ids.hhu.edu.cn/amserver/UI/Login'
    config = configparser.RawConfigParser()
    config.read('info.ini', encoding='utf-8-sig')
    dic1 = ['学号', '密码', '姓名', '身份证号', '学院', '专业', '攻读学位', '导师', '培养类别', '宿舍楼', '宿舍号', '手机号码', '紧急联系人电话']

    for i in range(0, 13):
        dic1[i] = config.get('personal_info', dic1[i])
        dic1[i] = parse.quote(dic1[i])

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    data = {
        'Login.Token1': '{}'.format(dic1[0]),
        'Login.Token2': '{}'.format(dic1[1]),
        'goto': 'http://my.hhu.edu.cn/loginSuccess.portal',
        'gotoOnFail': 'http://my.hhu.edu.cn/loginFailure.portal',
    }

    utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    sh_tz = timezone(timedelta(hours=8), name='Asia/Shanghai')
    beijing_now = utc_time.astimezone(sh_tz)

    datestr = datetime.strftime(beijing_now, '%F')
    timestr = datetime.strftime(beijing_now, '%H:%M:%S')
    year = datestr[0:4]
    month = datestr[5:7]
    day = datestr[8:10]
    time = timestr

    s = requests.session()
    r = s.post(url, data=data, headers=headers)
    r.text
    purl = 'http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid=A3359E1B43376F77E0538101600A8722&userId={}'.format(
        dic1[0])
    pheaders = {
        "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-us",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    pdata = 'DATETIME_CYCLE=' + year + '%2F' + month + '%2F' + day + '&XGH_566872={0}&XM_140773={1}&SFZJH_402404={2}&SZDW_439708={3}&ZY_878153={4}&GDXW_926421={5}&DSNAME_606453={6}&PYLB_253720={7}&SELECT_172548={8}&TEXT_91454={9}&TEXT_24613={10}&TEXT_826040={11}&RADIO_799044=%E6%AD%A3%E5%B8%B8%EF%BC%88%33%37%2E%33%E2%84%83%EF%BC%89&RADIO_907280=%E5%81%A5%E5%BA%B7&RADIO_384811=%E6%A0%A1%E5%86%85&RADIO_716001=%E5%81%A5%E5%BA%B7&RADIO_248990=%E5%90%A6'.format(
        dic1[0], dic1[2], dic1[3], dic1[4], dic1[5], dic1[6], dic1[7], dic1[8], dic1[9], dic1[10], dic1[11], dic1[12])

    pr = s.post(purl, data=pdata, headers=pheaders)
    pr.text
    if pr.text[10:14] == 'true':
        print('Success!')
    print(pr.text)
    ok = 'Success!'
    return ok

# %%
