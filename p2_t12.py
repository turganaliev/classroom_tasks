while True:
    sentence = input('Enter any sentence: ')
    if sentence == 'q':
        break

    if 'f' in sentence:
        print(sentence.index('f'))
