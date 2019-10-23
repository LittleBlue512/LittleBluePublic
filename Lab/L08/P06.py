def write_records(fileName, _dict):
    with open(fileName, 'a') as file:
        for key, val in _dict.items():
            file.write('='.join([key, val]) + '\n')


if __name__ == '__main__':
    world_heritage = {'Ayutthaya': 'Cultural 710 acre',
                      'Sukhothai': 'Cultural 29,290 acre',
                      'Thungyai-Huai Kha Khaeng': 'Natural 1,537,000 acre',
                      'Ban Chiang': 'Cultural 160 acre',
                      'Dong Phayayen-Khao Yai': 'Natural 1,521,000 acre'}
    write_records('unesco.txt', world_heritage)
