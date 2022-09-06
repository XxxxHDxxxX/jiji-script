#此脚本为几鸡机场签到脚本如果你没有注册请到这个链接注册https://b.luxury/waf/PgAB7k3DmpXU1bNf2
#作者 XxxxHuangDIxxxX & 毛毛
import requests
import re
import json
import time
import os
import sys


session = requests.session()
#账号密码存放处
data = {
  "email": "256964797",
  "passwd": "zjl123321..."
}

#登录
url = "https://a.luxury/signin?c=0.7831298079748228"
session.post(url,data=data)

#签到
resp = session.post('https://a.luxury/user/checkin?c=0.3588015978783363')
page_content = resp.content.decode('unicode_escape')
#正则表达式匹配
obj = re.compile(r'"msg":"(?P<name>.*?)"', re.S)
result = obj.finditer(page_content)

a=[]

for it in result:
#输出结果
 print(it.group("name"))
 a.append(it.group("name"))

if a == [] :
    print("账号或密码错误，请检查")

