

# Part A

# 1.
'''
number = 0

if number == 0:
    print("zero")
elif number > 0:
    print("positive")
else:
    print("negative")
'''

# 2.
'''
age = input("Print your age: ")
age = int(age)

if age > 65:
    print("pension age! Yeha!")
elif age > 20:
    print("hope you have a job... otherwise, prepare for problems...")
elif age > 14:
    print("try to have fun while it lasts!")
else:
    print("Do remember to listen to your parents some times, they've been through this you know")
'''

# 3.
''' 
user = "username"
password = "P1"

input_u = input("Please write yor username: ")
input_p = input("Please write yor password: ")

if input_u == user and input_p == password:
    print("Great, you're in!")
else:
    print("Sorry, wrong credenntials")
'''

# 4.
'''
score = 50

if score in range(90, 101):
    print ("A")
elif score in range(70, 90):
    print ("B")
elif score in range(50, 70):
    print ("C")
elif score in range(30, 50):
    print ("D")
elif score in range(10, 30):
    print ("E")
else:
    print("YOU'RE OUT OF WACK!")
'''

# 5.
'''
member = False
total_order = 1000

if total_order > 999 or member == True:
    print("ship!")
else:
    print("wait for more orders")
'''

# 6.
'''
1 == 1 #True
1 != 1 #False
1 > 1 #False
1 < 1 #False
1 >= 1 #True
1 <= 1 #True

print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 < 1)
print(1 >= 1)
print(1 <= 1)
'''

# Part B

# 1.
'''
e_str = ""
ne_str = " "
zero = 0
nonzero = 1
e_list = []
ne_list = ["a thing!", "another thing!"]

if e_str:
    print("string!")
else:
    print("no string")

if ne_str:
    print("string!")
else:
    print("no string")

if zero:
    print("number")
else:
    print("no number")

if nonzero:
    print("number")
else:
    print("no number")

if e_list:
    print("list")
else:
    print("no list")

if ne_list:
    print("list")
else:
    print("no list")
'''

# 2.
''' 
languages = ["Python", "C++", "C"]

print("C" in languages)
print("C#" in languages)
'''
# 3.
'''
blocked = ["nastyword1", "nastyword2", "nastyword3"]

user_input = input("Please provide your prefered username: ")

if user_input in blocked:
    print("aha... That won't do dear, and I think you know why")
else:
    print(f"Great! Your username is {user_input}")
'''

# 4.
'''
blocked = ["nastyword1", "nastyword2", "nastyword3"]

user_input = input("Please provide your prefered username: ")

if user_input not in blocked:
    print(f"Great! Your username is {user_input}")
else:
    print("aha... That won't do dear, and I think you know why")
 '''
'''
great_apes = ["orangutan", "schimpanzee", "gorilla", "bonobo", "homo sapiens"]

ape = "makak"

if ape not in great_apes:
    print("might be another type of monkey... Or even a cat!?")
elif ape == great_apes[0]:
    print("We've got the greatest of apes!")
else:
    print("We've got a great ape")
'''

# Part C

# 1.
'''
names = ["Hume", "Mill", "Dennett"]
number = 1
 
for name in names:
    print(name, ": You are welcome to the annual philosophers conference for the dead! \n You are member nr.", number)
    number += 1
 '''

''' 
number = 1
while number <= 50:
    if number % 2 == 0:
        print(number)
        number += 1
    else:
        number += 1
'''

# 3.
'''
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum = sum + number

print(sum)
'''

# 4.
'''
numbers = [1, 2, 3, 4, 5, 2]
largest = 0

for number in numbers:
    if number >= largest:
        largest = number

print(largest)
'''

# 5.
'''
words = ["ape", "orangutan", "pig", "dog", "anaconda"]
above5 = 0

for word in words:
    if len(word)> 5:
        above5 += 1

print(above5)
'''

# 6.
'''
scores = [50, 70, 80, 90, 20, 10]
passes = 0
fails = 0
for score in scores:
    if score >= 70:
        passes += 1
    else:
        fails += 1

print(passes)
print(fails)
'''

# 7.
'''
dictionary = {"name" : "Glenn", "food" : "bacon", "age" : 52}

for key in dictionary:
    print(key)

for key, value in dictionary.items():
    print(key, value)

for item in dictionary.items():
    print(item)
'''

# Part D

# 1.
'''
number = 10

while number in range(1,11):
    print(number)
    number -=1
 '''
# 2.
'''
user_input = input("enter a number for multiplication: ")
user_input = int(user_input)
count = 1

while count < 10:
    print(count," x ", user_input," = ",user_input * count)
    count += 1
'''

# 3.
'''
playlist = ["Song1", "Song2", "Song3", "Song4", "Song5"]

for index, song in enumerate(playlist):
    print(index +1,": ", song)
'''

# 4.
'''
x = 1
y = 1

while x <= 3:
    while True:
        print(x, y)
        y += 1
        if y == 4:
            print(x, y)
            x += 1
            y = 1
            break
 '''
# 5.
''' 
xcount = 1
ycount = 1

list1 = []

while xcount <= 5:
    while ycount <= 5:
        list1.append("X")
        ycount += 1
        if ycount == 6:
            break

    print(list1)
    xcount += 1
 '''


