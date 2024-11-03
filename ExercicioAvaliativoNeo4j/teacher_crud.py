class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' created successfully.")

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result[0] if result else None

    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' updated with new CPF '{new_cpf}'.")

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' deleted successfully.")
