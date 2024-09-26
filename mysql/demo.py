import pymysql
import pandas as pd
from pprint import pprint
#conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='db')

class DB():
    def __init__(self) -> None:
        pass
    sql="""
    select * from users;
    """
    def get_conn(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='db')    

        return conn

    def query_sql(self,conn,sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def insert_sql(self,conn,sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    def close_conn(self,conn):
        conn.close()

if __name__ == '__main__':
    db=DB()
    conn=db.get_conn()
    # result = query_sql(conn,"select * from users;")
    # pprint(result)
    # sql="insert into users(user_name,user_pwd) values('haha',25);"
    # db.insert_sql(conn,sql)
    res=db.query_sql(conn,"select * from users;")
    res=db.query_sql(conn,"select count(1) from users where user_name='haha' and user_pwd='25';")
    print(len(res))
    pprint(res)