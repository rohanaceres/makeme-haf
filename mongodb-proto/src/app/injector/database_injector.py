""" Mockar o banco com pelo menos dois modelos diferentes para a loja. """

from app.model.amazon import Amazon
from app.model.bestbuy import BestBuy

def mockAmazon():
    # Mock model class:
    amazon = Amazon()
    amazon.carrot1 = 'cenoura normal'
    amazon.carrot2 = 'cenoura radioativa'
    amazon.carrotNumber = 575
    return amazon

def mockBestBuy():
    # Mock model classes
    bestbuy = BestBuy()
    bestbuy.potato1 = 'batata baroa'
    bestbuy.potato2 = 'batata inglesa'
    bestbuy.potatoNumber = 666
    return bestbuy