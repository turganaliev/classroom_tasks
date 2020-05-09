while True:
    name = input('\nEnter your name:')
    if name == 'q':
        break
    msg = 'Hello ' + name.title() + '!'
    print(msg)
