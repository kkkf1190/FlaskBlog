from flask import Flask,render_template
from util import createFileWithFileName
from model import TestModel,ZhihuModel
import urllib,json
import urllib.request

app=Flask(__name__)

@app.route('/')
def hello_world():
	url = "http://news-at.zhihu.com/api/4/news/latest"
	data=urllib.request.urlopen(url).read()
	z_data=data.decode('UTF-8')
	items = json.loads(z_data)
	i=0
	stories = ZhihuModel.objects()
	return render_template('home.html',stories=stories)

@app.route('/user/<username>')
def user(username):
	item = TestModel(id='1')
	item.text=str(username)
	print(item.text)
	return '<h1>welcome! %s</h1>' % username

@app.route('/detile/<itemid>')
def detile(itemid):
	zhihus = ZhihuModel.objects()
	for zhihu in zhihus:
		if(zhihu.item_id==int(itemid)):
			item = zhihu
			break
	return render_template('detail.html',item=item)


if __name__ == '__main__':
	app.run()
