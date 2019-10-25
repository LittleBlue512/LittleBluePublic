"""
Write a function named read_mat.
The function takes a filename,
reads its content containing lines of numbers
separated by spaces
and returns a 2D list of integers
corresponding to the file content.
"""


def read_mat(fileName):
    res = list()
    with open(fileName, 'r') as file:
        for line in file:
            res.append([int(x.rstrip()) for x in line.split(' ')])
    return res


if __name__ == '__main__':

    res = read_mat('mat0.txt')
    print(res)
