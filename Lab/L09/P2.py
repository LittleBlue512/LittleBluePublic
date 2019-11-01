class dish:
    name = ''
    description = ''

    def info(self):
        return 'name: {}; description: {}'.format(self.name, self.description)


if __name__ == '__main__':
    d1 = dish()
    d1.name = 'Chicken galangal soup'
    d1.description = '(thai) tom kha kai'
    s = d1.info()

    print(type(d1))
    print(type(s))
    print(s)
