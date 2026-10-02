

# Part A

# 1.
'''
course_name = "Python"

def create_var():
    course_name = "Pythonesque"
    return course_name

print(course_name)
print(create_var())
'''
# in the first case (print(course_name)), we print the local variable since the one in the function is not available
# in the second case (print(create_var())) we look first within the function so therefore prints the "new" "course_name" within it.
# if we wanted otherwise we could intorduce the global variable or its value in our function: 
# Either by "global" or by adding a parameter to take the value from the global function

# 2.
'''
counter = 1

def counter_function(addon):
    counter = 2 + addon
    print(counter)

counter_function(counter)
print(counter)
'''

# 3.

# Non functional example:
'''
global_var = 5

def changer_function():
    global_var += 1
    return global_var

print(changer_function())
'''
# The problem with above is that we cannot access global_var. We could ofcourse create a local variable called "global_var"
# But that would be a new local variable with it's own value.

# I we want to change global_var we need to call it's value as a variable within the function (in this case change_var)
# and then update the value of global_var according to whatever is in the function, in this case + 1

# Functional example:
'''
global_var = 5

def changer_function(change_var):
    change_var += 1
    return change_var

global_var = changer_function(global_var)
print(global_var)
'''

# 4.
'''
def outer_function():
    outer_var = "I am outer"

    def inner_function():
        inner_var = "I am inner"
        print(outer_var + " & " + inner_var)
    inner_function()


outer_function()
'''

# 5.
'''
list_a = [1, 2, 3, 4, 5]
string1 = "I am A string, but I do not define the concept 'string'"
list_a_total = sum(list_a)
list_a_max = max(list_a)
'''

# Part B

# 1.
'''
def add_all(*numbers):
    total_nums = 0
    for num in numbers:
        total_nums = num + total_nums

    return total_nums

print(add_all(1, 2, 3, 4, 5))
'''

# 2.
'''
def average(*numbers):
    total_nums = 0
    if numbers == ():
        return "Nada (which is significantly different from None)"
    else:
        for num in numbers:
            total_nums = num + total_nums

    return total_nums/len(numbers)

print(average(1, 1, 2, 2))
'''

# 3.
'''
def longest_word(*words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word("orangutan", "bike", "beaver", "boat"))
'''

# 4.
'''
def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        sentence = sentence + word + separator

    if separator == "":
        return sentence
    else:
        return sentence[0:-1]

print(build_sentence(" ", "The", "greatest", "ape", "is", "the", "orangutan"))
'''

# 5.
'''
def describe_scores(student_name, *scores):
    total_score = 0
    for score in scores:
        total_score = score + total_score

    return "Name:",student_name, "Number of scores:", len(scores), "Avarage score:", total_score / len(scores)

print(describe_scores("Beatrice", 10, 50, 60, 20))
'''

# Part C

# 1.
'''
list_a = [10, 20, 30]

def unpacker(a, b, c):
    print("x:", a ,"y:", b,"z:", c)

unpacker(*list_a)
'''

# 2.
'''
tuple_a = ("first_name", "last_name", "city")

def getting_var_names(a, b, c, fn, ln, ci):
    print(a, fn)
    print(b, ln)
    print(c, ci)

getting_var_names(*tuple_a, "David", "Hume", "London")
'''

# 3 - 4
'''
list_a = ["a", "b", "c", "d"]

def starred_assign(first, *middle, last=1):
    print("F", first)
    print("M", middle)
    print("L", last)

starred_assign(*list_a)

# Star in a parameter in a function allows for more than one value in that parameter by arranging them into a tuple.
# Useful when there is an unknowable number of values in a collection.

# Star in a function call allows for unpacking of a collection-object into serveral parameters.
# Useful for unpacking when the maximum number of possible values is known, or to catch a predetermened number of values
# and put the rest in an overflow- parameter (which should then have a star itself)
'''

# Part D

# 1.
'''
def show_profile(**info):
    for key, value in info.items():
        print(key, ":" ,value)

show_profile(name="Glenn", age=55, city="Gothenburg")
'''

# 2.
'''
def create_user(username, **details):
    user = {"username" : username}
    for key, value in details.items():
        user[key] = value

    print(user)

create_user("coolestofall99", name="Harriet", age=42, interests=["cooking", "cars", "motorcycles"])
'''

# 3.
'''
def build_product(name, price, **metadata):
    product = {"name" : name, "price" : price}
    for key, value in metadata.items():
        product[key] = value

    print(product)

build_product(name="Supercar", price=999000, engine="v10", displacement=3.0, forced_induction=False)
'''


