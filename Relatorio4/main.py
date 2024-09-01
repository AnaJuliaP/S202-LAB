from database import Database
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")

mercado = ProductAnalyzer(db)

mercado.total_vendas_por_dia()
mercado.produto_mais_vendido()
mercado.cliente_mais_gastou()
mercado.produtos_vendidos_acima_de_1()
db.resetDatabase()