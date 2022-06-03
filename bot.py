from flask import Flask, request
import threading
import requests
import logging
import cheak_plugin
import json
import os

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
default_config = {
    'post_port': 5701,
    'host': '127.0.0.1',
    'command_prefix': '.'
}


helpmessage = '''----[动空Bot]目前支持的功能----
- .help -> 显示这条信息
- .player -> 获取MC服务器在线玩家（需要跟动空说明绑定地址）
- .jrrp -> 测试你今天的运势（每天四点刷新）
- .mcuuid -> 查找正版玩家的UUID
- .ofmcuuid -> 获取离线玩家UUID（不一定准确）'''

@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        try:
            t1 = threading.Thread(target = player1,args = (uid, message, gid))
            t1.start()
        except:
            print ("Error: unable to start thread")
    return 'OK'

def player1(uid, message, gid=None):
    a = 0
    if message:
        msg = message.split(' ')
        msg[0] = msg[0].replace(config['command_prefix'],'')
        for i in plugin:
            plugin[a].run(gid, msg, uid)
            a = a + 1

if __name__ == '__main__':
    plugin = cheak_plugin.cheak_plugin()
    if not os.path.exists('config.json'):
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)
    else:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    app.run(debug=True, host=config['host'], port=config['post_port']) 