import os
import timeit

import pdfplumber

from Traducao import converte

pasta = "Funciona/"
encoder = "utf-8"

diretorio = os.listdir(r'/Users/andreonaymayer/Python/' + pasta)
inicio = timeit.default_timer()
for arquivo in diretorio:
    if "pdf" in arquivo:
        print(arquivo)
        outfile = open(r'/Users/andreonaymayer/Python/Saida/saida.txt', 'w', encoding=encoder)
        pdf = pdfplumber.open(r'/Users/andreonaymayer/Python/' + pasta + arquivo)

        for page in pdf.pages:
            outfile.write(converte(page.extract_text()))

        outfile.close()

fim = timeit.default_timer()
print('duracao: %f' % (fim - inicio))
