def hanoi(n, src, via, dest):
    if (n > 1) :
        yield from hanoi(n - 1, src, dest, via)
        yield src, dest
        yield from hanoi(n - 1, via, src, dest)
    else :
        yield src, dest


def main():
    n = int(input('円盤の数 >> '))
    for src, dest in hanoi(n, 'A', 'B', 'C'):
        print(f'{src}->{dest}')
        
if __name__ == '__main__':
    main()