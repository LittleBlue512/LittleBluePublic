class dish:
    name = ''
    description = ''
    price = 100

    def info(self):
        return 'name: {}; description: {}'.format(self.name, self.description)

    def discount(self, discount_rate):
        return self.price * (1 - discount_rate/100)


if __name__ == '__main__':
    d1 = dish()
    d1.name = 'Chicken galangal soup'
    d1.description = '(thai) tom kha kai'
    s = d1.info()
    print(type(d1))
    print(type(s))
    print(s)
    print(d1.price)
    p = d1.discount(25)
    print(p)
