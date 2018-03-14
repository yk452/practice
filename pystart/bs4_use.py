#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

class ShowHtmlAttr:
    def showattr(self):
        result=requests.session().get("http://www.baidu.com")#requests.session()方法可以保存session信息，用于接下来的请求
        #print(result.content.decode(),"111111111")
        #soup = BeautifulSoup(result.text, "html.parser") #text是字符串
        soup = BeautifulSoup(result.content, "html.parser")#content是字节流
        print(soup.prettify(),"222222222")
        atags=soup.find_all("a")
        print(atags,"333333333")
        for atag in atags:
            print("[{0}]的链接是:{1}".format(atag.text,atag.attrs['href']))


if __name__ == "__main__":
    ShowHtmlAttr().showattr()