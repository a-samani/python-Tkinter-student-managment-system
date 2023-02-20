


class Person:
    def __init__(self, person_number, name, year, marriage, income1, income2, income3):
        self.personNumber = person_number
        self.name = name
        self.semester = year
        self.income_one = income1
        self.income_two = income2
        self.income_three = income3
        self.average = (income3 + income2 + income1) / 3
        self.marriage = marriage

    # info
    def get_person_number(self):
        return self.personNumber

    def set_person_number(self, new):
        self.personNumber = new

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def get_marriage(self):
        return self.marriage

    def set_marriage(self, marriage):
        self.semester = marriage

    # scores

    def set_income_one(self, new_score):
        self.income_one = new_score
        self.average = (self.income_three + self.income_two + self.income_one) / 3

    def get_income_one(self):
        return self.income_one

    def set_income_two(self, new_score):
        self.income_two = new_score
        self.average = (self.income_three + self.income_two + self.income_one) / 3

    def get_income_two(self):
        return self.income_two

    def set_income_three(self, new_score):
        self.income_three = new_score
        self.average = (self.income_three + self.income_two + self.income_one) / 3

    def get_income_three(self):
        return self.income_three

    def get_average(self):
        return self.average
