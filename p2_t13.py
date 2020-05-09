while True:
    n = int(input('Enter a number: '))

    def squares(n):
        for a in range(1, n + 1):
             print(a ** 2)

    squares(n)

    con = input('Do you want to continue? (yes/no): ')
    if con == 'no':
        break
