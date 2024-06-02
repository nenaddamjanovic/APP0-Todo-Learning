import time
from functions import get_todos, write_todos
import FreeSimpleGUI as sg  # Možemo da skratimo ime modula

sg.theme("LightBrown1")

clock_label = sg.Text("", key="key_label_clock")
input_label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter Todo",
                         key="key_input_todo")
add_button = sg.Button("Add", size=12)
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
#    print(1, event)  # Šta je kliknuto, koji element gui
#    print(2, values)  # vrednost svih elemenata windowa - rečnik
#    print(3, values["key_todos_listbox"])
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["key_input_todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window["key_todos_listbox"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["key_todos_listbox"][0]
                new_todo = values["key_input_todo"]
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

        case "Exit":
            break  # Stopira samo while petlju u toku

        case "key_todos_listbox":
            window["key_input_todo"].update(value=values["key_todos_listbox"][0])

        case sg.WIN_CLOSED:
            break  # Stopira samo while petlju u toku
            # exit() Stopira ceo program odmah

window.close()
