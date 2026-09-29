
import animals

import environment







animals_in_zoo = []

day = 1




# Environmental:

#trees_in_beaverpen = 50

#fruits_in_orangutan_pen = 500

#food_in_trex_pen = 50

#global_climate = 1

#global_event = 0



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











flappy = animals.Beaver("Flappy")
nibbles = animals.Beaver("Nibbles")
beni = animals.Orangutan("Beni")
sue = animals.TRex("Sue")
animals_in_zoo.append(sue)
animals_in_zoo.append(beni)
animals_in_zoo.append(nibbles)
animals_in_zoo.append(flappy)



while day <= 100:

    flappy.movement
    nibbles.movement
    print(flappy.location)

    print(animals.beaver_dam)

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