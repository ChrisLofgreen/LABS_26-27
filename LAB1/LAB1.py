# Part A

# 1.

""" 
print("Christofer Löfgreen")
print("Python 2026")
print("Goal of today is to get more familiarized with Python fundamentals")
 """
# 2.

""" 
name = "Christofer Löfgreen"
age = 42
height = 1.8
student = True

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Student:", student, type(student))
 """
# 3.

""" 
string = "10"
print ("String:", string, type(string))
number = int(string)
print ("Number:", number, type(number)) 
 """
# This shows that Python is dynamicly typed

# 4.

""" 
num1 = 3
num2 = 5
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Exponentiation:", num1 ** num2)
 """
# 5.

""" 
string_to_int = int("10")
int_to_float = float(5)
float_to_string = str(10.5)

print("string to int:", string_to_int, type(string_to_int))
print("int to float:", int_to_float, type(int_to_float))
print("float to string:", float_to_string, type(float_to_string))
 """

# Part B

# 1.

""" 
current_year = 2026
user_age = 0

user_birth_year = int(input("Enter your birth year: "))
user_age = current_year - user_birth_year
print("Your age is:", user_age)
"""
# 2.

'''
user_input_price = (float(input("Enter price: ")))
user_input_discount = (float(input("Enter discount percentage: ")))

discounted_price = user_input_price * (1 - user_input_discount / 100)   
print("Discounted price:", f"{format(discounted_price,'.2f')}")
'''

# 3.
""" 
user_input_tempc = (float(input("Enter temperature in Celsius: ")))
tempf = (user_input_tempc * 9/5) + 32
print("Temperature in Fahrenheit:", f"{format(tempf,'.2f')}") 
"""

# 4.
""" 
user_input_length = (float(input("Enter length of the room in meters: ")))
user_input_width = (float(input("Enter width of the room in meters: ")))
area = user_input_length * user_input_width
parimeter = 2 * (user_input_length + user_input_width)
print("Area of the room:", f"{format(area,'.0f')} m² (rounded to nearest whole number)")
print("Perimeter of the room:", f"{format(parimeter,'.0f')} meters (rounded to nearest whole number)")
 """

# 5.
""" 
user_input_length = (input("Enter length of the room in meters: "))
user_input_width = (input("Enter width of the room in meters: "))
if user_input_length.isdigit() and user_input_width.isdigit():
    user_input_length = float(user_input_length)
    user_input_width = float(user_input_width)
else:
    print("Please enter numeric values for length and width.")
    exit()

area = user_input_length * user_input_width
parimeter = 2 * (user_input_length + user_input_width)
print("Area of the room:", f"{format(area,'.0f')} m² (rounded to nearest whole number)")
print("Perimeter of the room:", f"{format(parimeter,'.0f')} meters (rounded to nearest whole number)")

# Without the conditioning (in this case the IF statement) the program returns "ValueError: could not convert string to float: 'hello'"
# Because a string of chars cannot be converted to a float, but a string of numbers can be converted to a float.
 
 """

# Part C

# 1.
""" 
sentence = "  Orangutans are by any reasonable measure the best primate, this might seem a controversial statement, but it is in fact the truth...  "
print("Length of the sentence:", len(sentence))
print("Sentence in uppercase:", sentence.upper())
print("Sentence in lowercase:", sentence.lower())
print("Whitespace removed:", sentence.strip())
 """

# 2.
""" 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"I declare your name to be {first_name} {last_name}. Welcome to my world!")
 """
# 3.
""" 
string1 = 'python programming'
print(string1[0], string1[-1], string1[0:7], string1[-11:], string1[::-1])
 """

# 4.
""" 
error_message = "Please enter your name using alphabetical characters only. (You are most likley not the offspring of Elon...)"
user_first_name = str(input("Enter your First Name: "))
if user_first_name.isalpha():
    user_first_name = user_first_name.strip()
    user_first_name = user_first_name.lower()
    user_first_name = user_first_name[0:3]
else:
    print(error_message)
    exit()

user_last_name = str(input("Enter your Last Name: "))
if user_last_name.isalpha():
    user_last_name = user_last_name.strip()
    user_last_name = user_last_name.lower()
    user_last_name = user_last_name[0:5]
else:
    print(error_message)
    exit()

username = user_first_name + user_last_name
print(f"Your username is {username}")
 """

# 5.
""" 
user_email = str(input("Please enter you e-mail adress: "))
userdomain = user_email.split("@")

print(userdomain)
 """ 

# 6.
""" 
sentancej = "This is a sentence about Java"
sentencep = sentancej.replace("Java", "Python")

print(sentancej)
print(sentencep)
 """

# Part D

# 1.
""" 
user_input = input(str("write something: "))
user_input = user_input.lower()
user_input = str(user_input)

if user_input[:1] == "he":
    print ("Hello World!")
elif "." in user_input:
    if "@" in user_input:
        print("e-mail")
    else:
        print("domain")
elif user_input[0:3] == "1,2":
    print("3")
elif user_input[6:] == "world!":
    print ("Hello World!")
elif user_input[0:4] == "comp":
    print ("Computer")
elif user_input[0:2] == "or":
    if "gutan" in user_input:
        print("Orangutan")
    else:
        print("Orange")
else:
    print("...")
 """ 

