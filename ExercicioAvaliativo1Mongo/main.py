from database.database import Database
from cli import PersonCLI
from database.MotoristaDAO import MotoristaDAO

db = Database(database="CorridaApp", collection="Motoristas")
motoristaModel = MotoristaDAO(database=db)

personCLI = PersonCLI(motoristaModel)
personCLI.run()