"""
Mockar o banco com pelo menos dois modelos diferentes para a loja.
+ Amazon: mocked model 1.
+ BestBuy: mocked model 2.
"""
from app.model.amazon import Amazon
from app.model.bestbuy import BestBuy

def mock_amazon():
    """
    Mock model amazon class.
    """
    amazon = Amazon()
    amazon.carrot1 = 'cenoura normal'
    amazon.carrot2 = 'cenoura radioativa'
    amazon.carrot_number = 575
    return amazon

def mock_bestbuy():
    """
    Mock model BestBuy class.
    """
    bestbuy = BestBuy()
    bestbuy.potato1 = 'batata baroa'
    bestbuy.potato2 = 'batata inglesa'
    bestbuy.potato_number = 666
    return bestbuy
