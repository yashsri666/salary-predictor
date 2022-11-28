import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

chart = alt.Chart(data).mark_circle().encode(
    x='a', y='b', tooltip=['a', 'b']
    )
st.altair_chart(chart)

st.map(city)

st.graphviz_chart("""
digraph {
    run -> intr
    intr -> runbl
    runbl -> run
    run -> kernel
    kernel -> zombie
    kernel -> sleep
    }
    """)

plt.scatter(data['a'], data['b'])
plt.title("Scatter Plot")
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)