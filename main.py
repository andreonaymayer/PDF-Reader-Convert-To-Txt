import os

import pdfplumber

pasta = "Funciona/"
try:
    diretorio = os.listdir(r'/Users/andreonaymayer/Python/' + pasta)
    print(diretorio)

    for arquivo in diretorio:
        if "pdf" in arquivo:
            print(arquivo)
            outfile = open(r'/Users/andreonaymayer/Python/Saida/saidaN.txt', 'w', encoding="latin-1")
            pdf = pdfplumber.open(r'/Users/andreonaymayer/Python/' + pasta + arquivo)

            for page in pdf.pages:
                print(
                    "===============================================================================: ---" + page.__str__().__str__())
                table = page.extract_text()
                print(table)
                outfile.write(table)
            outfile.close()
except:
    print('Erro na conversão')
