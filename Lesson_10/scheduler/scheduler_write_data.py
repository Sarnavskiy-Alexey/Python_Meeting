"""
File with write_data methods
"""


def write_data(filename, data, format):
    with open(filename, format, encoding='UTF-8') as f:
        for item in data:
            f.write(' | '.join(item) + '\n')