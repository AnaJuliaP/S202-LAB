class Animal:
    def __init__(self, nome, especie, raca, idade, status, descricao, adotante=None):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.status = status
        self.descricao = descricao
        self.adotante = adotante

    def to_dict(self):
        return vars(self)
