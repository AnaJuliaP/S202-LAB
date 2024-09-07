from database import Database
from writeAJson import writeAJson
from livroModel import LivroModel
from cli import LivroCLI

db = Database(database="relatorio_05", collection="livros")
livroModel = LivroModel(database=db)

#create
# livroModel.create_livro("Extraordinario", "R. J. Palacio", 2012, 44.95)

#read
# livroModel.read_livro_by_id("66dc978e369db86dc7423758")

#update
# livroModel.update_livro("66dc978e369db86dc7423758", "Entendendo algoritmos", "Aditya Y. Bhargava", 2017, 58.50)

#delete
# livroModel.delete_livro("66dc9987be9e154187c8676c")

livroCLI = LivroCLI(livroModel)
livroCLI.run()