
# Part A

# 1.
'''
courses = ["Python", "C#", "English", "Math"]


def greet(name):
    print(f"Hello {name}!\n")

def show_course_name(number):
    print (courses[number])
    print("")

def print_separator(input_string: str):
    list1 = input_string.split()
    for sub in list1:
        print(sub)

    print("\n")


greet("Ada")
greet("Sven")

show_course_name(0)
show_course_name(1)

print_separator("Hi This Is A Test")
print_separator("Hi This Is Another Test!")
'''

# 2. 
'''
def greet(name, city):
    print(f"Hello {name} from {city}!\n")

greet("Ada", "Stockholm")
'''

# 3.
'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Sorry friend, division with zero does'nt work..."
    return a / b


print(add(5, 6))
print(subtract(5, 6))
print(multiply(5, 6))
print(divide(5, 6))
print(divide(5, 0))
'''

# 4.
'''
def divide(a, b):
    if b == 0:
        return "Sorry friend, division with zero does'nt work..."
    return a / b

print(divide(5, 6))

# In this example 'a' and 'b' are the parameters and '5' and '6' are the arguments
'''

# 5.
'''
def calculate_area(width, height):
    return width * height


extra_area = 100

print(calculate_area(10, 5) + extra_area)
'''

# Part B

# 1.
'''
def is_even(number):
    return number %  2 == 0

print(is_even(8))
print(is_even(9))
'''

# 2.
'''
def get_larger(a, b):
    if a >= b:
        return a

    return b

print(get_larger(4, 5))
'''

# 3.
'''
def classify_score(score):
    if score >= 65:
        return "PASS"

    return "FAIL"

print(classify_score(70))
print(classify_score(60))
'''

# 4.
'''
def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Christofer", "Lofgreen"))
'''

# 5.
'''
def calculate_discount(price, percent):
    return price * (percent / 100)

print(calculate_discount(1000, 50))
'''

# 6.
'''
def calculate_discount(price, percent):
    print(price * (percent / 100))

print(calculate_discount(1000, 50) + 100) # TypeError because the function returns None, and None + 100 is... well... an Error :)
'''
'''
def calculate_discount(price, percent):
    return(price * (percent / 100))

print(calculate_discount(1000, 50) + 100) # Returns 600 as we wanted
'''

# Part C

# 1.
'''
def greet(name, greeting='Hello'):
    return (greeting + " " + name)

print(greet("Ada"))
print(greet("Ada", "Congratulations"))
'''

# 2.
'''
def calculate_price(price, quantity=1, discount=0):
    return (price * quantity) * (discount / 100)

print(calculate_price(100, 10, 50))
'''

# 3.
'''
def create_profile(name, city='Unknown', active=True):
    return {"name" : name, "city" : city, "active" : active}

print(create_profile("Chris"))
'''

# 4.
'''
def create_profile(name, city='Unknown', active=True):
    print("name:", name)
    print("city:", city)

create_profile(city="Stockholm", name="Glenn")
'''

# 5.
'''
def invalid(last_name=Ramone, first_name): # A parameter without a default cannot follow a parameter with a default, paramaters with defaults must be at the end.
    print(first_name + " " + last_name)
