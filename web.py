import streamlit as st
import functions


def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    if todo_local not in todos:
        todos.append(todo_local)
        functions.write_todos(todos)


todos = functions.get_todos()

st.title("My ToDo App")
st.subheader("This is a subheader")
st.write("This is a text ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)  # fshi indexin e ToDos qe behet check
        functions.write_todos(todos)  # rishkruaj listen e re
        del st.session_state[todo]  # fshije nga interface
        st.rerun()  # rerun script, pasi pa bere rerun elementi fshihet vetem duke i bere reload

st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
