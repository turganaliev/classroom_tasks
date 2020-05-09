while True:
    num = int(input('\nInput any number: '))
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    else:
        print(0)

    con = input('Do you want to continue? (yes/no): ')
    if con == 'no':
        break
