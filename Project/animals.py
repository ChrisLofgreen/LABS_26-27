import random
import environment

time_of_day = 4

day_report = []

beaver_dam = None

class Animal():
    def __init__(self, name, location=None, state="alert"):
        self.name = name
        self.location = location
        self.state = state


class Beaver(Animal):
    def __init__(self, name, location=None, state="alert"):
        super().__init__(name, location, state)

        self.species = "Beaver"
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
           
            x = x + random.randrange(-1, 2)
            y = y + random.randrange(-1, 2)

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
    def __init__(self, name, location=None, state="alert"):
        super().__init__(name, location, state)

        self.species = "Orangutan"

        self.current_forest = environment.o_forest

        self.direcion_of_curiosity = None

        self.curiosity_directions = ["West", "East"]
        
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

        if self.state == "curious":
            if self.direcion_of_curiosity == "West":
                x = x + random.randrange(-2, 1)
                
                if x < 1:
                    self.state = "fled"
 
                elif x < self.current_forest.x_min:
                    for forest in environment.forests:
                        if x <= forest.x_max and x >= forest.x_min:
                            self.state = "alert"
                            self.direcion_of_curiosity = None
                            self.current_forest = forest
                            day_report.append(f"Orangutan {self.name} has traversed any obstacles and moved to {self.current_forest.name}")
                            continue

            elif self.direcion_of_curiosity == "East":
                x = x + random.randrange(0, 3)
                
                if x > 29:
                    self.state = "fled"
 
                elif x > self.current_forest.x_max:
                    for forest in environment.forests:
                        if x <= forest.x_max and x >= forest.x_min:
                            self.state = "alert"
                            self.direcion_of_curiosity = None
                            self.current_forest = forest
                            day_report.append(f"Orangutan {self.name} has traversed any obstacles and moved to {self.current_forest.name}")
                            continue

        else:

            if time_of_day == 1:
                z = 1
                x = x + random.randrange(-1,2)
                y = y + random.randrange(-1,2)
            if time_of_day == 2:
                z = random.randrange(3,10)
                x = x + random.randrange(-1,2)
                y = y + random.randrange(-1,2)
            elif time_of_day == 3:
                for forest in environment.forests:
                    for coordinate in forest.coordinates:
                        a, b = coordinate
                        if a == x and b == y:
                            fruit_craving = random.randrange(0,3)
                            if forest.fruits >= fruit_craving:
                                forest.fruits = forest.fruits - fruit_craving
                                if fruit_craving > 0:
                                    day_report.append(f"Orangutan {self.name} ate {fruit_craving} units of fruit")

                            else:
                                self.state = "curious"
                                forest.fruits = 0
                                self.direcion_of_curiosity = random.choice(self.curiosity_directions)
                                day_report.append(f"Orangutan {self.name} is not satisfied with the number of fruits in {forest.name} and might look elsewhere")
                                print(self.direcion_of_curiosity)

                z = 10
                x = x + random.randrange(-1,2)
                y = y + random.randrange(-1,2)

            elif time_of_day == 4:
                pass

            if x > self.current_forest.x_max:
                x = self.current_forest.x_max
            elif x < self.current_forest.x_min:
                x = self.current_forest.x_min
            elif y > 9:
                y = 9
            elif y < 1:
                y = 1

        
        self.location = (x, y, z)



class TRex(Animal):
    def __init__(self, name, location=None, state="alert"):
        super().__init__(name, location, state)

        self.species = "Tyrannosaur"

        self.tiredness = 0
        
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
        # IF Beaver dam/lake (stuck/drown, help with rage?)
        x, y = self.location
        stored_location = (x, y)

        if (time_of_day == 1 or time_of_day == 2) and self.tiredness < 100:
            self.state = "alert"
            x = x + random.randrange(-1, 2)
            y = y + random.randrange(-1, 2)

            for wall in environment.walls:
                for coordinate in wall.coordinates:
                    a, b = coordinate
                    if a == x and b == y:
                        wall.health -= 10
                        day_report.append(f"Tyrannosaur {self.name} nibbled on {wall.name}")
                        self.tiredness += 25

                        if wall.health > 0:
                            x, y = stored_location
                        else:
                            day_report.append(f"Tyrannosaur {self.name} has destroyed {wall.name}")
                            self.tiredness -= 10

        elif time_of_day >= 3:
            self.state = "tired"
            pass

        if self.tiredness > 100:
            y = 5
            self.tiredness -= 50
            day_report.append(f"Tyrannosaur {self.name} worn themselves out and is retreating to the interior of the forest to rest")
            self.state = "tired"

        if y > 10 or y < 0 or x > 30 or x < 0:
            self.state = "fled"
            

        self.location = (x, y)