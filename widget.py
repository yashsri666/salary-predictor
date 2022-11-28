import streamlit as st

st.title("WIDGETS")

if st.button("Say hello"):
    st.write("Hello there")

name = st.text_input("Your name" )
if st.button("Submit"):
    st.write("Hello", name)

address = st.text_area("Your address")
if st.button("Submit "):
    st.write("Your address is", address)

st.date_input("Date")

st.time_input("Time")

st.checkbox("Check to accept the terms and condotions", value=False)

b1 = st.radio("Select Color", ("Red", "Green", "Blue"), index=0)

b2 = st.selectbox("Select Color", ("Red", "Green", "Blue"), index=1)
st.write(b1, b2)

b3 = st.multiselect("Select Color", ("Red", "Green", "Blue"), default=("Red", "Green"))
st.write(b3)

b4 = st.slider("Select your age", min_value=18, max_value=60, value=22)
st.write(b4)

st.number_input("Enter a number", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

st.file_uploader("Upload a file")