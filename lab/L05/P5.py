
def vowel_count(s):
    s = s.lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for c in s:
        if c in vowel:
            cnt += 1

    return cnt

if __name__ == '__main__':
    r = vowel_count('Kruntep Mahanakorn Amornrattanakosin')
    print(r)