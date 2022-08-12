import PySimpleGUI as sg
import sys
import pandas as pd
import os
from PyPDF2 import PdfFileReader


if len(sys.argv) == 1:
    window = sg.Window('Data 3000 S.A.S')
    fname = sg.FileBrowse("Contador de PDF's")
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancelado", "Ruta no ingresada")
    raise SystemExit("Cancelando: ruta no ingresada")
else:
    df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])

    dir_1= r'fname'
    print(fname)
    for root, dirs, files in os.walk(fname):
        for f in files:
            if f.endswith(".pdf"):
                pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
                df2 = pd.DataFrame([[f, os.path.join(root,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
                df = df.append(df2, ignore_index=True)
    sg.popup('La ruta que escogió es', fname, "Total de páginas en pdf: ", df['pageNumber'].sum())
    print(df.head)
    print("Total de páginas en pdf: ", df['pageNumber'].sum())