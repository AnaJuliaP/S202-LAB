from database.models.Animal import Animal
from database.models.Adotante import Adotante
from database.models.Ong import Ong

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
    def __init__(self, animal_model, ong_model):
        super().__init__()
        self.animal_model = animal_model
        self.ong_model = ong_model
        self.add_command("create", self.create_animal)
        self.add_command("read", self.read_animal)
        self.add_command("update", self.update_animal)
        self.add_command("delete", self.delete_animal)
        self.add_command("create_ong", self.create_ong)
        self.add_command("read_ong", self.read_ong)
        self.add_command("update_ong", self.update_ong)
        self.add_command("delete_ong", self.delete_ong)
        self.add_command("add_animal_ong", self.add_animal_to_ong)

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

        self.animal_model.create(animal, adotante)

    def read_animal(self):
        id = input("Insira o ID: ")
        animal = self.animal_model.read_by_id(id)

    def update_animal(self):
        id = input("Insira o ID: ")
        novo_status = input("Insira o novo status: ")
        self.animal_model.update_animal(id, novo_status)

    def delete_animal(self):
        id = input("Insira o ID: ")
        self.animal_model.delete(id)

    def create_ong(self):
        print("INSIRA AS INFORMAÇÕES DA ONG:")
        nome = input("Entre com o nome da ONG: ")
        endereco = input("Entre com o endereço: ")
        telefone = input("Entre com o telefone: ")
        email = input("Entre com o email: ")
        animal_id = input("Entre com o ID do animal: ")

        # Buscar os dados do animal pelo ID
        animal = self.ong_model.read_by_id(animal_id)
        
        if animal:
            ong = Ong(nome, endereco, telefone, email, animais=[animal])
            self.ong_model.create(ong)
            print(f"Ong criada e associada ao animal com ID {animal_id}")
        else:
            print(f"Animal com ID {animal_id} não encontrado")

    def read_ong(self):
        id = input("Insira o ID: ")
        ong = self.ong_model.read_by_id(id)

    def update_ong(self):
        id = input("Insira o ID: ")
        novo_email = input("Insira o novo email: ")
        self.ong_model.update_ong(id, novo_email)

    def delete_ong(self):
        id = input("Insira o ID: ")
        self.ong_model.delete(id)

    def add_animal_to_ong(self):
        ong_id = input("Insira o ID da ONG: ")
        animal_id = input("Insira o ID do Animal: ")
        
        # Buscar os dados do animal pelo ID
        animal = self.ong_model.read_by_id(animal_id)
        
        if animal:
            self.ong_model.add_animal(ong_id, animal)
            print(f"Animal com ID {animal_id} adicionado à ONG com ID {ong_id}")
        else:
            print(f"Animal com ID {animal_id} não encontrado")
