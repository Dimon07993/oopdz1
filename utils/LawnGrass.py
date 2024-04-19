from utils.MixinLog import MixinLog
from utils.Product import Product


class LawnGrass(Product, MixinLog):

    def __init__(self, name, description, price, count_in_stock, side_producer, time_germination, color):
        super().__init__(name, description, price, count_in_stock)
        self.full_price = None
        self.side_producer = side_producer
        self.time_germination = time_germination
        self.color = color
