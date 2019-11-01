class dish:
    name = ''
    description = ''
    price = 100

    def __init__(self, name='', desc='', price=100):
        self.name = name
        self.description = desc
        self.price = price

    def info(self):
        return 'name: {}; description: {}'.format(self.name, self.description)

    def discount(self, discount_rate):
        return self.price * (1 - discount_rate/100)


if __name__ == '__main__':
    d1 = dish()
    s = d1.info()
    print(s)
    print(d1.price)
    d2 = dish('mussel pineapple curry')
    s2 = d2.info()
    print(s2)
    print(d2.price)

    d3 = dish('basil spicy hotpot', 'jeolhon', 200)
    s3 = d3.info()
    print(s3)
    print(d3.price)
