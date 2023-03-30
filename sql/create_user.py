import pymysql
import sqlmsg
# 資料庫連線資訊
#db_settings={host,user,passwd,db,port,charset}
#conn = pymysql.connect(host,user,passwd,db,port,charset)
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
def readid():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "SELECT id FROM `USER_NAME`ORDER BY `id` DESC"
        cursor.execute(command)
        try:
            data= cursor.fetchone()
            print("oldid:"+data[0])
            id=int(data[0])+1
        except:
            id=1
            print("no oldid!!")

    #id="0002"
    return str(id).zfill(5)

def chackuser(name):
    ##確定名稱是否重複
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "SELECT * FROM `USER_NAME`ORDER BY `id` DESC"
        cursor.execute(command)
        try:
            for data in cursor:
                #print("迴圈數"+str(n))

                #print("name="+name+" data="+data[0])
                #print(data[0])
                if name == data[0] or name==data[1]:

                    print("名子重複!!")
                    return "WORRING!!"
            return "ok"
                    
        except:
            id=1
            print("error!")

def saveuser(NAME,id):
    ##儲存NAME,ID
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "INSERT INTO USER_NAME(name,id)VALUES(%s,%s)"

        data=(NAME,id)
        cursor.execute(command, data)
                
            # 儲存變更
        conn.commit()


def create():
    
    print("建立使用者")
    name=input("請輸入人名")
    id="0000"
    id=readid()
    chack=chackuser(name)
    while chack=="WORRING!!":
        name=input("此名稱已占用!!請重新輸入!! :")
        chack=chackuser(name)
        
    #print("chack:"+chack)
    if chack=="WORRING!!":
        err="WORRING!!"
        #print("dasdas")
        return(err,id)
    saveuser(name,id)
    print("名為"+name+"的使用者建立完畢，ID為:"+str(id))

    return(name,id)
