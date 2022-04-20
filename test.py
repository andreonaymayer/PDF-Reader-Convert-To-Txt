# import charade
# import pdfplumber
# from pip._internal.utils import encoding
#
# from Traducao import Traducao
# types = []
# types.append(Traducao('Æ','á'))
# types.append(Traducao("ª",'ã'))
# types.append(Traducao("Œ",'ê'))
# types.append(Traducao("Ø",'é'))
# types.append(Traducao("˙",'Ç'))
# types.append(Traducao("ˆ",'Ã'))
# types.append(Traducao("ı",'õ'))
# types.append(Traducao("œ",'ú'))
#
# funciona = 'Funciona/Extrato Mensal 01.2021_Oiapok.pdf'
# nfunciona = 'NFunciona/Extrato Mensal 02.2019_Oiapok.pdf'
#
# pdf = pdfplumber.open(r'/Users/andreonaymayer/Python/' + nfunciona)
# str = pdf.pages[0].extract_text()
# new = str.replace("(cid:231)","ç")
# new = new.replace("(cid:237)","í")
#
# print(new)
