<a href="https://github.com/chloceg/hhu-daily-health-common/actions"><img src="https://badgen.net/badge/test/passing/green" alt="Build Status"></a>


# hhu-daily-health

河海大学每日健康打卡

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
## 2021年11月24日   [@Miaosful](https://github.com/Miaosful)
似乎研究生跟本科生的打卡有点不一样，这个版本适用于研究生打卡，本科生应该修改几个参数就行了

***

***

以下之前的教程仅供参考，不适用于目前版本，过往版本可在[Commits](https://github.com/chloceg/hhu-daily-health-common/commits/master)中查询

## 2021年7月17日   [@chloceg](https://github.com/chloceg)
由于爷毕业了，而且学校的信息门户版本更迭，登陆方式发生了迭代，所以目前的项目并不支持最新打卡，请后辈继续努力，写出新的打卡程序！

## 2021年2月1日   [@chloceg](https://github.com/chloceg)
所有的就都写在一个程序里了，有时间再做个通用版供大家使用吧。在Actions里每天跑一下就可以了^_^ 

## 2021年2月3日   [@chloceg](https://github.com/chloceg)
通用版写好啦，让我们看看怎么用呢 q(≧▽≦q)
## 教学阶段
1、右上角fork一份到你自己的本地仓库(记得make private，要不然别人点进你的repositories，就能看到你填的个人信息)

2、将平时填在打卡网页上的个人信息填入info.ini文件中（因为是fork到自己的仓库里使用，所有不用担心隐私问题，如果还是不放心，可以研究一下Github Actions里的Secrets怎么用）


<img width="700" height="400" src="https://i.loli.net/2021/02/17/mqb3FnDLv2zKJkB.jpg" alt="这是一张info.ini的截图"/>
<img width="550" height="530" src="https://i.loli.net/2021/02/17/B87ybZHT5MY3ucV.jpg" alt="我们打卡的网站"/>


3、所有这个程序用到的python非标准库的依赖包在requirements.txt里，主程序是main.py，你可以下载到本地用python运行，但那样每天需要手动运行，失去了自动打卡解放双手的意义。所以我推荐使用Github的Actions，它可以按照你的要求创建一个工作流（使用的系统可以是Windows、Linux Ubuntu等），满足适当条件时便会自动运行。

### 创建一个工作流

点击Actions：

<img width="800" height="200" src="https://i.loli.net/2021/02/17/6xD2mHTnZde5fzW.jpg" alt="点击Actions"/>


点击set up a workflow yourself:
<img width="800" height="220" src="https://i.loli.net/2021/02/17/LbwJIu3CK2BFUHc.jpg" alt="点击set up a workflow yourself"/>


在编辑框填写以下代码：

<img width="800" height="420" src="https://i.loli.net/2021/02/17/8zEvtqRMXWa2Jej.jpg" alt="在编辑框填写代码"/>


```
# This is a basic workflow to help you get started with Actions

name: hhu-auto-clock-in

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  schedule:
    - cron: "1 0 * * *"  # scheduled at 08:01 (UTC+8) everyday #每天早上八点零一分打卡
      
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - name: checkout master
        uses: actions/checkout@v2
      
      - name: setup python
        uses: actions/setup-python@v2
        with: 
          python-version: 3.8
      
      # Runs a set of commands using the runners shell
      - name: Run the program
        
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          python3 ./main.py
```

然后点Start commit就可以了

4、手动运行一下试试，点Actions, hhu-auto-clock-in, run workflow，等待几十秒，出现绿色就代表运行成功。再去信息门户上看下打卡历史记录，应该就有了。

<img width="800" height="380" src="https://i.loli.net/2021/02/17/8FgyTWJCA7BMVUe.jpg" alt="run workflow"/>
  
5、然后这个程序每天早上八点零一会自动排队运行，GitHub一般延迟几分钟到十几分钟不等，真正实现白嫖，一劳永逸！

#### p.s. 如果有帮助的话，点一个小小的Star可好？
