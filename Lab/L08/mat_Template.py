"""
Write a function named read_mat.
The function takes a filename,
reads its content containing lines of numbers
separated by spaces
and returns a 2D list of integers
corresponding to the file content.
"""

def read_mat(fname):
    mat = []
    with open(fname, 'r') as f:
        for line in f:

            row = []
            # Write your code here

            mat.append(row)

    return mat

if __name__ == '__main__':

    res = read_mat('mat0.txt')
    print(res)