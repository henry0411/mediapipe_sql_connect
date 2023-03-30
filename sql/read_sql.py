#name 
#count 
#calories
import os,sys
import pymysql
import sqlmsg
import create_user
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
def read_data(name):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command="SELECT * FROM data WHERE name ='"+name+"'ORDER BY date DESC"
        cursor.execute(command)
        try:
            for data in cursor.fetchmany():
                #0=name 1=date 2=time 3=count 4=cal
                print("data[0]")###############################################################################
                return data[0],data[3],data[4]
            return name,"0","0"
                    
        except:
            id=1
            print("error!")
        
    
def read_nameid(name):
    
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        Name=""
        command = "SELECT * FROM `USER_NAME`ORDER BY `id` DESC"
        cursor.execute(command)

        for data in cursor.fetchall():
            #print("name="+name+" dataname="+data[0]+" dataid="+data[1])
            if name == data[0] or name==data[1]:
                Name=data[0]      
                print("有人!!")
                #print("一次印出全部內容 : ", data)
                conn.commit()
                cursor.close()
                name,count,cal=read_data(Name)
                return name,count,cal

        ans=input("沒人，請問是否要建立使用者?(Y/N)")
        #print(ans)
        i=0
        while i==0:
            if ans=="Y" or ans=="YES" or ans=="y" or ans=="yes":                            
                i=1      
                name,id=create_user.create()
                conn.commit()
                cursor.close()
                    
                return name,0,0
            elif ans=="N" or ans=="NO" or ans=="n" or ans=="no":
                i=1
                    
            if i==0:
                ans=input("請重新輸入:")
                            
        
    
        