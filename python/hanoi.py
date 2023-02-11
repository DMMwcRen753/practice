def hanoi(n, src, via, dest):
    if (n > 1) :
        yield from hanoi(n - 1, src, dest, via)
        yield src, dest
        yield from hanoi(n - 1, via, src, dest)
    else :
        yield src, dest


def tower(n, a, b, c):
    a = [0] * (n - len(a)) + a
    b = [0] * (n - len(b)) + b
    c = [0] * (n - len(c)) + c
    w = n * 2
    print(f'{"A ":^{w}} {"B ":^{w}} {"C ":^{w}}')
    for na, nb, nc in zip(a, b, c):
        print(f'{"- " * na or "| ":^{w}} '
              f'{"- " * nb or "| ":^{w}} '
              f'{"- " * nc or "| ":^{w}}')


def main():
    n = int(input('ハノイの段数 >> '))
    stack = {'A': [*range(1, n + 1)], 'B': [], 'C': []}
    tower(n, *stack.values())
    for src, dest in hanoi(n, 'A', 'B', 'C'):
        print(f'{src}->{dest}')
        stack[dest].insert(0, stack[src].pop(0))
        tower(n, *stack.values())

if __name__ == '__main__':
    main()