import pymysql

from until.getMesInfo import MesData

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = '123456'
    db = '111'

    conn = pymysql.Connect(host=host, port=port, user=user,
                           passwd=passwd, db=db)
    db_main = MesData(conn)

    sql = "select * from project"
    a = db_main.db_rw(sql)
    print(a)
