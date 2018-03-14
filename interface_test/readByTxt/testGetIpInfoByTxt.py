#-*-coding:utf-8-*-

import unittest
import requests
import time #python中的一个时间模块
import re #python中的正则模块

class TestGetIpInfoByFile(unittest.TestCase):
    testcaseList=[]
    def getCityFromIp(self,ipStr):
        params = {"ip":ipStr}
        result=requests.get("http://ip.taobao.com/service/getIpInfo.php",params=params)
        return result.json()["data"]
    def testRunTheCase(self):
        self.loadTestCaseFromFile("测试案例1.txt")
        self.loadTestCaseFromFile("测试案例2.txt")
        self.loadTestCaseFromFile("测试案例3.txt")
        for caseDict in self.testcaseList:
            time.sleep(3)
            with self.subTest(msg=caseDict["案例意图"]):#subTest方法应是继承自unittest
                result=self.getCityFromIp(caseDict["ip"])
                if(isinstance(result,str)):
                    self.assertEqual(caseDict["expect"],result,caseDict["案例意图"])
                else:
                    self.assertEqual(caseDict["expect"],result["city"],caseDict["案例意图"])

    def loadTestCaseFromFile(self,fileName):
        with open(fileName,'r') as file:
            testItem={}
            for line in file:
                if(re.match("\s*#",line)):
                    continue
                result=re.match(r'\s*\"([^\"]+)\"\s*:\s*\"([^\"]+)\"',line)
                print(result)
                if(result != None):
                    testItem[result.group(1)]=result.group(2)#正则表达式匹配到的对象，可通过group方法获取到，从1开始
                if(re.match(r"\s*-{3,}",line)):#re.match 尝试从字符串的起始位置匹配一个模式
                    self.testcaseList.append(testItem.copy())#列表的append方法用于添加列表项
                    testItem={}
                    continue

if __name__ == "__main__":
    unittest.main()



