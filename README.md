# QQbot
一个练习作品，QQbot基于go-cqhttp，反向http post协议
这个程序可以支持热加载插件
一些自己写插件都会放在这里

# Help
你需要按照一定格式编写插件
## 你的插件需要包含以下信息：
`SLUG = '插件ID'`  
`一个run函数[def run(gid,message,uid):]`  
### 例子：
```
import requests
SLUG = 'test'#引号内填写你的插件ID
def run(gid,message,uid)
    msg = 'Hello World'
    send(gid, msg)#发送群信息
def send(gid, message):#用于发送群信息
    put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
    requests.get(url=put.format(gid, message))
