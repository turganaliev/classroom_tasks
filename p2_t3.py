while True:
    num = int(input('\nEnter a number:'))
    next = num + 1
    previous = num - 1
    msg = 'The next number for the ' + str(num) + ' is ' + str(next) + '.'
    msg += '\nThe previous number for the ' + str(num) + ' is ' + str(previous) + '.'
    print(msg)
    con = input('Do you want to continue (yes/no):')
    if con == 'no':
        break
