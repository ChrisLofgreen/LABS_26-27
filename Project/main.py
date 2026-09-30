import time
import random
import animals
import environment


global_climate = 1

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
            forest.fruits = forest.fruits + 50 + (50 * global_climate)


def check_animal_state():
    for animal in animals_in_zoo:
        if animal.state == "fled":
            animals.day_report.append(f"The {animal.species} {animal.name} has 'moved out'... (expect a call from the local authorities)")
            animals_in_zoo.remove(animal)
        elif animal.state == "tired":
            animals.day_report.append(f"{animal.species} {animal.name} worn themselves out and is retreating to the interior of the forest to rest")


def management_decisions():

    




# Environmental:

# T-rex stuck in beaver-pen

# T-rex eat orangutan?

#food_in_trex_pen = 50



#global_event = 0




animals_in_zoo = []

day = 1

flappy = animals.Beaver("Flappy")
nibbles = animals.Beaver("Nibbles")
summer = animals.Beaver("Summer")
slippy = animals.Beaver("Slippy")

beni = animals.Orangutan("Beni")
cinta = animals.Orangutan("Cinta")
yutris = animals.Orangutan("Yutris")
bumi = animals.Orangutan("Bumi")
monita = animals.Orangutan("Monita")

sue = animals.TRex("Sue")
jane = animals.TRex("Jane")



animals_in_zoo.append(sue)
animals_in_zoo.append(beni)
animals_in_zoo.append(nibbles)
animals_in_zoo.append(flappy)

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
            for index, report in enumerate(animals.day_report, start=1):
                print(f"{index}. {report}\n")
        else:
            print("No news today")
    
        animals.day_report = []
        day += 1
        animals.time_of_day = 1

        user_input = input("Enter to continue, write something else to quit: ")

        if user_input != "":
            break




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

'''
walls_old = {
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
'''

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