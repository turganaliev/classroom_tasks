while True:
    a = int(input("Enter a number of students in group 'a': "))
    b = int(input("Enter a number of students in group 'b': "))
    c = int(input("Enter a number of students in group 'c': "))

    def desks(n):
        if n%2 == 1:
            num = n//2 + 1
            return num
        else:
            num = a/2
            return num

    def all_desks(num_a, num_b, num_c):
        general = num_a + num_b + num_c
        return general

    num_a = desks(a)
    num_b = desks(b)
    num_c = desks(c)
    total = int(all_desks(num_a, num_b, num_c))

    print('Three groups need ' + str(total) + ' desks totally.')

    con = input('Do you wanna check another three groups? (yes/no): ')
    if con == 'no':
        break
