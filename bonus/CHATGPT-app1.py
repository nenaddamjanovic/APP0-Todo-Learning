import time
import FreeSimpleGUI as sg
import os

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightBrown1")

clock_label = sg.Text("", key="key_label_clock")
input_label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter Todo",
                         key="key_input_todo")
add_button = sg.Button("Add", size=15)
list_box = sg.Listbox(values=get_todos(),
                      key="key_todos_listbox",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock_label],
                           [input_label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=500)
    window["key_label_clock"].update(value=time.strftime("%H:%M:%S"))

    match event:
        case sg.WIN_CLOSED:
            break

        case "Exit":
            break

        case "Add":
            todos = get_todos()
            new_todo = values["key_input_todo"].strip() + "\n"
            if new_todo.strip():  # Check if the todos is not empty
                todos.append(new_todo)
                write_todos(todos)
                window["key_todos_listbox"].update(values=todos)
            else:
                sg.popup("Please enter a todo item", font=("Calibri", 15))
            window["key_input_todo"].update("")

        case "Edit":
            try:
                todo_to_edit = values["key_todos_listbox"][0]
                new_todo = values["key_input_todo"].strip() + "\n"
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window["key_todos_listbox"].update(values=todos)
            except IndexError:
                sg.popup("Please select item in list first",
                         font=("Calibri", 15))

        case "Complete":
            try:
                todo_to_complete = values["key_todos_listbox"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["key_todos_listbox"].update(values=todos)
                window["key_input_todo"].update(value="")
            except IndexError:
                sg.popup("Please select item in list first",
                         font=("Calibri", 15))

        case "key_todos_listbox":
            window["key_input_todo"].update(value=values["key_todos_listbox"][0])

window.close()