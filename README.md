<a href="https://github.com/chloceg/hhu-daily-health-common/actions"><img src="https://badgen.net/badge/test/passing/green" alt="Build Status"></a>


# hhu-daily-health

河海大学每日健康打卡

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
## 2021年2月1日
所有的就都写在一个程序里了，有时间再做个通用版供大家使用吧。在Actions里每天跑一下就可以了^_^ 

## 2021年2月3日
通用版写好啦，让我们看看怎么用呢 q(≧▽≦q)
## 教学阶段
1、右上角fork一份到你自己的本地仓库

2、进入fork的仓库，点击右上角的`Settings`，选择`Secrets`菜单，点击`New repository secret`。设置一个名为`ACCOUNT_INFO`的secret，其值为学校健康填报网站的用户名和密码（中间用`空格`或`换行符`隔开），具体步骤可参照下图（同时兼容`info.ini`文件配置账号密码方式，见下方`info.ini`，若在GitHub上使用，请将仓库`make private`!）

- 选择新建secret

     ![image](https://user-images.githubusercontent.com/15844309/115863698-6865fb00-a468-11eb-8d79-14453ac752b1.png)

- secret填写（`username`和`password`用健康填报网站的账号密码代替）

     ![image](https://user-images.githubusercontent.com/15844309/115863310-dcec6a00-a467-11eb-8fd4-c7683ce17a60.png)

- 文件配置方式（不推荐在Github仓库中使用）

      # info.ini
      [personal_info]
      学号=
      密码=

3、所有这个程序用到的python非标准库的依赖包在requirements.txt里，主程序是main.py，你可以下载到本地用python运行，但那样每天需要手动运行，失去了自动打卡解放双手的意义。所以我推荐使用Github的Actions，它可以按照你的要求创建一个工作流（使用的系统可以是Windows、Linux Ubuntu等），满足适当条件时便会自动运行。

### 创建一个工作流

- 点击Actions：

    <img width="800" height="200" src="https://i.loli.net/2021/02/17/6xD2mHTnZde5fzW.jpg" alt="点击Actions"/>


- 点击set up a workflow yourself:
    <img width="800" height="220" src="https://i.loli.net/2021/02/17/LbwJIu3CK2BFUHc.jpg" alt="点击set up a workflow yourself"/>


- 在编辑框填写以下代码：

    <img width="800" height="420" src="https://i.loli.net/2021/02/17/8zEvtqRMXWa2Jej.jpg" alt="在编辑框填写代码"/>


    ```
    name: hhu-auto-clock-in
    on:
      schedule:
        - cron: "1 0 * * *"  # scheduled at 08:01 (UTC+8) everyday #每天早上八点零一分打卡

      workflow_dispatch: # workflow手动触发

    jobs:
      report:
        runs-on: ubuntu-latest

        steps:
          - name: checkout master
            uses: actions/checkout@v2

          - name: setup python
            uses: actions/setup-python@v2
            with: 
              python-version: 3.8

          - name: download dependance
            run: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt

          # set to env:params
          - name: get account info
            shell: bash
            env: 
              ACCOUNT_INFO: ${{ secrets.ACCOUNT_INFO }}
            if: env.ACCOUNT_INFO != null
            run: |
              arr=(${{env.ACCOUNT_INFO}})
              if [ "${#arr[@]}" -gt "1" ]; then
                echo "params=--u ${arr[0]} --p ${arr[1]}" >> ${GITHUB_ENV}
              fi

          # run main.py
          - name: Run the program
            run: |
              python3 main.py ${{env.params}}
    ```

- 然后点Start commit就可以了

4、手动运行一下试试，点Actions, hhu-auto-clock-in, run workflow，等待几十秒，出现绿色就代表运行成功。再去信息门户上看下打卡历史记录，应该就有了。

<img width="800" height="380" src="https://i.loli.net/2021/02/17/8FgyTWJCA7BMVUe.jpg" alt="run workflow"/>
  
5、然后这个程序每天早上八点零一会自动排队运行，GitHub一般延迟几分钟到十几分钟不等，真正实现白嫖，一劳永逸！

几个问题：有些同学没有把这个仓库make private，这样你的密码都被别人看到了。。。有个同学info.ini里的“密码”两个字之间加了个空格。。。程序就跑不起来，唉，我写程序也就是半吊子，鲁棒性很差的，我还在慢慢学习，尽量改善这种体验。

#### p.s. 如果有帮助的话，点一个小小的Star可好？
