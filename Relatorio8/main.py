from database import Database
from game_database import GameDatabase

db = Database("bolt://34.200.238.93:7687", "neo4j", "nation-blasts-method")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("1", "Julia")
game_db.create_player("2", "Carlos")
game_db.create_player("3", "Beatriz")

game_db.create_match("101", "1", "2", "Julia 2 - Carlos 1")
game_db.create_match("102", "2", "3", "Carlos 3 - Beatriz 2")
game_db.create_match("103", "1", "3", "Beatriz 2 - Julia 1")

game_db.update_player("1", "Juliana")

game_db.update_match_result("101", "Juliana 3 - Carlos 1")

game_db.delete_player("3")
game_db.delete_match("102")

print("Jogadores:")
print(game_db.get_players())

print("Partida 101:")
print(game_db.get_match("101"))

print("Histórico de partidas do jogador 2 (Carlos):")
print(game_db.get_player_match_history("2"))

db.close()
