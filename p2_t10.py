while True:
    string = input('Enter any sentence: ')
    if string == 'q':
        break
    print(string[2])
    print(string[1:])
    print(string[:5])
    print(string[:-2])
    print(string[::-2])
    print(string[::2])
    print(string[::-1])
    print(string[::-2])
    print(len(string))
