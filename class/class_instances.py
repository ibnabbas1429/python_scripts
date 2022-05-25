salary = float()


class Worker:

    num_of_workers = 0

    raise_factor = 1.04 

    def __init__(self, first_name, surname, salary):
        self.first_name = first_name
        self.surname = surname
        self.salary = salary
        self.email = (first_name + '.' + surname + '@gmail.com').lower()

        Worker.num_of_workers +=1

    def Fullname(self):
        return f"{self.first_name}  {self.surname}."


    def details(self):
        return f"{self.first_name}  {self.surname} {self.first_name}.{self.surname}@school.com {self.salary}"

    
    def apply_raise(self):
        self.salary = int(self.salary * Worker.raise_factor )


print(Worker.num_of_workers)
wrker_1 = Worker("Abbas", "Ade", 95000)

wrker_2 = Worker("James", "Nkem", 99000)

print(Worker.num_of_workers)

#stu1 = Students()
wrker_1.details()
print(wrker_1.Fullname)


print(Worker.Fullname(wrker_1))

print(Worker.Fullname(wrker_2))

print(Worker.details(wrker_1))
print(Worker.details(wrker_2))


wrker_1.raise_factor = 1.06

print(wrker_1.salary)

wrker_1.apply_raise()
print(wrker_1.salary)

print(Worker.apply_raise(wrker_1))

print(Worker.raise_factor)
print(wrker_1.raise_factor)


'''# to access the name space of the instance used 
"instance.__dict__." This will tell you about all 
the attribute of the instance and their values in dictorinary form
'''
print(wrker_1.__dict__)

print(Worker.raise_factor)
print(wrker_1.raise_factor)
print(wrker_2.raise_factor)


print(Worker.num_of_workers)
