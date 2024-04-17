from utils.MixinLog import MixinLog
from utils.Product import Product


class ProductSmartphone(Product, MixinLog):
    manufacturer: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, count_in_stock, manufacturer, model, memory, color):
        super().__init__(name, description, price, count_in_stock)
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.manufacturer}, {self.model}, {self.memory}, {self.color}"
