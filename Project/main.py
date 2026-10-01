import time
import random
import animals
import environment


global_climate = 1

day = 1

management_report = []

summery_report = []

animals_in_zoo = []

lost_animals = []


def flooding():

    new_flooded_squares= []
    for x, y in environment.stream_squares:
        b = y
        if b > animals.beaver_dam["y_coordinate"]:
            a = random.randrange(-1, 2, 2) + x
            if a <= 9 and a >= 1:
                a, b = (a, b)
                new_flooded_squares.append((a, b))

    for square in new_flooded_squares:
        if square not in environment.stream_squares:
            environment.stream_squares.append(square)


def environmental_change():

    if animals.beaver_dam != None and (animals.beaver_dam["progress"] > 90 and day % 14 == 0):
        flooding()

    for wall in environment.walls:
        if wall.health < 1:
            environment.walls.remove(wall)

    if animals.time_of_day == 4:
        for forest in environment.forests:
            if forest.fruits_eaten > 0:
                animals.day_report.append(f"Orangutans have eaten {forest.fruits_eaten} fruits from {forest.name}")
                forest.fruits_eaten = 0
                
    if day % 10 == 0 and animals.time_of_day == 4:
        global_climate = random.randrange(0, 3)
        animals.day_report.append(f"The trees have sprouted new fruits across all forests")

        for forest in environment.forests:
            if forest.fruits < 50:
                forest.fruits = forest.fruits + 10 + (20 * global_climate)


def check_animal_state():

    for animal in animals_in_zoo:

        if animal.state == "fled":
            animals.day_report.append(f"The {animal.species} {animal.name} has 'moved out'... (expect a call from the local authorities)")
            lost_animals.append(animal)
            animals_in_zoo.remove(animal)
        
        if animal.state == "died from starvation":
            animals.day_report.append(f"The {animal.species} {animal.name} has died from starvation")
            lost_animals.append(animal)
            animals_in_zoo.remove(animal)

        if animal.state == "ragehunt":
            x, y = animal.location
            for pray in animals_in_zoo:

                if len(pray.location) == 2 and animal != pray:
                    a, b = pray.location
                    
                    if abs(x - a) < 2 and abs(y - b) < 2:
                        pray.state = f"eaten by {animal.species}"
                        if pray.species == "Beaver" and pray.found_stream == True:
                            animals.beaver_dam["working"] = animals.beaver_dam["working"] - 1

                        lost_animals.append(pray)
                        animals_in_zoo.remove(pray)
                        animal.hunger = 0
                        animal.state = "alert"
                        animals.day_report.append(f"{animal.species} {animal.name} has killed {pray.species} {pray.name}")
                        pray.location = (a, b)
                        animal.location = (x, y)

                elif len(pray.location) == 3 and animal != pray:
                    a, b, c = pray.location
                    
                    if (abs(x - a) < 2 and abs(y - b) < 2) and c < 5:
                        pray.state = f"eaten by {animal.species}"
                        lost_animals.append(pray)
                        animals_in_zoo.remove(pray)
                        animal.hunger = 0
                        animal.state = "alert"
                        animals.day_report.append(f"{animal.species} {animal.name} has killed {pray.species} {pray.name}")
                        pray.location = (a, b, c)
                        animal.location = (x, y)

                    elif (abs(x - a) > 2 and abs(y - b) > 2) and c >= 5:
                        x, y, z = pray.location
                        pray.location = (x + random.randrange(-2, 3), y + random.randrange(-2, 3), z)
                        animals.day_report.append(f"{animal.species} {animal.name} tried to catch {pray.species} {pray.name}, but {pray.name} was climbing to high")
                        pray.location = (x, y, z)
                        animal.location = (x, y)
            
                animal.location = (x, y)
    

                    
def animal_release(name):

    animals_in_zoo.append(name)
    animals.day_report.append(name.release_report)

def put_food_in_tyrannosaur_pen():

    environment.food_in_tyrannosaur_pen["food"] = True
    management_report.append("Food has been delivered to the tyrannosaur pen")

