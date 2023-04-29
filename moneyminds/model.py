class Carteira():
    """
    Classe que representa a carteira do usuário
    """
    def __init__(self, valor: float, categoria: str, data: str, descricao: str):
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.descricao = descricao
        
        
    def __str__(self):
        return f'Valor: {self.valor}, Categoria: {self.categoria}, Data: {self.data}, Descrição: {self.descricao}'