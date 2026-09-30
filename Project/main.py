import time
import random
import animals
import environment


global_climate = 1

day = 1

management_report = []

animals_in_zoo = []


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

    if day % 10 == 0 and animals.time_of_day == 4:
        global_climate = random.randrange(0, 3)
        animals.day_report.append(f"The trees have sprouted new fruits across all forests")

        for forest in environment.forests:
            forest.fruits = forest.fruits + 10 + (50 * global_climate)


def check_animal_state():

    for animal in animals_in_zoo:
        if animal.state == "fled":
            animals.day_report.append(f"The {animal.species} {animal.name} has 'moved out'... (expect a call from the local authorities)")
            animals_in_zoo.remove(animal)

def animal_release(name):

    animals_in_zoo.append(name)
    animals.day_report.append(name.release_report)


def management_decisions():

    if day == 1 and animals.time_of_day == 4:
        animal_release(flappy)
        animal_release(nibbles)
        
        management_report.append("Release of beavers Nibbles and Flappy")

    if day == 2 and animals.time_of_day == 4:
        animal_release(beni)
        animal_release(cinta)
        animal_release(yutris)
        animal_release(bumi)
        animal_release(monita)

        management_report.append("Release of 5 orangutans")

    if day == 3 and animals.time_of_day == 4:
        animal_release(sue)

        management_report.append("Release of 1 tyrannosaur")

    if day == 10 and animals.time_of_day == 4:
        animal_release(jane)
    
        management_report.append("Release of 1 tyrannosaur")

    if day == 11 and animals.time_of_day == 4:

        management_report.append("Management feels that their job is done and will no longer interevene")
        management_report.append("The board celebrates with champagne in agreement!")

    if day == 12 and animals.time_of_day == 4:
    
            management_report.append("Now that 'active management' is gone things will run their course")
            management_report.append("You will be handed a summery report every 15:th day")

    




# Environmental:

# Beaverdam done

# T-rex stuck in beaver-pen

# T-rex eat orangutan?

# food_in_trex_pen = 50



#global_event = 0





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

while day <= 50:

    for animal in animals_in_zoo:
        animal.movement()

    environmental_change()
    check_animal_state()
    management_decisions()

    animals.time_of_day += 1

    if animals.time_of_day == 5:
    
        print(f"----------------------------\n    | Report Day {day} |\n----------------------------")

        

        if len(animals.day_report) > 0:
            print(f"Animal Report:\n")
            for index, report in enumerate(animals.day_report, start=1):
                print(f"{index}. {report}\n")

        if len(management_report) > 0:
            print(f"Mangement Decisions:\n")
            for index, report in enumerate(management_report, start=1):
                print(f"{index}. {report}\n")

    
        animals.day_report = []
        management_report = []
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