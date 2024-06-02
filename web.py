import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

st.title("my todo app")
st.subheader("This is my todo app :)")
st.write("You increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo...")