class Employee:
    a=1
    b=2
    def __init__(self,first,last,pay):
        self.name=first
        self.pay=pay
        self.last=last
        self.email=first + last + '@gmail.com'
        Employee.a+=1
    def fullname(self):
        return self.name +self.last
    def c(self):
        self.d=Employee.a+self.b
        return self.d 

      


     
emp_1 = Employee('Vekhyat','Jain',100000)
emp_2 = Employee('Test','User',1000)
# emp_1.a=3
# Employee.a=5
# print(emp_1)
# print(emp_2)
# print()
# # emp_1.first= 'Vekhyat'
# # emp_2.last = 'Jain'
# # emp_1.email= 'vekhyatjain123@gmail.com'
# # emp_1.pay=100000000

# # emp_2.first= 'Test'
# # emp_2.last = 'User'
# # emp_2.email= 'aveerasb@gmail.com'
# # emp_2.pay=10000000

# print(emp_1.email,emp_2.email)

# print(emp_1.fullname())
print(emp_1.__dict__)
print(Employee.a)

