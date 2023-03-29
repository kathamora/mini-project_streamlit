import streamlit as st
import functions
todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    if todo_local not in todos:  # Add this if-condition to fix the issue
        todos.append(todo_local)
        functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my to-do app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index+1)
    if checkbox: #is checked
        #remove selected to-do
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index+1]
        st.experimental_rerun()

st.text_input(label="Enter a to-do", placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')
# st.session_state #contain widgets information, checkboxes has no key yet so that is why it is not showing up in the session state
# #to

