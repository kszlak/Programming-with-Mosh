class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def all_info(self):
        return self.fname, self.lname, self.email

hr_specialist = Employee('John', 'Smith', '9000')
print(hr_specialist.all_info())