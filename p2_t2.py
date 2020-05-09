while True:
    students = int(input('\nEnter a number of students:'))
    apples = int(input('Enter a number of apples:'))
    X = apples % students
    Y = apples // students
    answer = 'Each student will take ' + str(Y) + ' apples,'
    answer += 'and remains ' + str(X) + ' apples.'
    print(answer)
    con = input('Do you want to continue (yes/no):')
    if con == 'no':
        break
