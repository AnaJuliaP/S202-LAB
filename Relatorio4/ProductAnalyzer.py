from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database: Database):
        self._database = database

    def total_vendas_por_dia(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_venda", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        writeAJson(result, "Total de vendas por dia")
        return list(result)
    
    def produto_mais_vendido(self):
        result1 = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ])
        writeAJson(result1, "Produto mais vendido")
        return list(result1)
    
    def cliente_mais_gastou(self):
        result2 = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        writeAJson(result2, "Cliente que mais gastou")
        return list(result2)

    def produtos_vendidos_acima_de_1(self):
        result3 = list(self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_vendida": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade_vendida": {"$gt": 1}}},
            {"$sort": {"quantidade_vendida": -1}}
        ]))
        writeAJson(result3, "Produtos vendidos acima de 1")
        return list(result3)
