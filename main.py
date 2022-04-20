# import os
# import charade
# import pdfplumber
#
# pasta = "NFunciona/"
# encoder = "latin-1"
#
# diretorio = os.listdir(r'/Users/andreonaymayer/Python/' + pasta)
# print(diretorio)
#
#
# for arquivo in diretorio:
#     if "pdf" in arquivo:
#         print(arquivo)
#         outfile = open(r'/Users/andreonaymayer/Python/Saida/saidaN.txt', 'w', encoding="utf-8")
#         pdf = pdfplumber.open(r'/Users/andreonaymayer/Python/' + pasta + arquivo)
#
#         for page in pdf.pages:
#             print(
#                 "===============================================================================: ---" + page.__str__().__str__())
#             table = page.extract_text()
#             print(table)
#             outfile.write(table)
#         outfile.close()
#
#