# 2.
""" 
art = 'Artificial Intelligence'
print(f"\n'{art[:3]}' is a debated term, even though most would say that it is a viable construct.\n\
It is likley that it is a product of primates species need for expression.")
print(f"\n'{art[:10]}' is a term that is a little bit like the term 'magic'; 'real' magic can't exist and what we call 'real magic' \n\
is in some sense 'fake'. If we were to be slightly more polite we could say that '{art[:10]}' is something that does not occur in nature\n\
and is put into existence by other means. But that excludes us from nature... You see the point")
print(f"\n'{art[11:]}' is something we are very keen on, even though it is not well defined.\n\
Unsurprisingly we as humans are also keen to connect it closely to something that we do")
print(f"\n'{art[0]}{art[18:22]}y' is a term describing a phenomena that is often confused with '{art[11:]}'. Even though this\n\
term is actually somewhat philosophicly sound.")
print(f"\n'{art[11:14]}' is a data type, a real number with no decimals.")
print(f"\n'{art[11:-2]}{art[13]}{art[17]}{art[8]}' is a cohort of people in a society precieved to have a higher degree of '{art[11:]}' \n\
than the 'common folk'. A highly self-referencial term, mostly used by the '{art[11:-2]}{art[13]}{art[17]}{art[8]}' itself to describe peers")
 """

# 3.
""" 
a = " this is a dog "

if "this" in a.replace("is", "was"):
    print (True)
else:
    print("returns none")

if " this" in a.strip():
    print(a.strip())
else:
    print("the space is not there anymore")

if "this" in a.split():
    print (a.split())
    print("can search for a word in a list created by the function")
 """
# 4.
""" 
string = "Ftring"
#string[0] = "S"
# Above assignment fails because we are trying to make a change within the string (index 0).

# Instead we can remove from the string with slicing and add what we want to a new string:
#string = "S" + string[1:]
#print (string)

#or use .replace, still creating a new string mind you.
string = string.replace("F","S")
print (string)
 """

# Part E

# 1 - 6.
""" 
first_name = input(str("Please enter your first name: "))
first_name = first_name.strip()
last_name = input(str("Please enter your last name: "))
last_name = last_name.strip()
city = input(str("Please enter your city: "))
city = city.strip()
year = input(str("Please enter your year of birth: "))
year = year.strip()
favlanguage = input(str("Please enter your favourite programming language: "))
favlanguage = favlanguage.strip()
idnumber = first_name.lower() + year[-3:-1]
initials = first_name[0] + last_name[0]
full_name = first_name + last_name

print(f"Hi and welcome {first_name} {last_name}.\nYour city is {city} and your year of birth is {year}\nIt is my pleasure to announce that your favourite language is {favlanguage}")


print(f"\n{initials[::-1]} {full_name[::-1]} {favlanguage[::-1]}")

print(full_name[0:3])
print(full_name.upper())
print((year) + (year[::-1])) 
 """

# Part F

# 1.
""" 
seconds = input("Please input a number (seconds): ")
seconds = int(seconds)
hours = seconds // 3600
minutes = (seconds % 3600) / 60

print (f"We have {hours} hour(s) and {minutes} minutes")
 """
# 2.
""" 
integer = int(9876)
one = int(integer/1000)
two = int((integer%1000)/100)
three = int(((integer%1000)%100)/10)
four = int(((integer%1000)%100)%10)

print (one, two, three, four)
 """

# 3.
""" 
user_input = input("input a word, minimum 4 letters: ")
first = user_input[:2]
last = user_input[-2:]
nrbetween = len(user_input) - 4
between = "*" * nrbetween

print (first + between + last)
 """

# 4.

""" 
score = 0
answer = 0


print ("\nHi! and welcome to prediction training version 0.00001!" \
" Please predict the outcome of the following 5 examples: \n")

print("Question 1(5)\n\n x = 5\n y = x + 5\n if y > x:\n\ty = x + y\n")
x = 5
y = x + 5
if y > x:
    y = x + y

answer = input("please type the value of y: ")
answer = int(answer)

if y == answer:
    score = score + 1
    print(f"Great work! Score: {score}\n")
else:
    print(f"Sorry, wrong answer... Score: {score}\n")

print("Question 2(5)\n\n x = \"Orangutans are great!\"\n y = x[:5] + x[13] + x[9:]\n")

x = "Orangutans are great!"
y = x[:5] + x[13] + x[9:]

answer = input("please type the value of y: ")
answer = str(answer)

if y == answer:
    score = score + 1
    print(f"Great work! Score: {score}\n")
else:
    print(f"Sorry, wrong answer... Score: {score}\n")

print("Question 3(5)\n\n x = str(10)\n y = len(x)\n")

x = str(10)
y = len(x)

answer = input("please type the value of y: ")
answer = int(answer)

if y == answer:
    score = score + 1
    print(f"Great work! Score: {score}\n")
else:
    print(f"Sorry, wrong answer... Score: {score}\n")

print("Question 4(5)\n\n x = len(\"10\")\n y = str(x)\n")

x = len("10")
y = str(x)

answer = input("please type the value of y: ")
answer = str(answer)

if y == answer:
    score = score + 1
    print(f"Great work! Score: {score}\n")
else:
    print(f"Sorry, wrong answer... Score: {score}\n")

print("Question 5(5)\n\n z = len(\" 1000 \")\n x = str(z * 2)\n y = x.strip()\n")

z = len(" 1000 ")
x = str(z * 2)
y = x.strip()

answer = input("please type the value of y: ")
answer = str(answer)

if y == answer:
    score = score + 1
    print(f"Great work! Score: {score}\n")
else:
    print(f"Sorry, wrong answer... Score: {score}\n")
 """