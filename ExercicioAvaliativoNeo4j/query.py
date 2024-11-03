class TeacherDatabase:
    def __init__(self, database):
        self.db = database

    # Questão 01

    def get_teacher_by_name(self, name="Renzo"):
        # 1. Buscar professor com nome "Renzo" e retornar ano_nasc e CPF
        query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [{"ano_nasc": result["ano_nasc"], "cpf": result["cpf"]} for result in results]

    def get_teachers_starting_with_m(self):
        # 2. Buscar professores cujo nome comece com "M" e retornar name e cpf
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [{"name": result["name"], "cpf": result["cpf"]} for result in results]

    def get_all_cities(self):
        # 3. Buscar nomes de todas as cidades
        query = "MATCH (c:City) RETURN c.name AS city_name"
        results = self.db.execute_query(query)
        return [result["city_name"] for result in results]

    def get_schools_within_number_range(self, min_number=150, max_number=550):
        # 4. Buscar escolas com number entre 150 e 550, retornando nome, endereço e número
        query = """
        MATCH (s:School) 
        WHERE s.number >= $min_number AND s.number <= $max_number 
        RETURN s.name AS school_name, s.address AS address, s.number AS number
        """
        parameters = {"min_number": min_number, "max_number": max_number}
        results = self.db.execute_query(query, parameters)
        return [{"school_name": result["school_name"], "address": result["address"], "number": result["number"]} for result in results]

    # Questão 02

    def get_youngest_and_oldest_teacher_birth_year(self):
        # 1. Encontrar o ano de nascimento do professor mais jovem e do mais velho
        query = """
        MATCH (t:Teacher)
        RETURN min(t.ano_nasc) AS oldest_birth_year, max(t.ano_nasc) AS youngest_birth_year
        """
        results = self.db.execute_query(query)
        return results[0] if results else None

    def get_average_population(self):
        # 2. Encontrar a média aritmética para os habitantes de todas as cidades
        query = "MATCH (c:City) RETURN avg(c.population) AS average_population"
        results = self.db.execute_query(query)
        return results[0]["average_population"] if results else None

    def get_city_by_cep_with_replaced_a(self, cep="37540-000"):
        # 3. Encontrar cidade cujo CEP seja "37540-000" e retornar o nome com 'a' substituído por 'A'
        query = "MATCH (c:City {cep: $cep}) RETURN replace(c.name, 'a', 'A') AS modified_city_name"
        parameters = {"cep": cep}
        results = self.db.execute_query(query, parameters)
        return results[0]["modified_city_name"] if results else None

    def get_third_letter_of_teacher_names(self):
        # 4. Para todos os professores, retornar um caractere a partir da 3ª letra do nome
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS third_character"
        results = self.db.execute_query(query)
        return [result["third_character"] for result in results]
