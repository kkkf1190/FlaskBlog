from flask import Flask,render_template
from util import createFileWithFileName
from model import TestModel
import urllib,json
import urllib.request

app=Flask(__name__)

@app.route('/')
def hello_world():
	url = "http://news-at.zhihu.com/api/4/news/latest"
	data=urllib.request.urlopen(url).read()
	z_data=data.decode('UTF-8')
	items = json.loads(z_data)
	stories = items['stories']
	i=0
	for story in stories:
		imgurl = str(stories[i]['images'][0])
		img = imgurl[22:]
		stories[i]['images'][0]=img
		i+=1
	return render_template('home.html',stories=stories)

@app.route('/user/<username>')
def user(username):
	item = TestModel(id='1')
	item.text=str(username)
	print(item.text)
	return '<h1>welcome! %s</h1>' % username

@app.route('/detile/<itemid>')
def detile(itemid):
	url = "http://news-at.zhihu.com/api/4/news/"+itemid
	print(url)
	data=urllib.request.urlopen(url).read()
	z_data=data.decode('UTF-8')
	item = json.loads(z_data)
	itembody = item['body']
	itemcss = item['css'][0]
	itemtitle = item['title']
	print(itemcss)
	return render_template('home.html',item=item)


if __name__ == '__main__':
	app.run()
