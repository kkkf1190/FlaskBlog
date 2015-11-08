import os,urllib,json
from htmlparse import MyHTMLParser
from model import ZhihuModel

localPath = 'static\\image'
contentPath = 'static\\image\\content'

def createFileWithFileName(localPathParam,fileName):
    totalPath=localPathParam+'\\'+fileName
    if not os.path.exists(totalPath):
        file=open(totalPath,'a+')
        file.close()
        return totalPath

def downloadFront(zhihu):
    url2 = str(zhihu.item_frontimg)
    frontimg = url2[22:]
    print(url2)
    frontimgdata=urllib.request.urlopen(url2).read()
    open(createFileWithFileName(localPath,frontimg), "wb").write(frontimgdata)
    zhihu.item_frontimg = frontimg
    zhihu.save()

def downloadImg(zhihu):
    parse = MyHTMLParser()
    parse.feed(zhihu.item_content)
    for img in parse.links:
        print(img)
        url = img
        frontimg = url[22:]
        frontimg = frontimg.replace('70/','')
        frontimg = frontimg.replace('/','')
        print(frontimg)
        frontimgdata=urllib.request.urlopen(url).read()
        open(createFileWithFileName(contentPath,frontimg), "wb").write(frontimgdata)
        url2 = "/static/image/content/"+frontimg
        print(url2)
        zhihu.item_content = zhihu.item_content.replace(img,url2)
        zhihu.save()

def pullstories(story,date):
    imgurl = str(story['images'][0])
    img = imgurl[22:]
    # imgdata=urllib.request.urlopen(imgurl).read()
    # print(img)
    # open(createFileWithFileName(localPath,img), "wb").write(imgdata)
    storyModel = ZhihuModel(item_id = story['id'] )
    storyModel.item_date = date
    storyModel.item_title = story['title']
    storyModel.item_frontimg = str(story['images'][0])
    itemid = story['id']
    url1 = "http://news-at.zhihu.com/api/4/news/"+str(itemid)
    itemContent = urllib.request.urlopen(url1).read()
    content_data=itemContent.decode('UTF-8')
    content = json.loads(content_data)
    storyModel.item_content = content['body']
    storyModel.item_css = content['css'][0]
    storyModel.save()
    return storyModel