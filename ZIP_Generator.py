import PySimpleGUI as sg
import ZIP_Creator as ZIP

#line 1
label1 = sg.Text("Select files to ZIP")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
#line 2
label2 = sg.Text("Select to where you want to ZIP")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key="folder")

compress_button = sg.Button("Compress")

label3 = sg.Text("", key="output")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("ZIP compressor",
                   layout=[[col1, col2, col3],
                           [compress_button,label3]],
                   element_justification="center")

while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]

    ZIP.make_archive(filepaths,folder)
    window["output"].update("File compressed sucessfully!")


window.read()
window.close()