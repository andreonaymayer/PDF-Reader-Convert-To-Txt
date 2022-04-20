def tipos():
    types = []
    types.append(Traducao('Æ', 'á'))
    types.append(Traducao("ª", 'ã'))
    types.append(Traducao("Œ", 'ê'))
    types.append(Traducao("Ø", 'é'))
    types.append(Traducao("˙", 'Ç'))
    types.append(Traducao("ˆ", 'Ã'))
    types.append(Traducao("ı", 'õ'))
    return types


def converte(textoCompleto):
    convertido = textoCompleto.replace("(cid:231)", "ç")
    convertido = convertido.replace("(cid:237)", "í")
    for tipo in tipos():
        convertido = convertido.replace(tipo.getAtual(), tipo.getNovo())

    return convertido


class Traducao:
    charAtual = b''
    charNovo = b''

    def __init__(self, atual, novo):
        self.charAtual = atual.encode()
        self.charNovo = novo.encode()

    def getAtual(self):
        return self.charAtual.decode()

    def getNovo(self):
        return self.charNovo.decode()

    def string(self):
        return self.charAtual.decode() + " : " + self.charNovo.decode()
