# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/23 22:21'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'mysql.py'

import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')


class MysqlSearch():
    def __init__(self):
        self.getConn()

    def getConn(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='mxonline',
                port=3306,
                charset='utf8',
            )
        except MySQLdb.Error as e:
            print 'Error: %s' % e

    def getOne(self):
        cursor = self.conn.cursor()
        sql = 'select * from courses_lesson where id = %s;'
        cursor.execute(sql, (6,))

        # rest = cursor.fetchall()
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchall()))
        print rest
        cursor.close()
        self.conn.close()

    def getAll(self):
        cursor = self.conn.cursor()
        sql = 'select * from courses_lesson;'
        cursor.execute(sql)
        # rest = cursor.fetchall()
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        print rest
        cursor.close()
        self.conn.close()

    def get_more(self, page, page_size):
        offset = (page - 1) * page_size
        cursor = self.conn.cursor()
        sql = "select * from 'news' where 'type' = %s order by 'created_at' desc limit %s, %s;"
        cursor.execute(sql, ('百家', offset, page_size))
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        print rest
        cursor.close()
        self.conn.close()

    def add_one(self):
        try:
            sql = (
                "insert into 'news' ('title', 'image', 'content', 'types', 'is_valid') value"
                "('til', 'img', %s, 'neitong', 'leixing', 'tiujian');"
            )
            cursor = self.conn.cursor()
            cursor.execute(sql, ('标题'))
            self.conn.commit()
            cursor.close()
            self.closeConn()
        except:
            print 'error'
            self.conn.rollback()




    def closeConn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print 'Error: %s' % e


def main():
    obj = MysqlSearch().getOne()


if __name__ == '__main__':
    main()
