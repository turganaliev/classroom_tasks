class Student():
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def about(self):
        print(f'name: {self.name}, age: {self.age}, major: {self.major}')

Steve = Student('Steven Schultz', 23, 'English')
Johnny = Student('Jonathan Rosenberg', 24, 'Biology')
Penny = Student('Penelope Meramveliotakis', 21, 'Physics')

Steve.about()
Johnny.about()
Penny.about()
