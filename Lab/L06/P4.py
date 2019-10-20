def list_info(l):
    res = str(len(l)) + "; "
    for i in range(len(l)-1):
        res += str(l[i]) + "; "

    return res + str(l[-1])


if __name__ == '__main__':
    test_list = ['Pacific', 'Atlantic', 'Indian']
    res = list_info(test_list)
    print(res)

    test_list = ['Area', 513120, 'GDP per capita', 19126]
    res = list_info(test_list)
    print(res)