# Part E

# 1.
'''
number = 10

while number in range(0,11):
    print(number)
    number -=1
 '''

# 2.
'''
password = "P1"
user_input = ""

while user_input != password:
    user_input = input("Type password: ")

print("Got it")
 '''

# 3.
''' 
quitstatement = "quit"
user_input = ""

while user_input != quitstatement:
    user_input = input("Type command or 'quit': ")
    print(user_input)
'''

# 4.
'''
counter = int(0)
user_input = int(1)

while user_input != 0:
    user_input = input("Type number: ")
    user_input = int(user_input)
    counter = counter + user_input

print(counter)
 '''

# 5.
'''
counter = int(0)
secret = int(5)
user_input = int(1)

while user_input != secret:
    user_input = input("Guess number: ")
    user_input = int(user_input)

    if user_input > secret:
        print("too high!")
    else:
        print("too low!")

print("Got it!", secret)
'''

# Part F

# 1.
'''
number = 1

while number <= 100:
    if number % 7 == 0 and number % 9 == 0:
        print(number)
        break
    else:
        number += 1
'''

# 2.
'''
strings = ["t1", "t2", "", "t3", "", "t4"]

for string in strings:
    if string == "":
        continue
    else:
        print(string)
'''

# 3.
'''
names = ["Glenn", "Ann", "Ada", "Camille", "Finn"]
target = "Finn"
found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print("Found target: ", target)
else:
    print("not found, went through the whole list... nothing")
 '''

# 4.
'''
nums = [40, 55, -55, -32, 999, 50]

for num in nums:
    if num < 0:
        continue
    elif num == 999:
        print("found 999")
        break
    else:
        print(num)
'''

# Part G

# 1.

studysess = [
    {"subject" : "Python",
     "minutes" : 500},
     {"subject" : "C#",
     "minutes" : 300},
     {"subject" : "C#",
     "minutes" : 200},
     {"subject" : "Python",
     "minutes" : 100},
     {"subject" : "English",
     "minutes" : 30},
     {"subject" : "English",
     "minutes" : 35},    
     {"subject" : "German",
     "minutes" : 5},
     {"subject" : "R",
     "minutes" : 500},
     {"subject" : "German",
     "minutes" : 10},
     {"subject" : "R",
     "minutes" : 105},
]


# 2.
'''
totaltime = 0

for sess in studysess:
    totaltime = totaltime + sess["minutes"]

print(totaltime)
'''

# 3.
'''
emptydict = {}
sub = ""

for dict in studysess:
    sub = dict["subject"]
    emptydict[sub] = 0
    for dict in studysess:
        if dict["subject"] == sub:
            emptydict[sub] += dict["minutes"]

print(emptydict)
'''
# 4.
'''
max = 0

for dict in studysess:
    if dict["minutes"] >= max:
        max = dict["minutes"]

print(max)
'''

# 5.
'''
for dict in studysess:
    if dict["minutes"] > 45:
        print (dict["subject"], dict["minutes"])
'''

# 6.
'''
print("")
print("Welcome to the premier student scruteneering service of 2026!\n(made in close collaboration with Microslop, and a group of anonomous latin american meat-packing glitterati)\n")

while True:
    print ("'as' to view all sessions\n'tt' to view total time\n'fi' to filter by subject\n'quit' to quit\n")
    user_input = input()
    user_input = user_input.lower()
    print("")

    if user_input == "as":
        for dict in studysess:
            print(dict["subject"], dict["minutes"])
        print("")

    elif user_input == "tt":
        totaltime = 0
        for dict in studysess:
            totaltime += dict["minutes"]
        print("total time: ",totaltime, "minutes","\n")

    elif user_input == "fi":
        list_s = []
        for dict in studysess:
            list_s.append(dict["subject"])

        list_s = set(list_s)
        print(list_s)
        user_input = input("Type which subject would you like the total time of: ")
        user_input = user_input.lower()

        totaltime = 0
        user_input = user_input[0].upper() + user_input[1:]
        print(user_input)
        for dict in studysess:
            if dict["subject"] == user_input:
                totaltime += dict["minutes"]
        print("\ntotal time", user_input, ":",totaltime," minutes","\n")

    elif user_input == "quit":
        print("\ngood night!\n")
        break

    else:
        continue
'''



# Part H

# 1.
'''
counter = 1

while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
        counter += 1
    elif counter % 3 == 0:
        print("Fizz")
        counter += 1
    elif counter % 5 == 0:
        print("Buzz")
        counter += 1
    else:
        print(counter)
        counter += 1
'''

# 2.
'''
sentence = input("print a sentence: ")
sentence = sentence.lower()
counter = 0
vowels = ["a", "e", "i", "o", "u"]

for char in sentence:
    if char in vowels:
        counter += 1

print(counter)
'''

# 3.
'''
list1 = [1, 6, 5, 8, 4, 1, 3, 6, 4, 1, 4]
duplicates = []

for item in list1:
    last = list1.pop(item)
    if last in list1:
        duplicates.append(last)

duplicates = set(duplicates)
print(duplicates)
'''

# 4.
'''
list1 = [3, 5, 2]

for number in list1:
    print ("*" * number)
'''