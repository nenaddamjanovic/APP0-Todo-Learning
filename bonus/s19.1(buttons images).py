import FreeSimpleGUI as sg

sg.theme("Black")

add_button = sg.Button(size=20,
                       image_source="files/add.png",
                       mouseover_colors="green",
                       tooltip="type in for add")
complete_button = sg.Button(size=20,
                            image_source="files/complete.png",
                            mouseover_colors="brown",
                            tooltip="press to complete")
# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')],
                       [add_button]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')],
                        [complete_button]]

# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()