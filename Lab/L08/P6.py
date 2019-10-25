"""
Write a function named write_records.
The function takes 2 arguments: a filename
and a dictionary whose keys and values all are strings.
Then, the function writes all key-value pairs to a file
 of the given name where each line contains a pair separating
 a key and its value by '=' sign.
"""

from checkdict import sorted_keys


def write_records(fileName, _dict):
    dictKeys = sorted_keys(_dict)
    with open(fileName, 'a') as file:
        for key in dictKeys:
            file.write('='.join([key, _dict[key]]) + '\n')


if __name__ == '__main__':
    world_heritage = {'Ayutthaya': 'Cultural 710 acre',
                      'Sukhothai': 'Cultural 29,290 acre',
                      'Thungyai-Huai Kha Khaeng': 'Natural 1,537,000 acre',
                      'Ban Chiang': 'Cultural 160 acre',
                      'Dong Phayayen-Khao Yai': 'Natural 1,521,000 acre'}

    write_records('unesco.txt', world_heritage)
