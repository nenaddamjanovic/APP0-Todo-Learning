import FreeSimpleGUI as sg

themes = sg.theme_previewer()
themes_list = sg.theme_list()
for i, t in enumerate(themes_list):
    print(i, t)


# PySimpleGUI Documentation