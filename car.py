class Car():
    """an attempt to describe car """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        long_name = self.year+" " +self.make+" "+ self.model        
        return long_name
cars  = []
active = True
while active:
    print ("enter yes to start addin and quit to end the application")
    response = input("enter response: ")
    if response == 'yes':
        name = input("enter make: ")
        model = input("enter model: ")
        year = input("enter year: ")
        car = Car(name,model,year)
        cars.append(car)
    elif response == 'quit':
        print("you choose to qui")
        active = False
    elif response != 'yes' and response != 'quit':
        print("invalid response")
        acive = False
if cars:
    for car in cars:
        print(car.describe_car())

else:
    print("empty list")

