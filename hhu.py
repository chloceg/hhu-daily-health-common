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
    config.read('info.ini',encoding='utf-8-sig')
    dic1=['学号','密码','姓名','身份证号','学院','年级','专业','班级','宿舍楼','宿舍号','手机号']
    
    for i in range(0,11):
        dic1[i] = config.get('personal_info', dic1[i])
        dic1[i] = parse.quote(dic1[i])
        


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    data = {
        'Login.Token1':'{}'.format(dic1[0]),
        'Login.Token2':'{}'.format(dic1[1]),
        'goto':'http://my.hhu.edu.cn/loginSuccess.portal',
        'gotoOnFail':'http://my.hhu.edu.cn/loginFailure.portal',
    }
    

    utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    sh_tz = timezone(timedelta(hours=8),name='Asia/Shanghai')
    beijing_now = utc_time.astimezone(sh_tz)
    
    datestr = datetime.strftime(beijing_now,'%F')
    timestr = datetime.strftime(beijing_now,'%H:%M:%S')
    year = datestr[0:4]
    month = datestr[5:7]
    day = datestr[8:10]
    time = timestr
    

    
    s = requests.session()
    r = s.post(url, data=data, headers=headers)
    r.text
    purl = 'http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid=A335B048C8456F75E0538101600A6A04&userId={}'.format(dic1[0])
    pheaders = {
        "Accept": "application/json, text/javascript, */*; q=0.01","Accept-Encoding": "gzip, deflate","Accept-Language": "en-us",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }



    pdata = 'DATETIME_CYCLE='+year+'%2F'+month+'%2F'+day+'&XGH_336526={0}&XM_1474={1}&SFZJH_859173={2}&SELECT_941320={3}&SELECT_459666={4}&SELECT_814855={5}&SELECT_525884={6}&SELECT_125597={7}&TEXT_950231={8}&TEXT_937296={9}&RADIO_853789=%E5%90%A6&RADIO_43840=%E5%90%A6&RADIO_579935=%E5%81%A5%E5%BA%B7&RADIO_138407=%E6%98%AF'.format(dic1[0],dic1[2],dic1[3],dic1[4],dic1[5],dic1[6],dic1[7],dic1[8],dic1[9],dic1[10])

    pr = s.post(purl, data=pdata, headers=pheaders)
    pr.text
    if pr.text[10:14]=='true':
        print('Success!')
    ok='Success!'
    return ok
