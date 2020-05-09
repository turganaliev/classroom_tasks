choices = ['Usain', 'Me', 'Aybek']
numbers = [1, 2, 3]

def choice_to_number(choice):
    if choice == choices[0]:
        return numbers[0]
    elif choice == choices[1]:
        return numbers[1]
    elif choice == choices[2]:
        return numbers[2]

def number_to_choice(number):
    if number == numbers[0]:
        return choices[0]
    elif number == numbers[1]:
        return choices[1]
    elif number == numbers[2]:
        return choices[2]

def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3

def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'

def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        print('WRONG')
    else:
        print('SUCCESS')

test_all()
