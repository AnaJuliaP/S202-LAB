class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (:Player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id, player1_id, player2_id, result):
        query = """
        MATCH (p1:Player {id: $player1_id}), (p2:Player {id: $player2_id})
        CREATE (:Match {id: $match_id, result: $result})<-[:PLAYED]-(p1), (:Match {id: $match_id, result: $result})<-[:PLAYED]-(p2)
        """
        parameters = {"match_id": match_id, "player1_id": player1_id, "player2_id": player2_id, "result": result}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_match_result(self, match_id, new_result):
        query = "MATCH (m:Match {id: $match_id}) SET m.result = $new_result"
        parameters = {"match_id": match_id, "new_result": new_result}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    def get_match(self, match_id):
        query = """
        MATCH (m:Match {id: $match_id})<-[:PLAYED]-(p:Player)
        RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players
        """
        parameters = {"match_id": match_id}
        results = self.db.execute_query(query, parameters)
        return results[0] if results else None

    def get_player_match_history(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[:PLAYED]->(m:Match)
        RETURN m.id AS match_id, m.result AS result
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"match_id": result["match_id"], "result": result["result"]} for result in results]

    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)
