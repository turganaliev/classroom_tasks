ns = []
evens = []
while True:
    n = int(input('Enter a number: '))
    ns.append(n)

    for n in ns:
        if n%2 == 0:
            evens.append(n)

    con = input('Show even numbers? (y/n): ')
    if con == 'y':
        print(set(evens))
