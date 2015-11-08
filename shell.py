import sys
sys.path.append('D:\\PycharmProjects\\FlaskBlog')
from util import pullstories
import urllib,json,os
import urllib.request

from util import downloadFront





localPath = 'static\\image'
url = "http://news-at.zhihu.com/api/4/news/latest"
data=urllib.request.urlopen(url).read()
z_data=data.decode('UTF-8')
items = json.loads(z_data)
stories = items['stories']
date = items['date']
for story in stories:
    storyMol = pullstories(story,date)