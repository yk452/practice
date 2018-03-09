#-*-coding:utf-8-*-

import comtypes.client #The comtypes package makes it easy to access and implement both custom and dispatch based COM interfaces
import os  #os是python中用来处理目录和文件的模块

def init_powerpoint():
    # comtypes.client的CreateObject方法用来创建一个COM对象并返回一个接口指针
    powerpoint=comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible=1
    return powerpoint
def ppt_to_pdf(powerpoint,inputFileName,outputFileName,formatType=32):
    #print(inputFileName);print(outputFileName)
    if outputFileName[-3:] == 'ppt':
        outputFileName = outputFileName[:-3] + "pdf"
    elif outputFileName[-4:] == 'pptx':
        outputFileName = outputFileName[:-4] + "pdf"
    # outputFileName=outputFileName+".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)  # 打开ppt文件
    deck.SaveAs(outputFileName, formatType)  # 保存为formType为32也就是pdf文件
    deck.Close()  # 关闭ppt文件

def convert_files_in_folder(powerpoint,folder):
    files = os.listdir(folder) #列出folder目录下的文件,打印出来是个列表
    pptfiles=[f for f in files if f.endswith((".ppt",".pptx"))]#Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False
    for pptfile in pptfiles:
        fullpath=os.path.join(cwd,pptfile)#连接目录和文件名，获得ppt文件的目录
        ppt_to_pdf(powerpoint,fullpath,fullpath)

if __name__ =="__main__":
    powerpoint = init_powerpoint()
    cwd = os.getcwd() #获取当前工作目录,比如：E:\github\practice\pystart
    convert_files_in_folder(powerpoint,cwd)
    powerpoint.Quit()
