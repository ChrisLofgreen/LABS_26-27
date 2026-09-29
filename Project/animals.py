import random
import environment

time_of_day = 1

day_report = []

beaver_dam = None

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

        day_report.append(self.name, "Movement")

        if time_of_day <= 2:
            if self.found_stream == False:
                self.find_stream()
                day_report.append(self.name, "Find Stream")
                
            elif beaver_dam["progress"] < 100:
                self.build_dam()
                day_report.append(self.name, "Damming")

            elif beaver_dam["progress"] >= 100:
                #day_report.append(f"The beavers are done with their dam. Expect partial flooding of the beaver pen")
                day_report.append(self.name, "dam100")
                pass

    def find_stream(self):
        x, y = self.location
        print(x, y)
        counter = 2
        global beaver_dam

        while counter > 0 and self.found_stream == False:
            for stream_square in environment.stream_squares:
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

    def movement(self):
        x, y, z = self.location

        if time_of_day == 1:
            z = 1
            x = x + random.randrange(-1,1)
            y = y + random.randrange(-1,1)
        if time_of_day == 2:
            z = random.randrange(3,10)
            x = x + random.randrange(-2,2)
            y = y + random.randrange(-2,2)
        elif time_of_day == 3:
            z = 10
            x = x + random.randrange(-1,1)
            y = y + random.randrange(-1,1)
        elif time_of_day == 4:
            pass

        if x > 19:
            x = 19
        elif x < 10:
            x = 10
        elif y > 19:
            y = 19
        elif y < 10:
            y = 10

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
          #  wall_life["t_east"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the eastern perimeter wall")
        elif x < 19:
            x = 25
           # wall_life["o_t"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the wall between the orangutang and tyrannosaur pen")
        elif y > 9:
            y = 5
           # wall_life["t_north"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the northern perimeter wall")
        elif y < 1:
            y = 5
            #wall_life["t_south"] -= 10
            day_report.append(f"The tyrannosaur {self.name} has nibbled on the southern perimeter wall")

        self.location = (x, y)