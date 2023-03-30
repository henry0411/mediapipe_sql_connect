import pymysql
import sqlmsg
# 資料庫連線資訊
#db_settings={host,user,passwd,db,port,charset}
#conn = pymysql.connect(host,user,passwd,db,port,charset)

def save(NAME,time,count,cal):
    dbhost,dbuser,dbpasswd,dbdb=sqlmsg.msg()
    # 建立Connection物件
    db_settings = {
        "host": dbhost,
        "port": 3306,
        "user": dbuser,
        "password": dbpasswd,
        "db": dbdb,
        "charset": "utf8"
        }
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "INSERT INTO data(NAME,time,count,cal)VALUES(%s,%s, %s,%s)"

        data=(NAME,time,count,cal)
        cursor.execute(
                command, data)
                
            # 儲存變更
        conn.commit()
