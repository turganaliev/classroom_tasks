while True:
    num = int(input("\nGive me a number and I will return it's tens digit: "))
    ten = num ** 10
    print(ten)

    con = input('Do you want to continue? (yes/no): ')
    if con == 'no':
        break
