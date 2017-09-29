# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/25 14:19'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'db_orm.py'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engin = create_engine("mysql://root:123456@127.0.0.1:3306/news?charset=utf8")
Base = declarative_base()

Session = sessionmaker(bind=engin)


class News(Base):
    __tablename__ = 'news_test'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), )
    author = Column(String(20), )
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        '''新增记录'''
        new_obj = News(
            title='标题',
            content='内容',
            types='百家',
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        return self.session.query(News).filter('id=2').first().title

    def update_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    def update_datas(self):
        '''增加多条记录'''
        data_list = self.session.query(News).filter_by(is_valid=True)
        for item in data_list:
            item.is_valid = 0
            self.session.add(item)
        self.session.commit()

    def delete_data(self, pk):
        '''删除数据'''
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()






def main():
    obj = OrmTest()
    # rest = obj.add_one()
    # print rest.id
    rest = obj.get_one()
    print rest


if __name__ == '__main__':
    main()
