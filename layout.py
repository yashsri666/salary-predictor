import streamlit as st

st.title("Registration Form")

first, last = st.columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email, mobile = st.columns([3, 1])

email.text_input("Email")
mobile.text_input("Mobile")

username, pass1, pass2 = st.columns(3)

username.text_input("Username")
pass1.text_input("Password", type="password")
pass2.text_input("Confirm Password", type="password")

st.checkbox("I agree to the terms and conditions")
st.button("Submit")

