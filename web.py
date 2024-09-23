import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
  if st.session_state["new_todo"] != '':
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase my productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')

print("hello")


