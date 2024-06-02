import FreeSimpleGUI as sg
from Fconvertfeetinches import convert

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="input_feet")
label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="input_inches")
convert_button = sg.Button("convert")
convert_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                   [label2, input2],
                   [convert_button, convert_label]],
                   font=("Calibri", 15)
                   )

while True:
    event, values = window.Read()
    feet = float(values["input_feet"])
    inches = float(values["input_inches"])
    result = convert(feet, inches)
    window["output"].update(value=f"{result} meters", text_color="red")

window.Close()