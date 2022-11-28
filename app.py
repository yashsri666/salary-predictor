import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np


st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv("data\\Salary_Data.csv")
x = np.array(data["YearsExperience"]).reshape(-1, 1)

st.title("Salary Predictor")

lr = LinearRegression()
lr.fit(x, np.array(data["Salary"]))


nav = st.sidebar.radio("Go to page", ["Home", "Predictor", "Contribute with data"])

if nav == "Home":
    st.image("data\\sal.jpg", width=800)
    if st.checkbox("Show data"):
        st.table(data)

    graph = st.selectbox("What kind of graph do you wish to see?", ["Interactive", "Static"])

    val = st.slider("Filter data by number of years of experience", min_value=0, max_value=20, value=1)
    data = data[data["YearsExperience"] >= val]

    if graph == "Static":
        plt.figure(figsize=(10, 5))
        plt.scatter(data["YearsExperience"], data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.title("Salary vs Experience")
        plt.tight_layout()
        st.pyplot()
    if graph == "Interactive":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode="markers"))
        fig.update_layout(title="Salary vs Experience", xaxis_title="Years of Experience", yaxis_title="Salary")
        st.plotly_chart(fig)


if nav == "Predictor":
    st.header("Know your salary")
    val = st.number_input("Enter your years of experience", min_value=0.0, max_value=20.0, step = 0.50)
    val = np.array(val).reshape(1, -1)
    pred = lr.predict(val)

    if st.button("Predict"):
        st.success(f"Your predicted salary is {(pred)}")
if nav == "Contribute with data":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your Experience",0.0,20.0)
    sal = st.number_input("Enter your Salary",0.00,1000000.00,step = 1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//Salary_Data.csv",mode='a',header = False,index= False)
        st.success("Submitted")


