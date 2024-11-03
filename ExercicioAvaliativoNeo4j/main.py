from database import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://44.200.162.216", "neo4j", "gram-afternoons-schoolroom")
# db.drop_all()

teacher_crud = TeacherCRUD(db)

# 2. Criar um Teacher com as características fornecidas
teacher_crud.create(name="Chris Lima", ano_nasc=1956, cpf="189.052.396-66")

# 3. Pesquisar o professor com o nome "Chris Lima"
teacher = teacher_crud.read(name="Chris Lima")
print("Teacher found:", teacher)

# 4. Alterar o CPF do Teacher "Chris Lima" para "162.052.777-77"
teacher_crud.update(name="Chris Lima", new_cpf="162.052.777-77")

db.close()
