while True:
    A = int(input('\nEnter a number: '))
    B = int(input('Enter a number: '))

    if A <= B:
        print(*range(A, B + 1))
    elif A >= B:
        print(*range(B, A + 1))

    con = input('Do you want to continue? (yes/no): ')
    if con == 'no':
        break
