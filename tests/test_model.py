from moneyminds.model import Carteira


def test_carteira():
    carteira = Carteira(valor=100.0, categoria='Comida', data='2022-01-01', descricao='Restaurante XPTO')
    assert str(carteira) == 'Valor: 100.0, Categoria: Comida, Data: 2022-01-01, Descrição: Restaurante XPTO'
