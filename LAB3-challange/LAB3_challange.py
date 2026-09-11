
# Part 1

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

for flight in flights:
    if not flight["gate"]:
        flight["gate"] = "Gate not assigned"

print("AIRPORT DEPARTURE SYSTEM\n")

while True:

    print(f"1. View all flights\n2. View delayed flights\n3. View cancelled flights\n4. Search for a flight")
    print(f"5. View flight statistics\n6. Quit\n")

    user_input = input("Choose an option (number): ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("\nOnly one single number, please try again\n")

    if user_input == 1:
        print ("\nALL FLIGHTS\n")
        num = 1
        for flight in flights:
            print(f"{num}. {flight["flightnumber"]} - {flight["dest"]} - {flight["departtime"]} - Gate: {flight["gate"]}")
            num += 1
        print("\n")

    elif user_input == 2:
        print ("\nDELAYED OR CANCELLED FLIGHTS\n")
        for flight in flights:
            status = ""
            if flight["cancelled"]:
                status = "CANCELLED"
            elif flight["delay"] >0:
                if flight["delay"] >= 60:
                    status = "SEVERLEY DELAYED"
                elif flight["delay"] >= 20:
                    status = "DELAYED"
                else:
                    status = "SLIGHT DELAY"
            else:
                status = "ON TIME"
            print(f"{flight["flightnumber"]} - {flight["dest"]} - {status}")
        print("\n")

    elif user_input == 3:
        print ("\nCANCELLED FLIGHTS\n")
        for flight in flights:
                status = ""
                if flight["cancelled"]:
                    status = "CANCELLED"
                    print(f"{flight["flightnumber"]} - {flight["dest"]} - {status}")
        print("\n")

    elif user_input == 4:
        print("\nThese are our upcoming flights:\n")

        for flight in flights:
            print(f"{flight["flightnumber"]}")

        found_flight = False
        status = ""

        while True:
            user_input = input("Please enter the flight number ('Q' or '6' to Quit): ")
            user_input = user_input.upper()

            if user_input == "Q" or user_input == "6":
                break

            for flight in flights:
                if flight["flightnumber"] == user_input:
                    if flight["cancelled"]:
                        status = "CANCELLED"
                    elif flight["delay"] >0:
                        if flight["delay"] >= 60:
                            status = "SEVERLEY DELAYED"
                        elif flight["delay"] >= 20:
                            status = "DELAYED"
                        else:
                            status = "SLIGHT DELAY"
                    else:
                        status = "ON TIME"

                    print(f"\nFlight {flight["flightnumber"]} found:\n")
                    print(f"Destination: {flight["dest"]}\nDeparture: {flight["departtime"]}\nGate: {flight["gate"]}\nPassangers: {flight["passangers"]}\nStatus: {status}\n")
                    found_flight = True

                else:
                    continue

            if found_flight:
                break
            else:
                print("\nFlight not found.\n")

    elif user_input == 5:
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
        print(f"Number of flights with 80% or more capacity utilized: {cap_80}\n")

    elif user_input == 6:
        print ("\nSHUTTING DOWN\n")
        break



