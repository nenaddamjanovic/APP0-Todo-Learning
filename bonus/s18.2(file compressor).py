import FreeSimpleGUI as sg
from Fzip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(key="input_src_files")
choose_button1 = sg.FilesBrowse("Choose", key="button_filepath")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(key="input_dst_folder")
choose_button2 = sg.FolderBrowse("Choose", key="button_folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="red")

window = sg.Window("File compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["button_filepath"].split(";")
    folder = values["button_folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="compression completed")


window.close()

# -------------------------------------------------------------------------------

# Compress {'input_src_files': 'C:/Users/Nenad/PycharmProjects/APP1/bonus/forziptest1.txt',
#          'button_filepath': 'C:/Users/Nenad/PycharmProjects/APP1/bonus/forziptest1.txt',
#          'input_dst_folder': 'C:/Users/Nenad/PycharmProjects/APP1/bonus/dest',
#          'button_folder': 'C:/Users/Nenad/PycharmProjects/APP1/bonus/dest'}

# Compress {0: 'C:/Users/Nenad/PycharmProjects/APP1/bonus/questions.json',
#          'Choose': 'C:/Users/Nenad/PycharmProjects/APP1/bonus/questions.json',
#          1: 'C:/Users/Nenad/PycharmProjects/APP1/bonus/files',
#          'Choose0': 'C:/Users/Nenad/PycharmProjects/APP1/bonus/files'}


