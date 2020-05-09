while True:
    explanation = '\nGive me a two timestamps in (h:m:s) format, and I will return'
    explanation += ' back to you a difference between them in seconds!'
    print(explanation)

    hour_1 = int(input('hour:'))
    min_1 = int(input('min:'))
    sec_1 = int(input('sec:'))
    print('Your first time is ' + str(hour_1) + ':' + str(min_1) + ':' + str(sec_1))

    hour_2 = int(input('hour:'))
    min_2 = int(input('min:'))
    sec_2 = int(input('sec:'))
    print('Your second time is ' + str(hour_2) + ':' + str(min_2) + ':' + str(sec_2))

    def rebuild(hour, min, sec):
        h = hour * 3600
        m = min * 60
        s = sec * 1
        in_seconds = h + m + s
        return in_seconds

    def difference(seconds_1, seconds_2):
        differ = seconds_1 - seconds_2
        if differ < 0:
            answer = differ * differ / -differ
            return answer
        else:
            return differ

    first = rebuild(hour_1, min_1, sec_1)
    second = rebuild(hour_2, min_2, sec_2)
    dif = int(difference(first, second))

    print('The difference between them in seconds is ' + str(dif))

    con = input('Do you want to continue (yes/no): ')
    if con == 'no':
        break