def summery_report_creator():


    summery_report.append(f"      Beaver-pen |Orangutan-pen| T-Rex-pen")
    summery_report.append(f"    -----------------------------------------")
    summery_report.append(f"    |   / /      |             |            |")
    summery_report.append(f"    |   | |      |             |            |")
    summery_report.append(f"    |   | |      |             |            |")
    summery_report.append(f"    |   / /      |             |         (*)|")
    summery_report.append(f"    -----------------------------------------")
    summery_report.append(f"                                       _===o ")
    summery_report.append(f"                                      //   | ")
    summery_report.append(f"                                     //      ")

    summery_report.append(f"\n----------------------Fruits----------------------\n")
   
    total_fruits_eaten = 0

    for forest in environment.forests:
        summery_report.append(f"Fruits in {forest.name}: {forest.fruits} \n")
        
        if forest.fruits_eaten_total > 0:
            summery_report.append(f"Eaten in {forest.name}: {forest.fruits_eaten_total}  (acc)\n")
            total_fruits_eaten += forest.fruits_eaten_total

    if total_fruits_eaten > 0:
        summery_report.append(f"Total fruits eaten: {total_fruits_eaten} (acc)\n")
        total_fruits_eaten = 0

    if animals.beaver_dam != None:
        summery_report.append(f"\n--------------------Beaver dam--------------------\n")
        if animals.beaver_dam["progress"] < 100:
            summery_report.append(f"Beaver dam progress: {animals.beaver_dam["progress"]}% \n")
            summery_report.append(f"Beavers working: {animals.beaver_dam["working"]} \n")
            summery_report.append(f"Beaver dam location: y {animals.beaver_dam["y_coordinate"]} \n")

        else:
            summery_report.append(f"Beaver dam has been built at y coordinate {animals.beaver_dam["y_coordinate"]} \n")
            if len(environment.stream_squares) > 9:
                summery_report.append(f"the dam has caused local flooding north of the dam affecting squares:")
                affected_squares = [(x, y) for x, y in environment.stream_squares if x != 3]
                summery_report.append(f"{affected_squares}\n")

    summery_report.append(f"\n-----------------Tyrannosaur pen------------------\n")
    summery_report.append(f"Food in tyrannosaur pen: {environment.food_in_tyrannosaur_pen["food"]} \n")

    summery_report.append(f"\n-----------------Security status------------------\n")
    for wall in environment.walls:
        if wall.health < 0:
            summery_report.append(f"{wall.name} health: destroyed \n")
        else:   
            summery_report.append(f"{wall.name} health: {wall.health} \n")


    if len(lost_animals) > 0:
        summery_report.append(f"\n-----------------Lost animals-------------------\n")
        for animal in lost_animals:
            summery_report.append(f"{animal.species} {animal.name} : {animal.state}")

    if len(animals_in_zoo) > 0:
        summery_report.append(f"\n-----------------Animals in Zoo-------------------\n")
        for index, animal in enumerate(animals_in_zoo, start=1):
            summery_report.append(f"{index}. {animal.species} {animal.name}")
        if len(animals_in_zoo) == 1:
            summery_report.append(f"\nThere is only 1 animal in the zoo, are you sure you want to continue the simulation?\n")
        summery_report.append(f"\n--------------------------------------------------\n")
    elif len(animals_in_zoo) == 0:
        summery_report.append(f"All animals have been lost or died, are you sure you want to continue the simulation?\n")

    

def management_decisions():

    if day % 15 == 0 and animals.time_of_day == 4:
        summery_report_creator()
        
    if day == 1 and animals.time_of_day == 4:
        animal_release(flappy)
        animal_release(nibbles)
        
        management_report.append("Release of beavers Nibbles and Flappy")

    if day == 2 and animals.time_of_day == 4:
        #animal_release(beni)
        #animal_release(cinta)
        #animal_release(yutris)
        #animal_release(bumi)
        #animal_release(monita)

        management_report.append("Release of 5 orangutans")

    if day == 3 and animals.time_of_day == 4:
        animal_release(sue)

        management_report.append("Release of 1 tyrannosaur")

    if day == 10 and animals.time_of_day == 4:
        animal_release(jane)
        animal_release(slippy)
    
        management_report.append("Release of 1 tyrannosaur and 1 beaver")
        put_food_in_tyrannosaur_pen()

    if day == 11 and animals.time_of_day == 4:

        management_report.append("Management feels that their job is done and they will no longer interevene.")
        management_report.append("The board celebrates with champagne!")
        management_report.append("It has been promised that the Tyrannosaur pen will have food delivered, one wonders if they remembered to call the crane operator...")

    if day == 12 and animals.time_of_day == 4:
    
        management_report.append("Now that 'active management' is gone things will run their course")
        management_report.append("You will now be handed a summery report every 15 days")
        management_report.append("There is one last gift for the zoo:")
        put_food_in_tyrannosaur_pen()



    




# Environmental:

# T-rex stuck in beaver-pen






# Beavers
flappy = animals.Beaver("Flappy")
nibbles = animals.Beaver("Nibbles")
summer = animals.Beaver("Summer")
slippy = animals.Beaver("Slippy")

# Orangutans
beni = animals.Orangutan("Beni")
cinta = animals.Orangutan("Cinta")
yutris = animals.Orangutan("Yutris")
bumi = animals.Orangutan("Bumi")
monita = animals.Orangutan("Monita")

# Tyrannosaurs
sue = animals.TRex("Sue")
jane = animals.TRex("Jane")


#time.sleep(1)

while day <= 100:

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    for animal in animals_in_zoo:
        animal.movement()

    environmental_change()
    check_animal_state()
    management_decisions()

    animals.time_of_day += 1

    if animals.time_of_day == 5:
    
        print(f"--------------------------------------------------\n                 | Report Day {day} |\n--------------------------------------------------")

        if len(summery_report) > 0:
            print(f"                  Summery Report\n")
            for report in summery_report:
                print(report)

        if len(management_report) > 0:
            print(f"               Management Decisions\n")
            for index, report in enumerate(management_report, start=1):
                print(f"{index}. {report}\n")

        if len(animals.day_report) > 0:
            print(f"                  Animal Report\n")
            for index, report in enumerate(animals.day_report, start=1):
                print(f"{index}. {report}\n")

        print("flappy", flappy.location)
        print("nibbles", nibbles.location)
        print("slippy", slippy.location)
        print("summer", summer.location)
        print("sue", sue.location, sue.state)
        print("jane", jane.location, jane.state)

        animals.day_report = []
        management_report = []
        summery_report = []
        day += 1
        animals.time_of_day = 1

        user_input = input("Enter to continue, write something else to quit: ")

        if user_input != "":
            break

        






# Interface stuff:


'''
Start screen: 
please type in the number of beavers you want for your simulation (1-12)
please type in the number of orangutans you would like for your simulation (1-12)


'''

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