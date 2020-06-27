def load(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip().split()
            if line:
                yield from line


if __name__ == '__main__':
    filename = 'pride-and-prejudice.txt'
    for work in readfile(filename):
        print(work)
