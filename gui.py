from functions import get_todos, write_todos
import FreeSimpleGUI as sg  # Možemo da skratimo ime modula

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter Todo", key="key_input_todo")
add_button = sg.Button("Add")  # Mora bit isto napisano kao u case
list_box = sg.Listbox(values=get_todos(), key="key_todos_listbox",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")  # Mora bit isto napisano kao u case
complete_button = sg.Button("Complete")  # Mora bit isto napisano kao u case
exit_button = sg.Button("Exit")  # Mora bit isto napisano kao u case
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(1, event)  # Šta je kliknuto, koji element gui
    print(2, values)  # vrednost svih elemenata windowa - rečnik
    print(3, values["key_todos_listbox"])
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["key_input_todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window["key_todos_listbox"].update(values=todos)

        case "Edit":
            todo_to_edit = values["key_todos_listbox"][0]
            new_todo = values["key_input_todo"]
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["key_todos_listbox"].update(values=todos)

        case "Complete":
            todo_to_complete = values["key_todos_listbox"][0]
            todos = get_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window["key_todos_listbox"].update(values=todos)
            window["key_input_todo"].update(value="")

        case "Exit":
            break  # Stopira samo while petlju u toku

        case "key_todos_listbox":
            window["key_input_todo"].update(value=values["key_todos_listbox"][0])

        case sg.WIN_CLOSED:
            break  # Stopira samo while petlju u toku
            # exit() Stopira ceo program odmah

window.close()
