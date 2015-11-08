import sys
sys.path.append('D:\\PycharmProjects\\FlaskBlog')
from model import TestModel
test = TestModel(testid='1')
test.text='test1'
test.save()