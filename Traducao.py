class Traducao:
    charAtual = b''
    charNovo = b''

    def __init__(self, atual, novo):
        self.charAtual = atual.encode()
        self.charNovo = novo.encode()

    def getAtual(self):
        return self.charAtual

    def getNovo(self):
        return self.charNovo

    def string (self):
        return self.charAtual.decode() + " : " + self.charNovo.decode()