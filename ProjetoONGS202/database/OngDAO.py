from pymongo import MongoClient
from bson.objectid import ObjectId
from database.models.Animal import Animal
from database.models.Adotante import Adotante

class OngDAO:
    def __init__(self, database):
        self.db = database
        
    def create(self, animal: Animal, adotante: Adotante):
        try:
            animal_doc = {
                "nome": animal.nome,
                "especie": animal.especie,
                "raca": animal.raca,
                "idade": animal.idade,
                "status": animal.status,
                "descricao": animal.descricao,
                "adotante": {
                    "nome": adotante.nome,
                    "documento": adotante.documento
                }
            }
            
            animal_res = self.db.collection.insert_one(animal_doc)
            animal_id = animal_res.inserted_id
            
            print(f"Animal created with id: {animal_id}")
            
            return animal_id
        except Exception as e:
            print(f"An error occurred while creating records: {e}")
            return None
        
    def read_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Animal found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None
        
    def update_animal(self, id: str, novo_status: str):
        try:
            # Atualize o status do animal no banco de dados
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"status": novo_status}}
            )
            
            if res.modified_count > 0:
                return res.modified_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred while updating animal: {e}")
            return None
        
    def delete(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Animal deleted: {res.deleted_count}")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting animal: {e}")
            return None