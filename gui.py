from functions import get_todos, write_todos
import FreeSimpleGUI as sg  #Možemo da skratimo ime modula

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
