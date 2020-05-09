from math import factorial

while True:
    n = int(input('\nEnter a number: '))
    a = (1, n)
    print(*map(factorial, a))

    con = input('Continue? (yes/no): ')
    if con == 'no':
        break
