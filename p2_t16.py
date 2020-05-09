while True:
    w = int(input('\nEnter your weight: '))
    print('\nYour weight on mars:')
    w_m = w * 0.165
    print(w_m)

    print('---')
    for n in range(1, 16):
        each_y = w_m + n
        print(each_y)

    con = input('Do you want to continue? (y/n): ')
    if con == 'n':
        break
