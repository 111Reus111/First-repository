class ComponentCompany():
    def getTotalSalary(self):
        throw NotImplementedError
class Department(ComponentCompany):
    def __init__(self,name):
        self.name = name
        self.subdepartments = []

    def add(self, worker):
        self.subdepartments.append(worker)

    def getTotalSalary(self):
        res = 0
        for worker in self.subdepartments:
            res += worker.getTotalSalary()
        return res

class Worker(Department):
    def __init__(self,name ,salary ):
        self.name = name
        self.salary = salary

    def getTotalSalary(self):
        return self.salary

class CompositeCompany(ComponentCompany):
    def __init__(self):
        self.departments = []


    def add(self, worker):
        self.departments.append(worker)
    def getTotalSalary(self):
        res = 0
        for worker in self.departments:
            res += worker.getTotalSalary()
        return res

company = CompositeCompany()

worker1 = Worker("Makr", 3500)
worker2 = Worker("Borya", 1500)
worker3 = Worker("Katay", 4000)
worker4 = Worker("Vova", 6000)

main_department = Department("Main Department")
minor_department = Department("Minor Department")
second_department = Department("Second Department")
sub_minor_department = Department("Subminor Department")
sub_minor_department = Department("Subminor Department")

sub_minor_department.add(worker2)
second_department.add(worker1)
minor_department.add(worker3)
main_department.add(worker4)
minor_department.add(sub_minor_department)
main_department.add(second_department)
main_department.add(minor_department)

company.add(main_department)
print(company.getTotalSalary())
