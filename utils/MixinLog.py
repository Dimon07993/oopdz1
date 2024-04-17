from utils.ProductTemlate import ProductTemplate


class MixinLog(ProductTemplate):
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID += 1

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.description}, {self.price}, {self.count_in_stock}"



class A:
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)