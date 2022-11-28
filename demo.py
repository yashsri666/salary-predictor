import streamlit as st

st.title("Hello World")

st.header("This is a header")

st.subheader("This is a subheader")

st.text("This is a text")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag
**bold text**
_italic text_
:moon: </br>
:sun_with_face: :earth_americas:""", True)

st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.write(st)