from database.models.Animal import Animal
from database.models.Adotante import Adotante

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")  
                
class AnimalCLI(SimpleCLI):
    def __init__(self, ong_model):
        super().__init__()
        self.ong_model = ong_model
        self.add_command("create", self.create_animal)
        self.add_command("read", self.read_animal)
        self.add_command("update", self.update_animal)
        self.add_command("delete", self.delete_animal)
        
    def create_animal(self):
        print("INSIRA AS INFORMAÇÕES DO ANIMAL:")
        nome_animal = input("Entre com nome do animal: ")
        especie = input("Entre com a especie: ")
        raca = input("Entre com a raça: ")
        idade = input("Entre com a idade: ")
        status = input("Entre com o status: ")
        descricao = input("Entre com a descrição: ")
        animal = Animal(nome_animal, especie, raca, idade, status, descricao)
        
        print("INSIRA AS INFORMAÇÕES DO ADOTANTE: ")
        nome_adotante = input("Entre com o nome do adotante: ")
        doc = input("Entre o numero do documento: ")
        adotante = Adotante(nome_adotante, doc)
        
        self.ong_model.create(animal, adotante)
        
    def read_animal(self):
        id = input("Insira o ID: ")
        animal = self.ong_model.read_by_id(id)
        
    def update_animal(self):
        id = input("Insira o ID: ")
        novo_status = input("Insira o novo status: ")
        self.ong_model.update_animal(id, novo_status)
        
    def delete_animal(self):
        id = input("Insira o ID: ")
        self.ong_model.delete(id)