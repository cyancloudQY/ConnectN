import sys


def get_the_value():
    a = sys.argv
    file = a[1]
    with open(file) as f:
        contents = f.readlines()
    k = []
    v = []
    information = {}
    for a in contents:
        key, value = a.split(':')
        value.strip('\n')
        k.append(key)
        v.append(value)
    information = dict(zip(k, v))

    return str(information['blank_char ']).strip('\n').strip(' '), int(information['num_rows ']), \
           int(information['num_cols ']), int(information['num_pieces_to_win '])
