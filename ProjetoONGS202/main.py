from database.database import Database
from cli import AnimalCLI
from database.OngDAO import OngDAO

db = Database(database="AdocaoDB", collection="Animais")
ong_model = OngDAO(database=db)

animal_cli = AnimalCLI(ong_model)
animal_cli.run()