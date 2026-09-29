
import random




'''
# Maybe:
class SensoryInputModule():
    pass

# If close to other animal (smell, sight)
# If close to wall (sight)
'''

# Environmental:

animals = []

day = 1

time_of_day = 1

#trees_in_beaverpen = 50

#fruits_in_orangutan_pen = 500

#food_in_trex_pen = 50

#global_climate = 1

#global_event = 0

day_report = []

wall_life = {
    "b_south": 5000, 
    "b_north": 5000, 
    "b_west": 5000, 
    "b_o": 500, 
    "o_north": 5000, 
    "o_south": 5000, 
    "o_t": 500, 
    "t_north": 5000, 
    "t_south": 5000, 
    "t_east": 5000
    }

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
            x, y = self.location

            if y > 5:
                day_report.append(f"Beaver {self.name} ran deep into the forest upon release")
            elif y > 2:
                day_report.append(f"Beaver {self.name} ran into to the forest upon release")
            else:
                day_report.append(f"Beaver {self.name} stayed close to the enrance upon release")

            self.location = (x, y)



    def movement(self):

        if time_of_day <= 2:
            if self.found_stream == False:
                self.find_stream()
                
            elif beaver_dam["progress"] < 100:
                self.build_dam()

            elif beaver_dam["progress"] >= 100:
                #day_report.append(f"The beavers are done with their dam. Expect partial flooding of the beaver pen")
                pass

    def find_stream(self):
        x, y = self.location
        global beaver_dam
        counter = 2

        while counter > 0 and self.found_stream == False:
            for stream_square in stream_squares:
                if stream_square == (x, y):
                    self.found_stream = True
                    if beaver_dam == None:
                        beaver_dam = {"y_coordinate": y, "working": 1, "progress": 0}
                        day_report.append(f"Beaver {self.name} has found the stream and started work on the beaver dam")
                        break
                    else:
                        day_report.append(f"Beaver {self.name} has found the stream and will help with the beaver dam")
                        beaver_dam["working"] += 1
                        break
           
            x = x + random.randrange(-1, 1)
            y = y + random.randrange(-1, 1)

            if x > 9:
                x = 9
            elif x < 1:
                x = 1
            elif y > 9:
                y = 9
            elif y < 1:
                y = 1
                
            counter -= 1

        self.location = (x, y)

    def build_dam(self):
        beaver_dam["progress"] = beaver_dam["progress"] + (beaver_dam["working"] * 0.5)




class Orangutan(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)
        
        if self.location == None:
            self.location = (15, random.randrange(1,8), random.randrange(5,10))             # Orangutans are 3D in scope, they use the z-axis.
            x, y, z = self.location

            if y > 5:
                day_report.append(f"Orangutan {self.name} ran deep into the forest and climbed a tree upon release")
            elif y > 2:
                day_report.append(f"Orangutan {self.name} ran into to the forest and climbed a tree upon release")
            else:
                day_report.append(f"Orangutan {self.name} stayed close to the enrance and climbed a tree upon release")

            self.location = (x, y, z)



class TRex(Animal):
    def __init__(self, name, location=None):
        super().__init__(name, location)
        
        if self.location == None:
            self.location = (25, random.randrange(1,8))
            x, y = self.location

            if y > 5:
                day_report.append(f"Tyrannosaur {self.name} ran deep into the forest upon release")
            elif y > 2:
                day_report.append(f"Tyrannosaur {self.name} ran into to the forest upon release")
            else:
                day_report.append(f"Tyrannosaur {self.name} stayed close to the enrance upon release")

            self.location = (x, y)


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
            x = 25
            wall_life["t_east"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the eastern perimeter wall")
        elif x < 19:
            x = 25
            wall_life["o_t"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the wall between the orangutang and tyrannosaur pen")
        elif y > 9:
            y = 5
            wall_life["t_north"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the northern perimeter wall")
        elif y < 1:
            y = 5
            wall_life["t_south"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the southern perimeter wall")

        self.location = (x, y)



flappy = Beaver("Flappy")
nibbles = Beaver("Nibbles")
tommy = Orangutan("Tommy")
sue = TRex("Sue")
animals.append(sue)
animals.append(tommy)
animals.append(nibbles)
animals.append(flappy)



while day <= 100:

    nibbles.movement()
    flappy.movement()
    sue.movement()

    print(f"------------------------\n    | Daily Report |\n------------------------")

    for report in day_report:
        print(report,"\n")


    user_input = input("Enter to continue, write something else to quit: ")
    
    if user_input != "":
        break


            
    day_report = []
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