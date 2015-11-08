import urllib,json,os
import urllib.request

def createFileWithFileName(localPathParam,fileName):
    totalPath=localPathParam+'\\'+fileName
    if not os.path.exists(totalPath):
        file=open(totalPath,'a+')
        file.close()
        return totalPath


localPath = 'static\\image'
url = "http://news-at.zhihu.com/api/4/news/latest"
data=urllib.request.urlopen(url).read()
z_data=data.decode('UTF-8')
items = json.loads(z_data)
stories = items['stories']
url1 = stories[0]['images'][0]
i=0
for story in stories:
    imgurl = str(stories[i]['images'][0])
    img = imgurl[22:]
    imgdata=urllib.request.urlopen(imgurl).read()
    print(img)
    open(createFileWithFileName(localPath,img), "wb").write(imgdata)
    i+=1