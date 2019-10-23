def simple_write(fileName, _str):
    with open(fileName, 'w') as file:
        file.write(_str)


if __name__ == '__main__':
    s = "Yet the truely unique feature of our language " + \
        "is not its ability to transmit information " + \
        "about men and lions. Rather, it's the ability to " + \
        "transmit information about things that do not exist at all." + \
        "\n-- Yuval Noah Harari, Sapiens."
    simple_write('new.txt', s)
