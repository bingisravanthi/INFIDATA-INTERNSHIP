import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",password="",database="company")

cur=myconn.cursor()

try:
    cur.execute("select upper(f_name)from staff")
    result=cur.fetchall()
    for i in result:
        print(i)


except Exception as e:
    print("can not process:",e)
