filenames = ['\ngoogle_kazakstan.txt', 'google_paris.txt',
                'google_uar.txt', 'google_kyrgyzstan.txt',
                'google_san_francisco.txt', 'google_germany.txt',
                'google_moscow.txt', 'google_sweden.txt']

user = input('Enter a key word: ')
if user == 'Hello':
    for filename in filenames:
        print(filename)
    choosen = input('\nPlease, choose an office to complain: ')
    for filename in filenames:
        if choosen == filename:
            with open(filename, 'w') as f_obj:
                complain = input('Write your opinion here: ')
                f_obj.write(complain)
