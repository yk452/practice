#-*-coding:utf-8-*-

import unittest
import requests
import time
import re
import pyexcel

class TestGetIpInfoByExcel(unittest.TestCase):
    testcaseList=[]
    def getCityFromIp(self,ipStr):
        params={"ip":ipStr}
        result=requests.get("http://ip.taobao.com/service/getIpInfo.php",params=params)
        return result.json()["data"]
    def testRunTheCase(self):
        self.testcaseList=pyexcel.iget_records(file_name="测试案例.xlsx")
        print(self.testcaseList,"33333")
        for caseDict in self.testcaseList:
            print(caseDict)
            time.sleep(3)
            with self.subTest(msg=caseDict["案例意图"]):
                result = self.getCityFromIp(caseDict["ip"])
                if (isinstance(result,str)):
                    self.assertEqual(caseDict["expect"],result,msg=caseDict["案例意图"])
                else:
                    self.assertEqual(caseDict["expect"],result["city"],msg=caseDict["案例意图"])

if __name__ == "__main__":
    unittest.main()

