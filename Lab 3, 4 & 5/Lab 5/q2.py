class vehicle():
     def __init__(self): # properties of vehicle class
            self.vid = None
            self.name = None
            self.mfd = None
            
class passenger(vehicle):
    def __init__(self): # properties of passenger class
        self.passengers = None
        
    def getInput(self):
            self.vid = input('Enter vehicle ID:')
            self.name = input("Enter owner's name:")
            self.mfd = input('Enter name of manufacturer:')
            self.passengers = input('Enter number of passengers:')
            
    def display(self):
        print('Vehicle ID:', self.vid)
        print('Name of Owner:',self.name)
        print('Name of Manufacturer:',self.mfd)
        print('Number of Passengers:',self.passengers)
        print("\n")

n = int(input('Enter number of vehicles:'))
vehicles = []

for i in range(n):
    vehicles.append(passenger())
    vehicles[i].getInput()
    
print('\nDisplaying all vehicles data:')
print("\n")

for i in range(n):
    vehicles[i].display()