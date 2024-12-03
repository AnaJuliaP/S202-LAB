from database.database import Database
from cli import AnimalCLI
from database.OngDAO import OngDAO
from database.infoDAO import infoDAO

db = Database(database="AdocaoDB", collection="Animais")
animal_model = OngDAO(database=db)
ong_model = infoDAO(database=db)


animal_cli = AnimalCLI(animal_model, ong_model)
animal_cli.run()
