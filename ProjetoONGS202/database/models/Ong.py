class Ong:
    def __init__(self, nome, endereco, telefone, email, animais=None):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.animais = animais if animais is not None else []

    def add_animal(self, animal):
        self.animais.append(animal)

    def to_dict(self):
        return {
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "email": self.email,
            "animais": self.animais
        }