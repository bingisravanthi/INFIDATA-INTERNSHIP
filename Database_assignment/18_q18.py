import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",password="",database="company")

cur=myconn.cursor()

try:
    cur.execute("select * from staff order by salary DESC")
    result=cur.fetchall()
    for i in result:
        print(i)


except Exception as e:
    print("can not process:",e)