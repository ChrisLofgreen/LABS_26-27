
import random
import animals
import environment




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
    if animals.beaver_dam != None and (animals.beaver_dam["progress"] > 10 and day % 14 == 0):
        flooding()

    for wall in environment.walls:
        if wall.health < 1:
            environment.walls.remove(wall)


def check_animal_state():
    for animal in animals_in_zoo:
        if animal.state == "fleed":
            animals_in_zoo.remove(animal)
            animals.day_report.append(f"{animal.name} has 'moved out'... (expect a call from the local authorities)")

    print(len(animals_in_zoo))






# Environmental:

#trees_in_beaverpen = 50

#fruits_in_orangutan_pen = 500

#food_in_trex_pen = 50

#global_climate = 1

#global_event = 0

#Change randoms -> animals stop + 1



animals_in_zoo = []

day = 1




flappy = animals.Beaver("Flappy")
nibbles = animals.Beaver("Nibbles")
summer = animals.Beaver("Summer")
slippy = animals.Beaver("Slippy")
beni = animals.Orangutan("Beni")
sue = animals.TRex("Sue")
animals_in_zoo.append(sue)
#animals_in_zoo.append(beni)
#animals_in_zoo.append(nibbles)
#animals_in_zoo.append(flappy)



while day <= 100:

    for animal in animals_in_zoo:
        animal.movement()

    environmental_change()
    check_animal_state()
    
    





    print(f"------------------------\n    | Daily Report |\n------------------------")

    for report in animals.day_report:
        print(report,"\n")



    user_input = input("Enter to continue, write something else to quit: ")
    
    if user_input != "":
        break


    animals.day_report = []
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