class dish:
    name = ''
    description = ''
    __price = 100

    def __init__(self, name='', desc='', price=100):
        self.name = name
        self.description = desc
        self.__price = price

    def info(self):
        return 'name: {}; description: {}'.format(self.name, self.description)

    def discount(self, discount_rate):
        return self.__price * (1 - discount_rate/100)

    def get_price(self):
        return self.__price

    def set_price(self, newPrice):
        self.__price = newPrice


if __name__ == '__main__':
    d1 = dish('Chicken galangal soup', 'tom kha kai', 150)
    d1.set_price(120)
    print(d1.info(), d1.get_price())
    print(hasattr(d1, 'name'))
    print(hasattr(d1, 'price'))
    print(hasattr(d1, '_price'))
    print(hasattr(d1, '__price'))
