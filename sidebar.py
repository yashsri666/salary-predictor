import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

rad = st.sidebar.radio("Navigation", ("Home", "About Us", "Contact"))

if rad == "Home":
    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a column", df.columns)

    plt.plot(df["num"], df[col])

    st.pyplot()
if rad == "About Us":
    st.error("This is an error")
    st.warning("This is a warning")
    st.success("This is a success")
    st.info("This is an info")
    st.exception(RuntimeError("This is an exception"))