'''

# Part D

# 1.
'''
def calculate_total(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(calculate_total([1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''

# 2.
'''
def count_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total

print(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''

# 3.
'''
def get_long_words(words, minimum_lenght=0):
    long_words = []
    for word in words:
        if len(word) >= minimum_lenght:
            long_words.append(word)

    return long_words

print(get_long_words(["orangutan", "gorilla", "bonobo"], 8))
'''

# 4.
'''
students = [
    {"name" : "Glenn", "hair color" : "Brown"},
    {"name" : "Anna", "hair color" : "Red"},
    {"name" : "Angie", "hair color" : "Blue"},
    {"name" : "Faud", "hair color" : "Green"}
]

def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

print(find_student(students, "Faud"))
print(find_student(students, "Gregory"))
'''

# 5.

'''
students = [
    {"name" : "Glenn", "score" : 85},
    {"name" : "Anna", "score" : 80},
    {"name" : "Angie", "score" : 75},
    {"name" : "Faud", "score" : 70}
]

def avarage_score(students):
    total_score = 0
    for student in students:
        total_score = total_score + student["score"]

    return total_score / len(students)

print(avarage_score(students))
'''

# 6.
'''
users = [
    {"name" : "Glenn", "active" : True},
    {"name" : "Anna", "active" : False},
    {"name" : "Angie", "active" : True},
    {"name" : "Faud", "active" : False}
]

def get_active_users(users):
    active = []
    for user in users:
        if user["active"]:
            active.append(user)

    return active

print(get_active_users(users))
'''

# Part E

# 1.
'''
def c_to_f(celcius):
    return celcius * (9 / 5) + 32

def temp_feel(celcius):
    if celcius >= 25:
        return "Hot"
    elif celcius >= 20:
        return "Warm"
    else:
        return "Cold"

def temp_report(temp_c):
    return f"{temp_c} celcius feels {temp_feel(temp_c)} and is equivilent to {c_to_f(temp_c)} in Fahrenheit"

print(temp_report(20))
'''

# 2.
'''
order = [
    {"name" : "Item1",
     "quantity" : 3,
     "price" : 95},
     {"name" : "Item2",
      "quantity" : 2,
     "price" : 85},
     {"name" : "Item3",
      "quantity" : 1,
      "price" : 75}
]

def subtotal(order):
    subtotal = 0
    for item in order:
        subtotal = subtotal + (item["quantity"] * item["price"])

    return subtotal

def discount(procent):
    return procent/100

def final_total(order, disc_procent):
    return subtotal(order) * discount(disc_procent)

print(final_total(order, 50))
'''

# 3 - 4
'''
booklist = [
    {"title": "brave new world", "author": "Aldous Huxley", "pages" : 525, "genre": "fiction", "year" : 1946},
    {"title": "1984", "author": "George Orwell", "pages" : 480, "genre": "fiction", "year" : 1944},
    {"title": "the angel of darkness", "author": "Caleb Carr", "pages" : 625, "genre": "fiction", "year" : 1999},
    {"title": "the trial", "author": "Franz Kafka", "pages" : 270, "genre": "fiction", "year" : 1951},
    {"title": "the transformation", "author": "Franz Kafka", "pages" : 70, "genre": "fiction", "year" : 1946},
    {"title": "problems of knowledge", "author": "Michael Williams", "pages" : 200, "genre": "non fiction", "year" : 2011},
    {"title": "the principles of morals", "author": "David Hume", "pages" : 260, "genre": "non fiction", "year" : 1751},
    {"title": "group dynamics", "author": "Donelson R. Forsyth", "pages" : 667, "genre": "non fiction", "year" : 2012},
    {"title": "business reseach methods", "author": "Emma Bell", "pages" : 600, "genre": "non fiction", "year" : 2018}
    ]

def get_genres(booklist):
    genre = []
    for books in booklist:
        genre.append(books.get("genre"))

    genre = set(genre)
    return genre

def get_years(booklist):
    years = []
    for books in booklist:
        title = books.get("title")
        year =  books.get("year")

        years.append((title, year))
    return years

def get_totalpages(booklist):
    totalpages = []
    for b in booklist:
        totalpages.append(b.get("pages"))
    return sum(totalpages)


def main_like():
    dataset = booklist
    genres_list = get_genres(dataset)
    years_list = get_years(dataset)
    total_pages = get_totalpages(dataset)

    return f"The genres are: {genres_list}\nThe years are: {years_list}\nTotal pages are: {total_pages}"

print(main_like())
'''


# Part F

# 1 - 7
'''
list_of_participants = []

def norm_name(name: str) -> str:
    """Returns name without blanks"""
    name = name.replace(" ", "")
    name = name.strip()
    return name


def val_age(age: int) -> bool:
    """Returns boolean: "Old enough" """
    return age >= 18

def reg_fee(age: int, s_status: bool) -> int:
    """ Returns event fee for participant adjusted for age and student status"""
    fee = 100
    if age <= 30 and s_status == True:
        fee = fee - 50

    return fee

def new_participant(name: str, age: int, s_status: bool) -> dict:
    """ adds new participant to the list of participants"""
    name = norm_name(name)
    fee = reg_fee(age, s_status)
    valid_age = val_age(age)
    new_participant = {"name" : name, "valid age": valid_age, "age": age, "student status" : s_status, "fee" : fee}
    list_of_participants.append(new_participant)
    return "participant added"


print(new_participant("Glenn", 35, True))
print(new_participant("Ann", 42, False))
print(new_participant("Anna", 25, True))
print(new_participant("Elisabeth", 25, True))
print(new_participant("Faud", 55, True))
print(new_participant("Ada", 56, False))
print(new_participant("Caroline", 17, False))
print(new_participant("Samantha", 29, True))


def total_rev(list_of_participants: list) -> int:
    """ Returns the anticipated revenue from the event based on fees, excludes participants who are to young to come"""
    total_rev = 0
    for participant in list_of_participants:
        if participant["valid age"] == True:
            total_rev = total_rev + participant["fee"]
    return total_rev


def student_part(list_of_participants: list) ->list:
    """ Returns the participants who are students as a list of their dictionaries"""
    student_part = []
    for partisipant in list_of_participants:
        if partisipant["student status"] == True:
            student_part.append(partisipant)
    return student_part


def oldest_part(list_of_participants: list) -> dict:
    """ Searches the oldest participant in a list of participants and returns that participants dictionary"""
    oldest = 0
    oldest_part = 0
    for partisipant in list_of_participants:
        if partisipant["age"] >= oldest:
            oldest = partisipant["age"]
            oldest_part = partisipant
    return oldest_part

    
def part_summery(participant_name: str, list_of_participants: list) -> str:
    """ Searches for a participant and returning a short summery from list of participants"""
    for part in list_of_participants:
        if part["name"] == participant_name:
            return f"{part["name"]} is {part["age"]} years old. Their fee is {part["fee"]}:-"

'''
            
# Part G

'''
# 1.

booklist = [
    {"title": "brave new world", "author": "Aldous Huxley", "pages" : 525, "genre": "fiction", "year" : 1946},
    {"title": "1984", "author": "George Orwell", "pages" : 480, "genre": "fiction", "year" : 1944},
    {"title": "the angel of darkness", "author": "Caleb Carr", "pages" : 625, "genre": "fiction", "year" : 1999},
    {"title": "the trial", "author": "Franz Kafka", "pages" : 270, "genre": "fiction", "year" : 1951},
    {"title": "the transformation", "author": "Franz Kafka", "pages" : 70, "genre": "fiction", "year" : 1946},
    {"title": "problems of knowledge", "author": "Michael Williams", "pages" : 200, "genre": "non fiction", "year" : 2011},
    {"title": "the principles of morals", "author": "David Hume", "pages" : 260, "genre": "non fiction", "year" : 1751},
    {"title": "group dynamics", "author": "Donelson R. Forsyth", "pages" : 667, "genre": "non fiction", "year" : 2012},
    {"title": "business reseach methods", "author": "Emma Bell", "pages" : 600, "genre": "non fiction", "year" : 2018}
    ]

def min_max(key: str, listofvalues: list) -> tuple:
    """ Returns the (min, max) value for a given key in a list of dictionaries"""
    min = listofvalues[0][key]
    max = listofvalues[0][key]
    for value in listofvalues:
        if value[key] <= min:
            min = value[key]
        elif value[key] >= max:
            max = value[key]
    return (min, max)

print(min_max("year", booklist))
'''
# 2.
'''
def palindrome_check(word: str) -> bool:
    """ Returns the boolean of "Is palindrome" """
    word = word.lower()
    return word[::-1] == word

print(palindrome_check("Apa"))
'''

# 3.
'''
def char_freq(string: str) -> dict:
    """ Returns the frequency of characters excluding " " from a string """
    string = string.upper()
    dict_of_chars = {}
    for character in string:
        if character == " ":
            continue
        elif character in dict_of_chars:
            dict_of_chars[character] += 1
        else:
            dict_of_chars[character] = 1

    return(dict_of_chars)

print(char_freq("Tell me your name"))
'''

# 4.
'''
list_of_nums = [0, 0, 0, 1, 1, -2, -2, 2, 9, -9, 0, -0, 0, 5, 4, 3, 3]

def num_freq(list_of_nums:list) -> dict:
    """ Returns the frequency of positive, negative, and zero numbers from a list """
    dict_of_nums = {"positive" : 0, "negative" : 0, "zero" : 0}
    for num in list_of_nums:
        if num == 0:
            dict_of_nums["zero"] += 1           
        elif num > 0:
            dict_of_nums["positive"] += 1
        elif num < 0:
            dict_of_nums["negative"] += 1

    return(dict_of_nums)


print(num_freq(list_of_nums))
'''

# 5. Added light type hints and docstrings to parts F and G