def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False
    print("YOUR CODE IS CORRECT!")

test_is_even()
