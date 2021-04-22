#!/usr/bin/env python
# coding: utf-8

# In[1]:
from absl import flags, app
import configparser
from urllib import parse
import hhu

FLAGS = flags.FLAGS
flags.DEFINE_string('u', None, 'set username')
flags.DEFINE_string('p', None, 'set password')


def main(_):
    username = ""
    password = ""
    if FLAGS.u and FLAGS.p:
        username, password = FLAGS.u, FLAGS.p
    else:
        config = configparser.RawConfigParser()
        if config.read('info.ini',encoding='utf-8-sig'):
            print('若在仓库中使用该程序，推荐使用arg传参形式传入账号密码')
        else:
            raise OSError("info.ini not exists")
        dic1=['学号','密码']

        for i in range(len(dic1)):
            dic1[i] = config.get('personal_info', dic1[i])
            dic1[i] = parse.quote(dic1[i])
        username, password = dic1[0], dic1[1]

    hhu.hhu(username, password)

if __name__ == '__main__':
    app.run(main)
