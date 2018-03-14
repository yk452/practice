#-*-coding:utf-8-*-

import unittest
import requests
import time

class TestGetIPInfo(unittest.TestCase):
    testcaseList=[{"msg":"ReturnGoodWhenGetIpInfoGivenNormalIPInBeijing","ip":"124.126.228.193","expect":"北京"},
                  {"msg": "ReturnErrorMsgWhenGetIpInfoGivenInvalidIP", "ip": "124.126.228.", "expect": "invaild ip."}]
    def getCityFromIP(self,ipStr):
        params = {"ip": ipStr}
        result = requests.get("http://ip.taobao.com/service/getIpInfo.php", params=params)
        print(result.json()["data"])
        return result.json()["data"]
    def testRunTheCase(self):
        for caseDict in self.testcaseList:
            time.sleep(3)
            with self.subTest(msg=caseDict["msg"]):#with在下面代码抛出错误时，都可以被处理，保证程序继续进行
                result=self.getCityFromIP(caseDict["ip"])
                if(isinstance(result,str)):
                    self.assertEqual(caseDict["expect"],result,caseDict["msg"]) #assertEqual第三个参数msg，即message
                else:
                    self.assertEqual(caseDict["expect"],result["city"],caseDict["msg"])

if __name__ == "__main__":
    unittest.main()