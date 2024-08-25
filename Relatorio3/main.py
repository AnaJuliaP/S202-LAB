from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")

poke = Pokedex(db)

poke.list_pokemon()
poke.create_pokemon()
poke.delete_pokemon()
poke.show_one_pokemon()
poke.count_all_pokemon()
db.resetDatabase()