import FreeSimpleGUI as sg
from Fextractor import extract_archive

#  može da extraktuje samo .zip

sg.theme("Black")

label1 = sg.Text("Select archive to extract:")
input1 = sg.Input(key="input_src_archive")
choose_button1 = sg.FileBrowse("Choose", key="button_archive")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(key="input_dst_folder")
choose_button2 = sg.FolderBrowse("Choose", key="button_folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="white")

window = sg.Window("File extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["input_src_archive"]
    dest_dir = values["input_dst_folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction completed")

window.close()
