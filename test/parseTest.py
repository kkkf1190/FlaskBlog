import sys,urllib,os
sys.path.append('D:\\PycharmProjects\\FlaskBlog')
from model import ZhihuModel
from htmlparse import MyHTMLParser

localPath = '..\\static\\image\\content'

def createFileWithFileName(localPathParam,fileName):
    totalPath=localPathParam+'\\'+fileName
    if not os.path.exists(totalPath):
        file=open(totalPath,'a+')
        file.close()
        return totalPath


zhihus = ZhihuModel.objects()
for zhihu in zhihus:
    downloadImg(zhihu)
