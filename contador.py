import PySimpleGUI as sg
import pandas as pd
import os
#from PyPDF2 import PdfFileReader


sg.theme("LightGray2")
layout = [[sg.T("")], [sg.Text("Seleccionar una carpeta: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],[sg.Button("Contar")]]

###Building Window
window = sg.Window("Contador de páginas de PDF's | Data 3000 S.A.S v1.0", layout, size=(600,150))
    
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Contar":
        df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])
        dir_1= r'values["-IN-"]'
        print(values["-IN-"])
        for root, dirs, files in os.walk(values["-IN-"]):
            for f in files:
                if f.endswith(".pdf") or f.endswith(".PDF"):
                    pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
                    df2 = pd.DataFrame([[f, os.path.join(root,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
                    df = df.append(df2, ignore_index=True)
        sg.popup('La ruta que escogió es', values["-IN-"], "Total de páginas en pdf: ", df['pageNumber'].sum())
        print(df.head)
        print("Total de páginas en pdf: ", df['pageNumber'].sum())