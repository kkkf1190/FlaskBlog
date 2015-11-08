import urllib,json
from model import ZhihuModel
from util import pullstories,downloadFront,downloadImg

url = "http://news-at.zhihu.com/api/4/news/latest"
data=urllib.request.urlopen(url).read()
z_data=data.decode('UTF-8')
items = json.loads(z_data)
stories = items['stories']
date = items['date']
storyModels = ZhihuModel.objects
for story in stories:
    flag=0
    item_id = story['id']
    for model in storyModels:
        if(model.item_id==item_id):
            flag=1
    if(flag==0):
        storyMol = pullstories(story,date)
        downloadFront(storyMol)
        downloadImg(storyMol)
