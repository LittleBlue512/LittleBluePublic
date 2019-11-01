from P5_sys import dish


class SDish(dish):
    __smallPrice = 0
    __mediumPrice = 0
    __largePrice = 0

    def get_priceS(self):
        return self.__smallPrice

    def get_priceM(self):
        return self.__mediumPrice

    def get_priceL(self):
        return self.__largePrice

    def set_priceS(self, newPrice):
        self.__smallPrice = newPrice

    def set_priceM(self, newPrice):
        self.__mediumPrice = newPrice

    def set_priceL(self, newPrice):
        self.__largePrice = newPrice


if __name__ == '__main__':
    print(issubclass(SDish, dish))
    d1 = SDish('Chicken galangal soup', 'tom kha kai')
    print(d1.info())
    d1.set_priceS(80)
    d1.set_priceM(100)
    d1.set_priceL(120)
    print(d1.get_priceS(), d1.get_priceM(), d1.get_priceL())
    d2 = SDish('Bamboo shoot salad', 'soop noh mai')
    print(d2.info())
    d2.set_priceS(40)
    d2.set_priceM(60)
    d2.set_priceL(80)
    print(d2.get_priceS(), d2.get_priceM(), d2.get_priceL())

    print(d1.info())
    print(d1.get_priceS(), d1.get_priceM(), d1.get_priceL())
