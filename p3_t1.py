text = input('Type some sentence: ')
lower = 0
upper = 0

for letter in text:
    if letter == letter.lower():
        lower += 1
    elif letter == letter.upper():
        upper +=1

sum = lower + upper

def percentage(text):
    l = lower/sum*100
    print('Percentage of lower letters: ' + str(l))
    u = upper/sum*100
    print('Percentage of upper letters: ' + str(u))

percentage(text)