# 4.
'''
def import_settings(**settings):
    revised_settings = {}
    for key, value in settings.items():
        if value == None:
            continue
        else:
            revised_settings[key] = value

    print (revised_settings)


import_settings(height=55, speed=500, test=None, shape="round")
'''

# 5.
'''
student = {
    "name" : "Heidi",
    "age" : 30,
    "course" : "Python"
}


def import_student_data(name, age, course):
    print(name)
    print(age)
    print(course)

import_student_data(**student) 
'''

# Part E

# 1.

'''
def log_event(event_type, *messages, **metadata):
    event = {"type" : event_type}
    input_messages = []

    for message in messages:
        input_messages.append(message)

    for key, value in metadata.items():
        event[key] = value

    event["messages"] = input_messages
    print(event)

log_event(
    "crash",
    "what is going on",
    "why is that one blinking red?",
    "Arm seat",
    "Jump",
    casualties=0,
    assets_destroyed=1,
    asset_value=10000000
)
'''

# 2.
'''
def calculate_order(customer, *prices, **options):
    order = {"customer" : customer}
    total_price = 0

    for price in prices:
        total_price = price + total_price

    for key, value in options.items():
        order[key] = value

    if order["add_discount"]:
        total_price = total_price * (1 - (order["discount"]/100))

    if order["add_shipping"]:
        total_price = total_price + order["shipping_fee"]

    order["total_price"] = total_price 
    print(order)



calculate_order(
    "Mushnick's flower shop",
    500,
    50,
    10,
    100,
    discount=25,
    shipping_fee=100,
    add_shipping=True,
    add_discount=True
)
'''

# 3.
'''
# Version with explicit parameters:
def guitar_tuning(transpose, E, A, D, G, B, e):
    tuning = {"E" : E, "A" : A, "D" : D, "G" : G, "B" : B, "e": e}

    for key, value in tuning.items():
        tuning[key] = value + transpose

    print(tuning)

guitar_tuning(transpose=-2, E=82.41, A=110.0, D=146.83, G=196.00, B=246.94, e=329.63)


# Version with **kwargs:
def guitar_tuning(transpose, **kwargs):
    tuning = {}
    
    for key, value in kwargs.items():
        tuning[key] = value + transpose

    print(tuning)

guitar_tuning(transpose=-2, E=82.41, A=110.0, D=146.83, G=196.00, B=246.94, e=329.63)

# COMMENTS:
# In the explicit version it is a bit easier to follow what the program does if you don't have the input at hand i'd say.
# In this case we have 7 parameters, 6 of those are "guitar strings", each of which can be clearly distiguished by the E to e terminology. 
# In that case it might be useful to make that explicit in code too.
# One could of course do a version where the "transpose" parameter is also in **kwargs, that would make it harder to see what is happening.
'''

# 4.
'''
def receipt_printer(**kwargs):
    output = {}
    total_price = 0
    total_string = ""

    for key, value in kwargs.items():
        if type(value) == int or type(value) == float:
            output[key] = value
            total_price = value + total_price
        else:
            output[key] = value
            if total_string == "":
                total_string = value
            else:
                total_string = total_string + ", " + value

    if total_price > 0:
        output["total mathable price"] = total_price

    if total_string != "":
        output["unmathable price summery"] = total_string

    print(f"THE PRICING-SUMMERY OF ASSIGNED OBJECTS AND SUBJECTS IS AS FOLLOWS:\n")

    for key, value in output.items():
        print(key,":", value)
    print("")



receipt_printer()
receipt_printer(book=500, pen=20, car=500000, piano=50000, socks=250, hat=1200)
receipt_printer(book=500, pen=20, car=500000, piano=50000, socks=250, hat=1200, lamp=2000, snoring_partner="sleeplessness", earplugs=10, boat=120000, apartment=5000000, mortgage="worry")
receipt_printer(orangutan="priceless")
'''

# Part F

# 1 - 7

