#-*-coding:utf-8-*-

import requests
import json
import math #python中的数学计算模块
import random

class TestLogin:

    login_info = {'username': 'supervisor', 'password': '111111'}
    headers = {"Content-Type": "application/json"}

    def testLogin(self):
        r = requests.request('POST', "http://183.81.180.222:2227/public/login", headers=self.headers,
                             data=json.dumps(self.login_info))
        token=r.json()["token"]
        jm=self.encrypt(self.login_info["password"],token)
        login_info2={"username":"supervisor",'password':jm}
        print(login_info2)
        r2=requests.request('POST',"http://183.81.180.222:2227/public/loginTwo",headers=self.headers,data=json.dumps(login_info2))
        print(r2.json())
        return token

    def encrypt(self,pas,pwd):
        pwd_len=len(pwd)
        if (pwd == None or pwd_len <=0):#python中None相当于js中的null
            print("登录失败，请重试")
            return None
        prand=""
        for i in range(0,pwd_len):
            fit=ord(pwd[i])
            prand += str(fit)      #python中的ord函数相当于js中的charCodeAt(),会返回字符的unicode编码
        print(prand,"字符数字编码字符串连接")
        sPos=math.floor(len(prand)/5) #对prand除5的结果向下取整
        mult=int(prand[sPos]+prand[sPos*2]+prand[sPos*3]+prand[sPos*4]+prand[sPos*5])#获取prand相应位置的字符并转换为整数
        incr=math.ceil(pwd_len/2) #对pwd_len除2向上取整
        modu=pow(2,31)-1
        if mult < 2:
            print("Algorithm cannot find a suitable hash. Please choose a different password. \nPossible considerations are to choose a more complex or longer password.")
            return None
        salt=round(random.random()*1000000000)%100000000#取0-1之间的随机数并乘以10亿再除以1亿取余数
        prand+=str(salt)
        print(prand,"prand与取模的值的字符串连接后的prand")
        while len(prand)>10:
            prand=str(int(prand[0:10])+int(prand[10:len(prand)]))
        print(prand,"取prand的前10与后面的值相加循环后的字符串prand")
        prand=(mult*int(prand)+incr)%modu
        print(prand,"暂且为整数")
        enc_chr=""
        enc_str=""
        for k in range(0,len(pas)):
            enc_chr=int(ord(pas[k]) ^ math.floor((prand/modu)*255))#^为python的按位异或运算符，当两对应的二进位相异时为1
            print(enc_chr,"按位异或运算结果显示",k)
            if enc_chr < 16:
                enc_str += "0"+str(hex(enc_chr))#hex方法是将10进制转换为16进制
                print(enc_str,"字符串1",k)
            else:
                enc_str += str(hex(enc_chr))
                print(enc_str,"字符串2", k)
            prand=(mult * prand + incr) % modu
            print(prand,k)
        salt=str(hex(salt))
        while len(salt)<8:
            salt="0"+salt
        enc_str+=salt
        print(enc_str)
        return enc_str



if __name__ == '__main__':
    TestLogin().testLogin()