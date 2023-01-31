import PySimpleGUI as sg

#line 1
label1 = sg.Text("Select files to ZIP")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")
#line 2
label2 = sg.Text("Select to where you want to ZIP")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("ZIP compressor", layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[compress_button]], element_justification="center")
window.read()
window.close()