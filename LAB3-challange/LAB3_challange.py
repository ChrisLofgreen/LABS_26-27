
flights = [
    {"flightnumber" : "SK142",
     "dest" : "Munich",
     "departtime" : 1445,
     "gate" : "B4",
     "passangers" : 145,
     "max_cap" : 180,
     "delay" : 25,
     "cancelled" : False},
    {"flightnumber" : "AB496",
     "dest" : "Gothenburg",
     "departtime" : 1320,
     "gate" : "A2",
     "passangers" : 90,
     "max_cap" : 140,
     "delay" : 10,
     "cancelled" : False},
    {"flightnumber" : "DC248",
     "dest" : "Paris",
     "departtime" : 1005,
     "gate" : "C1",
     "passangers" : 150,
     "max_cap" : 210,
     "delay" : 10,
     "cancelled" : True}, 
    {"flightnumber" : "CA696",
     "dest" : "Dusseldorf",
     "departtime" : 1200,
     "gate" : "A3",
     "passangers" : 50,
     "max_cap" : 140,
     "delay" : 0,
     "cancelled" : False},
     {"flightnumber" : "DG642",
      "dest" : "Provance",
      "departtime" : 1645,
      "gate" : "C2",
      "passangers" : 150,
      "max_cap" : 180,
      "delay" : 0,
      "cancelled" : False},
     {"flightnumber" : "FG192",
      "dest" : "Rome",
      "departtime" : 1545,
      "gate" : "B4",
      "passangers" : 0,
      "max_cap" : 150,
      "delay" : 10,
      "cancelled" : False},      
     {"flightnumber" : "CB411",
      "dest" : "Kiev",
      "departtime" : 905,
      "gate" : "",
      "passangers" : 150,
      "max_cap" : 180,
      "delay" : 70,
      "cancelled" : False},
      {"flightnumber" : "UA512",
      "dest" : "Prag",
      "departtime" : 825,
      "gate" : "B3",
      "passangers" : 163,
      "max_cap" : 180,
      "delay" : 0,
      "cancelled" : False},
      {"flightnumber" : "UB342",
      "dest" : "Oslo",
      "departtime" : 1015,
      "gate" : "D1",
      "passangers" : 175,
      "max_cap" : 180,
      "delay" : 0,
      "cancelled" : False},
      {"flightnumber" : "EA312",
      "dest" : "Copenhagen",
      "departtime" : 1110,
      "gate" : "D2",
      "passangers" : 178,
      "max_cap" : 190,
      "delay" : 10,
      "cancelled" : False}
]


# Data cleaning:

for flight in flights:
    if not flight["gate"]:
        flight["gate"] = "Gate not assigned"

# Add status field to flights

for flight in flights:    
    if flight["cancelled"]:
        flight["status"] = "CANCELLED"
    elif flight["delay"] >0:
        if flight["delay"] >= 60:
            flight["status"] = "SEVERLEY DELAYED"
        elif flight["delay"] >= 20:
            flight["status"] = "DELAYED"
        else:
            flight["status"] = "SLIGHT DELAY"
    else:
        flight["status"] = "ON TIME"

# Welcome message:

print("AIRPORT DEPARTURE SYSTEM\n")


# Base functions:

def gate_overview():
    print ("\nGATE OVERVIEW\n")
    terminal_list = ["A", "B", "C"]
    gatenr = 1

    for terminal in terminal_list:
        while gatenr <= 4:
            print ("Gate", terminal + str(gatenr))
            gatenr += 1
        gatenr = 1 

    return("")


def view_all_flights():
    print ("\nALL FLIGHTS\n")

    for index, flight in enumerate(flights, start=1):
        print(f"{index}. {flight["flightnumber"]} - {flight["dest"]} - {flight["departtime"]} - Gate: {flight["gate"]}")

    return "\n"
    

def view_delayed_or_cancelled():
    print ("\nDELAYED OR CANCELLED FLIGHTS\n")

    for flight in flights:    
        if flight["status"] != "ON TIME":
            print(f"{flight["flightnumber"]} - {flight["dest"]} - {flight["status"]}")

    return "\n"


