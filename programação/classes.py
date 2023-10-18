
class Perfil:
    def __init__(self, imagem, nome, descricao, dono):
        self.imagem = imagem
        self.nome = nome
        self.descricao = descricao
        self.dono = dono

class Perfis:
    def __init__(self):
        self.perfis = []

    def adicionar(self, perfil):
        self.perfis.append(perfil)
