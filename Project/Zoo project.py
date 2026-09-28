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

#trees_in_beaverpen = 50

#fruits_in_orangutan_pen = 500

#food_in_trex_pen = 50

#global_climate = 1

#global_event = 0

beaver_dam = None

stream_squares = [
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4), 
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9)]



class Animal():
    def __init__(self, name, location=None):
        self.name = name
        self.location = location


class Beaver(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)

        self.found_stream = False
        
        if self.location == None:
            self.location = (5, random.randrange(1,8))

    def movement(self):
        x, y = self.location
        global beaver_dam

        if self.found_stream == False:
            counter = 3
            while counter > 0 and self.found_stream == False:
                for stream_square in stream_squares:
                    if stream_square == (x, y):
                        self.found_stream = True
                        if beaver_dam == None:
                            beaver_dam = y
                            print(f"{self.name} has found the stream and started work on the beaver dam!")
                            break
                        else:
                            print(f"{self.name} has found the stream and will help the other beavers with the beaver dam!") 
                            break
           
                x = x + random.randrange(-1, 1)
                y = y + random.randrange(-1, 1)
                print(x, y)
                print(beaver_dam)
                if x > 9:
                    x = 9
                elif x < 1:
                    x = 1
                elif y > 9:
                    y = 9
                elif y < 1:
                    y = 1
                
                counter += 1


        '''
        if time_of_day == 1 or time_of_day == 2:
            x = x + random.randrange(-1,1)
            y = y + random.randrange(-1,1)
        elif time_of_day == 3:
            x = x + random.randrange(-3,3)
            y = y + random.randrange(-3,3)
        elif time_of_day == 4:
            pass
            
        

        '''
        self.location = (x, y)


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
            pass

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

    nibbles.movement()

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
# Stream: 3,1 to 3,9

# Orangutan pen:

# Western between B and O: 10,0 - 10,10
# Eastern between O and TR: 20,0 - 20,10

# Rex pen:

# Eastern vertical wall: 30,0 - 30,10
# Western between O and TR: 20,0 - 20,10



# Interface stuff:

'''

print("-----------------------------------------")
print("|   / /      |             |            |")
print("|   | |      |             |            |")
print("|   Beaver   |  Orangutan  |   T-Rex    |")
print("|   | |      |             |            |")
print("|   / /      |             |            |")
print("-----------------------------------------")
print("                                   _===o ")
print("                                  //   | ")
print("                                 //      ")
'''

'''
"This is a strange zoo, all animal pens are lush forests where these animals thrive."
"It is not the best for the visitors to see the animals but it is the best for the animals"

"The beaver-pen has a stream, and the Tyrannosaur-pen has a giant crane to deliver food over the wall."
"The orangutang-pen has no special amenities, they thrive in the tall forest and eat the produce from the trees"

"The pens can mostly sustain it's inhabitants without intervension, exept for the T-rex, for whom outside food is a necessity for calm behaivior.
'''