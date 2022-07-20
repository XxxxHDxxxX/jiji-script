#此脚本为几鸡机场签到脚本如果你没有注册请到这个链接注册https://b.luxury/waf/PgAB7k3DmpXU1bNf2
#作者 XxxxHuangDIxxxX & 毛毛
import requests
import re
import json
import time
import os
import sys


#获取email
def get_id():
    if os.environ.get("jcid"):
        jcid = os.environ["jcid"]
        print("已获取用户名"+" "+jcid)
        return jcid
    else:
        print("获取账号失败，请export jcid='你的账号'")

email=get_id() 

#获取密码            
def get_pw():
    if os.environ.get("jcpw"):
        jcpw = os.environ["jcpw"]
        lenth = len(jcpw)
        l = list(jcpw)
        lenth1=lenth-1
        pw=l[0]+"****"+l[lenth1]
        print("已获取密码"+" "+pw)
        return jcpw
    else:

        print("获取密码失败，请export jcpw='你的密码'")     

passwd=get_pw()

session = requests.session()
#账号密码存放处
data = {
  "email": email,
  "passwd": passwd
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

