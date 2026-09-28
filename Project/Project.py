import random

'''
# Maybe:
class SensoryInputModule():
    pass

# If close to other animal (smell, sight)
# If close to wall (sight)
'''

randomtest = random.randrange(0,8)

print(randomtest)

animals = []

class Animal():
    def __init__(self, name, location=None):
        self.name = name
        self.location = location


class Beaver(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)
        
        if self.location == None:
            self.location = (5, random.randrange(1,8))


class Orangutan(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)
        
        if self.location == None:
            self.location = (15, random.randrange(1,8), random.randrange(5,10))


class TRex(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)
        
        if self.location == None:
            self.location = (25, random.randrange(1,8))



nibbles = Beaver("Nibbles")
tommy = Orangutan("Tommy")
sue = TRex("Sue")
animals.append(sue)
animals.append(tommy)



print(sue.location)
print(tommy.location)






# pen structure:

# Southern horizontal wall: 0,0 - 30,0
# Northern horizontal wall: 0,10 - 30,10

# Beaver pen:

# Western vertical wall: 0,0 - 0,10
# S to N between B and O: 10,0 - 10,10
# River: 3,1 - 7,1 through 3,9 - 7,9

# Orangutan pen:

# S to N between B and O: 10,0 - 10,10
# S to N O and TR: 20,0 - 20,10

# Rex pen:

# Eastern vertical wall: 30,0 - 30,10
# S-N between O and TR: 20,0 - 20,10



# Interface stuff:

'''

print("-----------------------------------------")
print("|     / /    |             |            |")
print("|     | |    |             |            |")
print("|   Beaver   |  Orangutan  |   T-Rex    |")
print("|     | |    |             |            |")
print("|     / /    |             |            |")
print("-----------------------------------------")
print("                                   _===o ")
print("                                  //   | ")
print("                                 //      ")
'''

'''
"This is a strange zoo, all animal pens are lush forests where these animals thrive."
"It is not the best for the visitors to see the animals but it is the best for the animals"

"The beaver-pen has a river, and the Tyrannosaur-pen has a giant crane to deliver food over the wall"
"The orangutang-pen has no special amenities, they thrive in the tall forest and eat the produce from the trees"

"The pens can mostly sustain it's inhabitants without intervension, exept for the T-rex, for whom outside food is a necessity for calm behaivior.
'''