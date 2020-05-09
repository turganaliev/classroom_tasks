while True:
    sentence = input('Enter any sentence: ')
    if sentence == 'q':
        break
    words = sentence.count(' ') + 1
    print(words)
