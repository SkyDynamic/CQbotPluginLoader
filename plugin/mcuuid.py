from uuid import UUID
import hashlib
import re
import json
import requests

SLUG = 'mcuuid'
__all__=["nameUUIDFromBytes","checkPlayerName","offlineUUID","onlineUUID"]

def nameUUIDFromBytes(name: bytes) -> UUID:
    md5 = hashlib.md5()
    md5.update(name)
    md5Bytes = bytearray(md5.digest())
    md5Bytes[6] &= 0x0F
    md5Bytes[6] |= 0x30
    md5Bytes[8] &= 0x3F
    md5Bytes[8] |= 0x80
    return UUID(bytes=bytes(md5Bytes))

class Mcuuid():
    def checkPlayerName(player: str) -> bool:
        return (re.fullmatch(r"\w+",player) is not None) and len(player)<=16

    def get_offlineUUID(player: str) -> UUID:
        if not Mcuuid.checkPlayerName(player):
            return None
        return nameUUIDFromBytes(("OfflinePlayer:" + player).encode())

    def get_uuid(player: str) -> UUID:
        if not Mcuuid.checkPlayerName(player):
            return None
        response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + player)
        if response.status_code == 204:
            return "[动空Bot]未能找到此用户名的玩家"
        elif response.status_code != 200:
            return "[动空Bot]未知错误"
        result = response.json()
        trimmedUUID=result['id']
        return UUID(trimmedUUID)

def run(gid,message,uid):
    if message[0] == 'mcuuid':
        uuid = Mcuuid.get_uuid(message[1])
        if uuid == "[动空Bot]未能找到此用户名的玩家" or uuid == '"[动空Bot]未知错误"':
            send(gid, uuid)
        else:
            send(gid,f'[CQ:at,qq={uid}]\n玩家名：{message[1]}\nUUID：{uuid}')
    elif message[0] == 'ofmcuuid':
        uuid = Mcuuid.get_offlineUUID(message[1])
        send(gid,f'[CQ:at,qq={uid}]\n您获取的是离线玩家UUID\n玩家名：{message[1]}\nUUID：{uuid}')

def send(gid, message):
	with open('./config.json', 'r', encoding='utf-8') as f:
		botconfig = json.load(f)
	put = 'http://{0}:{1}/send_group_msg?group_id={2}&message={3}&auto_escape=false'
	requests.get(url=put.format(botconfig['host'],str(botconfig['api_port']),gid, message))
