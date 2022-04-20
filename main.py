import pdfplumber
import os
import shutil
import sys
try:
    caminhos = os.listdir(r'C:\Users\Eduardo\Downloads\PDFs')
    print(caminhos)
    for nome in caminhos:
        print(nome)
        outfile = open(r'C:\Users\Eduardo\Downloads\teste.txt','w')
        pdf = pdfplumber.open(r'C:\Users\Eduardo\Downloads\PDFs\\'+nome)
        for page in pdf.pages:
            print(page)
            table = page.extract_text()
            #print(table)
            # for row in table[0:]:
            #     outcsv.writerow(row)
            outfile.write(table)
            print("Escrevi")
    outfile.close()
except:
    print('Erro na conversão')