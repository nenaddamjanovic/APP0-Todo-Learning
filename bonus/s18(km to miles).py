import FreeSimpleGUI as sg


def km_to_miles(local_km):
    return local_km / 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter kilometers", key="input_kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box],
                           [miles_button, output]],
                   font=('Calibri', 14))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["input_kms"])
            result = km_to_miles(km)
            window['output'].update(value=f"{km} kms is: {result} miles")
        case sg.WIN_CLOSED:
            break

window.close()