'''
def create_report(title, *sections, **metadata):
    report = {"title" : title}
    sections_list = []
    metadata_dict = {}

    for section in sections:
        sections_list.append(section)

    report["sections"] = sections_list

    for key, value in metadata.items():
        metadata_dict[key] = value

    report["metadata"] = metadata_dict

    return(report) 



def summarize_report(report):
    word_count = count_words(report)
    title = report["title"].upper()
    metadata = dict(report["metadata"].items())
    report_summery = f"\n{title}\n\n"

    for section in report["sections"]:
        report_summery = report_summery + section + "\n\n"

    for key, value in metadata.items():
        value = str(value)
        key = key.replace("_", " ")
        report_summery = report_summery + "\n" + key[0].upper() + key[1:] + " : " + value

    report_summery = report_summery + "\n" + str(word_count)
    return(report_summery)



def count_words(*sections):
    indata = sections[0]["sections"]
    all_strings = sections[0]["title"].lower()
    
    for string in indata:
        all_strings = all_strings + " " + string.lower() + " "

    all_strings = all_strings.split()
    word_count = len(all_strings)
    
    return f"Word count: {word_count}"


    
report1 = create_report("Q2 report", "Markets \nOur CEO taking his pants of on stage seems to have had a slight negative global effect " \
                        "on different actor's long term comittment the market in general, \nand likewise regarding our cause in particular.", 
                        "R&D \nThe experiment of unplugging Sid's bass-rig has been deemed a total success by all stakeholders.", 
                        "Finance \nThe beer money jar have been subject to intervention by one or serveral malicius actor(s). " \
                        "This have negativly affected the quartarly earnings, \nand also the estimated credit risk to possible financiers.", 
                        author="Johnny Rotten", 
                        report_type="Q-report", 
                        version=1.0
                        )

report2 = create_report("Test", "test2", "test3", "test4", "test5", "test6", metatest=10)

report3 = create_report("test")

print(summarize_report(report3))

print(summarize_report(report2))

print(summarize_report(report1))

'''


# Part G

# 1.
'''
def merge_settings (default, **overrides):
    return default, overrides


print(merge_settings(10 , setting1=55, setting2=20))
'''

# 2.
'''
def call_summery(function_name, *args, **kwargs):
    output_string = f"This {function_name} provides you with "
    

    for arg in args:
        output_string += str(arg) + ", "

    output_string += "and "

    for key, value in kwargs.items():
        value = str(value)
        key = key.replace("_", " ")
        if key[-1] == "s":
            output_string += value  + " " + key + ", "
        else:
            output_string += value  + " " + key + "s, "

    output_string += "etc. etc!"
        
    return output_string


print(call_summery("inventory checker", 
                   "outstanding reliability", 
                   "pleasant language", 
                   "pedigree", 
                   settings=20, 
                   day_night_mode=3, 
                   background_options=80))

'''

# 3.
'''
def statistics(*numbers):
    count = 0
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        count += 1

    for number in numbers:
        total += number

    for number in numbers:

        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    avarage = total / count

    return f"Number count: {count}\nTotal: {total}\nAvarage: {avarage}\nMinimum: {minimum}\nMaximum: {maximum}"


print(statistics(-5, -9, -2, -6, -101, -50, -5, -5))
'''

# 4.


'''
print ("\nHi! and welcome to prediction training version 0.00002!" \
" Please predict the outcome of the following 5 examples: \n")


score = 0
answer = 0

def scorer(answer, y):
    global score
    if y == answer:
        score += 1
        return(f"Great work! Score: {score}\n")
    else:
        return(f"Sorry, wrong answer... Score: {score}\n")


print("Question 1(5)\n\n x, y = (5, 6)\n a, b = (6, 5)\n b, a = y, x\n x, y = y, x\n")

x, y = (5, 6)
a, b = (6, 5)
b, a = y, x
x, y = y, x

answer = input("please type the value of y(int): ")
answer = int(answer)

print(scorer(answer, y))
    
print("Question 2(5)\n\n x = \"Superman has returned!\"\n y = x[13] + " " + x[16] + " " + x[5:7] + x[-2]\n y = y.upper()\n")

x = "Superman has returned!"
y = x[13] + " " + x[16] + " " + x[5:7] + x[-2]
y = y.upper()
print(y)

answer = input("please type the value of y: ")
answer = answer

print(scorer(answer, y))


print("Question 3(5)\n\n x = \"4\" + \"4\" + \"4\"\n string = int(x + x)\n y = string\n")

x = "4" + "4" + "4"
string = int(x + x)
y = string

answer = input("please type the value of y(int): ")
answer = int(answer)

print(scorer(answer, y))


print("Question 4(5)\n\n a = [[11]]\n b = [[11]]\n y = len(a) + len(b)\n")

a = [[11]]
b = [[11]]
y = len(a) + len(b)

answer = input("please type the value of y(int): ")
answer = int(answer)

print(scorer(answer, y))


print("Question 5(5)\n\n a = {\"a\" : 4, \"A\" : 3, \"a\" : 5, \"A\" : 2}\n y = a[\"a\"]\n")

a = {"a" : 4, "A" : 3, "a" : 5, "A" : 2}
y = a["a"]

answer = input("please type the value of y(int): ")
answer = int(answer)

print(scorer(answer, y))

'''