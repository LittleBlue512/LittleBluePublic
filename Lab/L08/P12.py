import math


# Return a dictionary containing the frequency of words in the file.
def getWords(fileName):
    # Skip the first line!!!!!
    skipFirstLine = True
    res = dict()
    with open(fileName, 'r') as file:
        for line in file:
            if (skipFirstLine):
                skipFirstLine = False
                continue
            words = [x.rstrip('. \n').rstrip('.').lower() for x in line.split(' ')]
            for word in words:
                if word in res:
                    res[word] += 1
                else:
                    res[word] = 1
    return res


# Return a 2D dictionary containing the frequency of words in each file.
def getFiles(fileList):
    res = dict()
    for fileName in fileList:
        res[fileName] = getWords(fileName)
    return res


def getSecondHalf(word, fileWords):
    Nt = 0
    for words in fileWords.values():
        if word in words:
            Nt += 1
    return math.log(len(fileWords.keys()) / (1 + Nt))


def culture_tf_idf(list_filename):
    res = dict()
    fileWords = getFiles(list_filename)
    for fileName, words in fileWords.items():
        res[fileName] = dict()
        for word, cnt in words.items():
            tf_d = cnt
            sum_tf_d = sum(words.values())
            firstHalf = tf_d / sum_tf_d
            secondHalf = getSecondHalf(word, fileWords)
            res[fileName][word] = firstHalf * secondHalf
    return res


def nice_print2Ddict(d):
    dkeys = list(d.keys())
    dkeys.sort()
    for k in dkeys:
        print('\n', k)
        d2 = d[k]
        k2s = list(d2.keys())
        k2s.sort()
        print('*', end=' ')
        for k2 in k2s:
            print("{}:{:.3f}".format(k2, d2[k2]), end='; ')


if __name__ == '__main__':
    cultures = ['chinese.txt', 'thai.txt', 'japanese.txt']
    res = culture_tf_idf(cultures)
    nice_print2Ddict(res)
