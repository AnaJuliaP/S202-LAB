from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self._database = database

    def list_pokemon(self):
        resultList = list(self._database.collection.find({}))
        print(resultList)
        writeAJson(resultList, "list_pokemon_log")

    def create_pokemon(self):
        pokemon_data = {
            "id": 1,
            "num": "001",
            "name": "Bulbasaurr",
            "img": "http://www.serebii.net/pokemongo/pokemon/001.png",
            "type": ["Grass", "Poison"],
            "height": "0.71 m",
            "weight": "6.9 kg",
            "candy": "Bulbasaur Candy",
            "candy_count": 25,
            "egg": "2 km",
            "spawn_chance": 0.69,
            "avg_spawns": 69,
            "spawn_time": "20:00"
        }
        self._database.collection.insert_one(pokemon_data)
        print("Pokemon created: ", pokemon_data)
        writeAJson(pokemon_data, "create_pokemon_log")
        
    def delete_pokemon(self):
        resultDelete = self._database.collection.delete_one({'name' : 'Bulbasaurr'})
        print(resultDelete)
        delete_log = {
        "deleted_count": resultDelete.deleted_count,
        "acknowledged": resultDelete.acknowledged
        }
        writeAJson(delete_log, "delete_pokemon_log")
        
    def show_one_pokemon(self):
        resultShow = self._database.collection.find_one({'name': 'Ivysaur'})
        print(resultShow)
        writeAJson(resultShow, "show_one_pokemon_log")
        
    def count_all_pokemon(self):
        resultCount = self._database.collection.estimated_document_count()
        print(resultCount)
        writeAJson(resultCount, "count_all_pokemon_log")
