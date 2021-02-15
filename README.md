# ICBC_appointment


## 功能
自动刷新ICBC预约系统，找到合适的时间。


## 安装
**请预先安装python2.7 版本**


## 用法

### 笔试刷新

- 打开命令行直接运行：

`python knowledge_test.py locations.json {YYYY-MM}`

不间断刷新知道有可用的预约时间，电脑会发出声音。

### 路考刷新

同上修改expectMonth后，运行:

`python road_test.py {driverLastName} {licenceNumber} {keyword}`

说明
- driverLastName, 登陆使用的Last Name
- licenceNumber, 驾照号码
- keyword 登陆密码

