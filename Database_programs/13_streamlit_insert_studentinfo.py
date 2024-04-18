import streamlit as st

st.info("Student registration")

f_name=st.text_input('f_name')
l_name=st.text_input('l_name')
email=st.text_input('email')
gender=st.text_input('gender')
age=st.number_input('age')
bday=st.text_input('bday')
address=st.text_input('address')


def add():
    import mysql.connector
    #creat the connection object
    myconn=mysql.connector.connect(host="localhost",user="root",password="",database="college")
    #creating the cursor object
    cur=myconn.cursor()

    sql="insert into studentinfo(f_name,l_name,email,gender,age,bday,address)values(%s,%s,%s,%s,%s,%s,%s)"
    val=(f_name,l_name,email,gender,age,bday,address)

    try:

        # inserting the values into the table
        cur.execute(sql, val)
        myconn.commit()  # commit the transaction
        print("data inserted")

    except Exception as e:
        print("can not process:", e)
        myconn.rollback()

    print(cur.rowcount, "record inserted!")
    st.success("Registration Success")
    myconn.close()

def set_state(i):
    st.session_state.stage = i
    st.write("i value is:",i)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    st.button('INSERT', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    add()



