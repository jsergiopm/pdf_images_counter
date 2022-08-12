import pandas as pd
import os
from PyPDF2 import PdfFileReader

def run():
    df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])

    dir_1= r'..'

    for root, dirs, files in os.walk(dir_1):
        for f in files:
            if f.endswith(".pdf"):
                pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
                df2 = pd.DataFrame([[f, os.path.join(root,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
                df = df.append(df2, ignore_index=True)
    print(df.head)
    print("Total de páginas en pdf: ", df['pageNumber'].sum())

if __name__ == "__main__":
    run()