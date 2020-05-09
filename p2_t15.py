while True:
    n = int(input('Enter your age: '))
    if n % 2 != 0:
        print(*range(1, n, 2))
    elif n % 2 == 0:
        print(*range(0, n, 2))

    con = input('Do you want to continue? (y/n): ')
    if con == 'n':
        break