def view_cancelled():
    print ("\nCANCELLED FLIGHTS\n")

    for flight in flights:
        if flight["status"] == "CANCELLED":
            print(f"{flight["flightnumber"]} - {flight["dest"]} - {flight["status"]}")

    return "\n"


def search_for_flight():
    print("\nThese are our upcoming flights:\n")

    for flight in flights:
        print(f"{flight["flightnumber"]}")

    found_flight = False

    while True:
        user_input = input("Please enter the flight number ('Q' or '6' to Quit): ")
        user_input = user_input.upper()

        if user_input == "Q" or user_input == "6":
            return "\n"

        for flight in flights:
            if flight["flightnumber"] == user_input:
                print(f"\nFlight {flight["flightnumber"]} found:\n")
                print(f"Destination: {flight["dest"]}\nDeparture: {flight["departtime"]}\nGate: {flight["gate"]}\nPassangers: {flight["passangers"]}\nStatus: {flight["status"]}")
                found_flight = True
            else:
                continue

        if found_flight:
            return "\n"
        else:
            print("\nFlight not found.\n")


def flight_statistics():
    print ("\nFLIGHT STATISTICS\n")
    scheduled = len(flights)
    no_pass = 0
    cancelled = 0
    delayed = 0
    total_pass = 0
    max_pass = 0
    max_pass_flight = ""
    cap_80 = 0

    for flight in flights:
        if flight["cancelled"] == True:
            cancelled  += 1
        elif flight["delay"] > 0 and flight["cancelled"] == False:
            delayed += 1

    for flight in flights:
        total_pass = total_pass + flight["passangers"]
        if flight["passangers"] > max_pass:
            max_pass = flight["passangers"]
            max_pass_flight = flight["flightnumber"]

        if flight["passangers"]/ flight["max_cap"] >= 0.8:
            cap_80 += 1

        if flight["passangers"] == 0:
            no_pass += 1

    print("Scheduled flights:",scheduled)
    print("Cancelled flights:",cancelled)
    print("Delayed flights:",delayed)
    print("Flights on time:",(scheduled - cancelled) - delayed)
    print("Total passangers:",total_pass)
    print("Avg passanger count:", total_pass / (scheduled - no_pass))
    print("Highest passanger count:","Flight",max_pass_flight,"Passangers:",max_pass)
    print(f"Number of flights with 80% or more capacity utilized: {cap_80}")
    return "\n"
    



while True:

    print(f"0. Gate overview \n1. View all flights\n2. View delayed flights\n3. View cancelled flights")
    print(f"4. Search for a flight\n5. View flight statistics\n6. Quit\n")

    user_input = input("Choose an option (number): ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("\nOnly one single number, please try again\n")


    if user_input == 0:
        print(gate_overview())

    elif user_input == 1:
        print (view_all_flights())

    elif user_input == 2:
        print(view_delayed_or_cancelled())

    elif user_input == 3:
        print (view_cancelled())

    elif user_input == 4:
        print(search_for_flight())

    elif user_input == 5:
        print(flight_statistics())
        
    elif user_input == 6:
        print ("\nSHUTTING DOWN\n")
        break





# variables where the type is not defined becomes strings under the input() function, before this excercise i thought that 
# this was more arbitrary for some reason (why would it be..?). But it is quite clear that even numbers become strings when using input(). 
# For this program the problem with that becomes that I need to convert the sting to an integer for the main input loop to work.
# But if that input is something that cannot be converted to an integer we will get a ValueError.
# 
# I solved it by the try-statement even though I know we havn't learned it yet, I do think that this is the right solution.
# But I also couldnt figure out an if-statement that would work to solve the problem completley unless I just declare 
# every single agreeable option (numbers 0-6 as strings) in the if-statement,
# and that seemed both constraining and bloated at the same time somehow... 
# Also if anyone wanted to add a new option in the program later on it wouldnt work unless they also changed that if-tree.

# Now i get it: the if statement could be taking from a list of "agreable options". if in... etc. else: "error message".
# I still think the try-statement is probably the "right" solution, but I should have done the list for this task 
# since try had not been part of the course yet.

