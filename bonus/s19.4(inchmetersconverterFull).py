import FreeSimpleGUI as sg
from Fconvertfeetinches import convert

sg.theme("Black")

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="input_feet")
label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="input_inches")
convert_button = sg.Button("Convert")
convert_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                   [label2, input2],
                   [convert_button, convert_label],
                   [exit_button]],
                   font=("Calibri", 15)
                   )

while True:
    event, values = window.Read()

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    try:
        feet = float(values["input_feet"])
        inches = float(values["input_inches"])
        result = convert(feet, inches)
        window["output"].update(value=f"{result} meters", text_color="red")
    except ValueError:
        sg.popup("Please write numbers first",
                 font=("Calibri", 15))

window.Close()