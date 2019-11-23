"""
Chattipoom Sirimul
623040132-7
P8
"""


def list_to_string(_list):
    for i in range(len(_list)):
        _list[i] = str(_list[i])
    return ' '.join(_list)


def readMatrix(fileName):
    res = list()
    with open(fileName, 'r') as file:
        for line in file:
            line = line.split(' ')
            temp = list()
            for e in line:
                e = e.strip()
                temp.append(int(e))
            res.append(temp)
    return res


def writeMatrix(fileName, matrix):
    with open(fileName, 'w') as file:
        for row in matrix:
            temp = list_to_string(row)
            file.write(temp + '\n')


def add_mat(matrix1, matrix2, matrixRes):
    mat1 = readMatrix(matrix1)
    mat2 = readMatrix(matrix2)
    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])
    # Check if two matrices have the same dimension.
    if row1 != row2 or col1 != col2:
        # Create an empty file.
        with open(matrixRes, 'w') as file:
            file.write('')
        return None
    # Addition
    matRes = list()
    for i in range(row1):
        temp = list()
        for j in range(col1):
            temp.append(mat1[i][j] + mat2[i][j])
        matRes.append(temp)
    # Write output matrix.
    writeMatrix(matrixRes, matRes)


if __name__ == '__main__':
    add_mat('mat1.txt', 'mat2.txt', 'outmat.txt')
    add_mat('mat1.txt', 'mat3.txt', 'outmat1.txt')
