import PySimpleGUI as sg
import ZIP_extractor_func

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("Select dest directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive extractor",
                   layout=[[col1, col2, col3],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    ArchivePath = values['archive']
    DirPath = values['folder']

    ZIP_extractor_func.extract_archive(ArchivePath,DirPath)
    window['output'].update(value="Extraction completed!")


window.close()
