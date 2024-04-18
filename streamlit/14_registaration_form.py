import streamlit as st
import datetime

st.title('Registration Form')

my_form=st.form(key='form-1')

fname=my_form.text_input('First Name:')
lname=my_form.text_input('Last Name:')
email=my_form.text_input('Email:')
mobile=my_form.text_input('Mobile:')

gender=my_form.radio('Gender',('Male','Female'))


DateOfBirth=my_form.date_input('DateOfBirth:',min_value=datetime.date(1980,1,1))

address=my_form.text_area('Address:')
city=my_form.text_input('City:')
areapin=my_form.text_input('Area PIN:')
state=my_form.text_input('State:')

qualification=my_form.selectbox('Qualification', [None,'B.sc','B.tech','M.sc','B.com','BZC'])

specialization=my_form.radio('Specialization',('Computer science','Information technology','Computer architecture','Tele communication'))
password=my_form.text_input('Password:')
submit=my_form.form_submit_button('Register')