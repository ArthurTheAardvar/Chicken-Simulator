import random

class Chicken():
    def __init__(self, name):
        self.name = name
        self.hunger = 0
      
   
 
#
    def update(self):
         self.hunger -= 5
         chance = random.randrange(0, 10)
         if self.hunger < 30:
             if chance <=5:
                 print("bok bok")
                 return 1
             elif chance >=6:
                 return 0

    def feed(self):
         self.hunger += 10

    def pet(self):
        print("*Happy Chicken Noises*")


    def printInfo(self):
        print("My name is",self.name, "and my hunger bar is", self.hunger)

chicken = Chicken("Jessica")
chicken2 = Chicken("Daisy")
chicken3 = Chicken("Charlotte")


while True:
    choice = int(input("press 1 to feed Jessica, 2 to feed Daisy, 3 to feed Charlotte, 4 to pet all the chickens, and 5 to check their info: "))
    if choice == 1:
        chicken.feed()
    elif choice == 2:
        chicken2.feed()
    elif choice == 3:
        chicken2.feed()
    elif choice == 4:
        chicken.pet()
        chicken2.pet()
        chicken3.pet()
    elif choice == 5:
        chicken.printInfo()
        chicken2.printInfo()
        chicken3.printInfo()
   
        
    
    chicken.update()
    chicken2.update()
    chicken3.update()
    
#end game loop################################################
    


