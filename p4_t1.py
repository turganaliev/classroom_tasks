class Student():
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(f'{self.name} {self.lastname} поступил в {self.year_of_entrance}г. на факультет: {self.department}')

student_1 = Student('Вася', 'Иванов', 'Программирование', 2017)
student_1.get_student_info()
