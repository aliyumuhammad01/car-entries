class Restuarant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restuarant(self):
        print(self.name.title()+ " of "+ self.cuisine_type.title())
    def open_restuarant(self):
        print(self.name.title()+ "is now open")
    def set_num_served(self,num):
        self.number_served += num

restuarant = Restuarant("sabil", "traditioal")
restuarant.describe_restuarant()

restuarant1 = Restuarant('al-amir', "hausa ")
restuarant2 = Restuarant("dala", "fulde")
restuarant3 = Restuarant("wanasa","arab")
restuarant.set_num_served(12)
print("Customers served: " +str(restuarant.number_served))
