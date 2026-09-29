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
    def __init__(self, name, location=None, rage=False):
        super().__init__(name, location)

        self.rage = rage
        
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
        stored_location = (x, y)

        if time_of_day == 1 or time_of_day == 2:
            x = x + random.randrange(-1,1)
            y = y + random.randrange(-1,1)

            for wall in environment.walls:
                for coordinate in wall.coordinates:
                    if coordinate == (x, y):
                        wall.health -= 10
                        day_report.append(f"Tyrannosaur {self.name} nibbled on {wall.name}")

                        if wall.health > 0:
                            x, y = stored_location
                        else:
                            day_report.append(f"Tyrannosaur {self.name} has destroyed {wall.name}")


        elif time_of_day == 3:
            counter = 2
            while counter > 0:
                x = x + random.randrange(-1,1)
                y = y + random.randrange(-1,1)

                for wall in environment.walls:
                    for coordinate in wall.coordinates:
                        if coordinate == (x, y):
                            wall.health -= 10
                            day_report.append(f"Tyrannosaur {self.name} nibbled on {wall.name}")

                            if wall.health > 0:
                                x, y = stored_location
                            else:
                                day_report.append(f"Tyrannosaur {self.name} has destroyed {wall.name}")



        elif time_of_day == 4:
            pass
            
        self.location = (x, y)