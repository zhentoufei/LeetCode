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
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        print rest
        cursor.close()
        self.conn.close()


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