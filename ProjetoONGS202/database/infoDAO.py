from pymongo import MongoClient
from bson.objectid import ObjectId
from database.models.Ong import Ong
from database.models.Animal import Animal

class infoDAO:
    def __init__(self, database):
        self.db = database

    def create(self, ong: Ong):
        try:
            ong_doc = ong.to_dict()
            ong_res = self.db.collection.insert_one(ong_doc)
            ong_id = ong_res.inserted_id

            print(f"Ong created with id: {ong_id}")

            return ong_id
        except Exception as e:
            print(f"An error occurred while creating records: {e}")
            return None

    def read_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Ong found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    def update_ong(self, id: str, novo_email: str):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"email": novo_email}}
            )

            if res.modified_count > 0:
                return res.modified_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred while updating ong: {e}")
            return None

    def delete(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            if res.deleted_count > 0:
                return res.deleted_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred while deleting ong: {e}")
            return None

    def add_animal(self, ong_id: str, animal_id: str):
        try:
            # Buscar os dados do animal pelo ID
            animal = self.db.collection.find_one({"_id": ObjectId(animal_id)})
            if not animal:
                print("Animal não encontrado")
                return None

            # Adicionar o animal à ONG
            res = self.db.collection.update_one(
                {"_id": ObjectId(ong_id)},
                {"$push": {"animais": animal}}
            )

            if res.modified_count > 0:
                return res.modified_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred while adding animal: {e}")
            return None