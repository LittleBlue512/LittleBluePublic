
def count_kmer(k, s):
    cnt = 0
    for i in range(0, len(s)):
        if s[i:i+len(k)] == k:
            cnt += 1
    return cnt


if __name__ == '__main__':
    r = count_kmer('ACTAT', 'ACAACTATGCATACTATCGGGAACTATC')
    print(r)
    r = count_kmer('AC', 'ACAACTATGCATACTATCGGGAACTATC')
    print(r)
    r = count_kmer('ATA', 'CGATATATCCATAG')
    print(r)