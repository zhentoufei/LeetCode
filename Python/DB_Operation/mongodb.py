# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/26 22:42'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'mongodb.py'


from datetime import datetime
from pymongo import MongoClient

from bson.objectid import ObjectId

#在pumongo里面使用了连接池把

class TestMongo(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def addOne(self):
        post = {
            'title': '111111',
            'content': '11111111111111111111111111111111111111',
            'created_at': datetime.now(),
            'x': 1
        }
        return self.db.blog.posts.insert_one(post)

    def getOne(self):
        '''查询一条数据'''
        return self.db.blog.posts.find_one()

    def getMore(self):
        '''查询多条数据'''
        return self.db.blog.posts.find({'content': '博客内容...'})


    def getOneFromId(self, id):
        ''' 查询制定ID的数据 '''
        # return self.db.blog.posts.find_one({'_id': id}) # 注意这种方法是获取不到结果的，最终返回的是None

        # 通过模块的ObjectId实现id的传入
        obj = ObjectId(id)
        return self.db.blog.posts.find_one({'_id': obj})


    def update(self):
        ''' 修改数据 '''

        # 修改一条数据
        rest = self.db.blog.posts.update_one({'x': 1}, {'$inc': {'x': 10}})

        # 修改多条数据
        return self.db.blog.posts.update_many({}, {'$inc': {'x':10}})

    def delete(self):
        ''' 删除数据 '''

        # 删除一条数据
        # return self.db.blog.posts.delete_one({'x': 10})

        # 删除多条数据
        return self.db.blog.posts.delete_many({'x': 31})

if __name__ == '__main__':
    # client1 = MongoClient()
    # client2 = MongoClient('localhost', 27017)
    # client3 = MongoClient('mongodb://localhost:27017/')

    obj = TestMongo()
    # obj.addOne()
    # rest = obj.getOne()
    # print rest

    # rest2 = obj.getMore()
    # for item in rest2:
    #     print item['_id']

    # print obj.getOneFromId('59d9bf387fdd0830b01a4763')

    # print obj.update()

    print obj.delete().deleted_count