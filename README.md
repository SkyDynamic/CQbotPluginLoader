# QQbot
一个练习作品，QQbot基于go-cqhttp，反向http post协议  
这个程序可以支持热加载插件  
一些自己写插件都会放在这里  
# 给我看这个！！！！
请把你的插件放进plugin文件加内：
目录结构
```
──QQBot
    │  bot.py
    │  cheak_plugin.py
    │  config.json
    │  start.bat
    │  
    └─plugin
        │  __init__.py
```
# Help
windows可以直接运行`start.bat`来运行程序  
其他系统可以使用`python bot.py`运行
你需要按照一定格式编写插件
## 你的插件需要包含以下信息：
`SLUG = '插件ID'`  
`一个run函数[def run(gid,message,uid):]`  
### 例子：
```
import requests
SLUG = 'test'#引号内填写你的插件ID
def run(gid,message,uid):
    msg = 'Hello World'
    if message[0] == 'test':#判断Q群指令，默认可以从config里面配置指令前缀(默认为 . ),插件内不需要写前缀
        send(gid, msg)#发送群信息
    send(gid, msg)#发送群信息
def send(gid, message):
	with open('./config.json', 'r', encoding='utf-8') as f:
		botconfig = json.load(f)
	put = 'http://{0}:{1}/send_group_msg?group_id={2}&message={3}&auto_escape=false'
	requests.get(url=put.format(botconfig['host'],str(botconfig['api_port']),gid, message))
```
![image](https://s1.328888.xyz/2022/06/03/W835R.png)

# 注意：
config内的host都对应go-cqhttp内的config.yml  
使用前请注意端口对应
