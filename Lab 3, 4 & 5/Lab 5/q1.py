class employee():
    employees = [] # list of all employees
    def __init__(self,ID,name,salary,department):
        self.ID = ID
        self.name = name
        self.salary = salary
        self.department = department
        employee.employees.append((ID,name,salary,department))
    
    @staticmethod    
    def search(ID):
        found = False
        position = -1
        for i in range(len(employee.employees)):
            if(employee.employees[i][0]==ID):
                found = True
                position = i
        if(found==False):
            print('Employee Not Found!')
        else:
            employee.display(position)
            
    @staticmethod    
    def display(position):
        print('ID:',employee.employees[position][0])
        print('Name:',employee.employees[position][1])
        print('Salary:',employee.employees[position][2])
        print('Department:',employee.employees[position][3])
        
n = int(input('Enter number of employees:'))
print("\n")

for i in range(n):
    ID = int(input('Enter id:'))
    name = input('Enter name:')
    salary = float(input('Enter salary:'))
    department = input('Enter department:')
    print("\n")
    employee(ID,name,salary,department)
    
searchID = int(input('Enter ID to be searched:'))
print("\n")
employee.search(searchID)
