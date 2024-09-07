class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class LivroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        titulo = input("Enter the title: ")
        autor = input("Enter the author: ")
        ano = int(input("Enter the year: "))
        preco = float(input("Enter the price: "))
        self.livro_model.create_livro(titulo, autor, ano, preco)

    def read_livro(self):
        _id = input("Enter the ID: ")
        livro = self.livro_model.read_livro_by_id(_id)
        if livro:
            print(f"Title: {livro['titulo']}")
            print(f"Author: {livro['autor']}")
            print(f"Year: {livro['ano']}")
            print(f"Price: {livro['preco']}")

    def update_livro(self):
        _id = input("Enter the ID: ")
        titulo = input("Enter the new title: ")
        autor = input("Enter the new author: ")
        ano = int(input("Enter the new year: "))
        preco = float(input("Enter the new price: "))
        self.livro_model.update_livro(_id, titulo, autor, ano, preco)

    def delete_livro(self):
        _id = input("Enter the ID: ")
        self.livro_model.delete_livro(_id)

    def run(self):
        print("Welcome to the book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()