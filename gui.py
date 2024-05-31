from functions import get_todos, write_todos
import FreeSimpleGUI as sg  #Možemo da skratimo ime modula

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
