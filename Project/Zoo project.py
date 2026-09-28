import random

'''
# Maybe:
class SensoryInputModule():
    pass

# If close to other animal (smell, sight)
# If close to wall (sight)
'''



animals = []

day = 1

time_of_day = 1


# Maybe:
'''
[
    {"1": "Morning"},
    {"2": "Midday"},
    {"3": "Evening"},
    {"4": "Night"},
]
'''
#fruits_in_orangutan_pen = 500

#trees_in_beaverpen = 50

#food_in_trex_pen = 50

#global_climate = 1

#global_event = 0



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
            self.location = (15, random.randrange(1,8), random.randrange(5,10))             # Orangutans are 3D in scope, they use the z-axis.


class TRex(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)
        
        if self.location == None:
            self.location = (25, random.randrange(1,8))

    def movement(self):
        x, y = self.location

        if time_of_day == 1 or time_of_day == 2:
            x = x + random.randrange(-1,1)
            y = y + random.randrange(-1,1)
        elif time_of_day == 3:
            x = x + random.randrange(-3,3)
            y = y + random.randrange(-3,3)
        elif time_of_day == 4:
            x = x + random.randrange(-1,1)
            y = y + random.randrange(-1,1)

        if x > 29:
            x = 29
        elif x < 19:
            x = 19
        elif y > 9:
            y = 9
        elif y < 1:
            y = 1

        self.location = (x, y)




nibbles = Beaver("Nibbles")
tommy = Orangutan("Tommy")
sue = TRex("Sue")
animals.append(sue)
animals.append(tommy)
animals.append(nibbles)



while day <= 5:
    sue.movement()
    print(sue.location)

    user_input = input("Enter to continue, write something to quit")
    if user_input != "":
        break

    day += 1





# pen structure:

# Southern wall: 0,0 - 30,0
# Northern wall: 0,10 - 30,10

# Beaver pen:

# Western vertical wall: 0,0 - 0,10
# Eastern between B and O: 10,0 - 10,10
# River: 3,1 - 7,1 through 3,9 - 7,9

# Orangutan pen:

# Western between B and O: 10,0 - 10,10
# Eastern between O and TR: 20,0 - 20,10

# Rex pen:

# Eastern vertical wall: 30,0 - 30,10
# Western between O and TR: 20,0 - 20,10



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

"The pens can mostly sustain it's inhabitants without intervension, exept the T-rex, for whom outside food is a necessity for calm behaivior.
'''