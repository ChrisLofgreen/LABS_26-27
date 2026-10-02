

# PART A

# 1.
'''
numbers = list(range(1,21))

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


squares = [number ** 2 for number in numbers]

print(squares)
'''

# 2.
'''
even_numbers = list(range(2,101, 2))

print(even_numbers)

# OR

numbers = list(range(1,101))

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
'''
# 3.
'''
names = ["  glenn", "peter", "ann ", "patricia  "]
stripped = [name.strip() for name in names]
fixed_names = [name[0].upper() + name[1:] for name in stripped]

print(fixed_names)
'''

# 4.
'''
scores = [89, 95, 20, 75]

passing_scores = [number for number in scores if number >= 70]

print(passing_scores)
'''

# 5.
'''
scores = [89, 95, 20, 75]

pass_fail_scores = {number: ("PASS" if number >= 70 else "FAIL") for number in scores}

print(pass_fail_scores)
'''

# 6.1


'''
inventory = [
    {"i_number" : 0,
     "prodname" : "prod1",
     "stock" : 52 
    },
    {"i_number" : 1,
     "prodname" : "prod2",
     "stock" : 4 
    },
    {"i_number" : 2,
     "prodname" : "prod3",
     "stock" : 10 
    },
    {"i_number" : 3,
     "prodname" : "prod4",
     "stock" : 5 
    },
    {"i_number" : 4,
     "prodname" : "prod5",
     "stock" : 3 
    }
]

# OLD VERSION
totalstock = []
for i in inventory:
    totalstock.append(i.get("stock"))

print(sum(totalstock))

# NEW VERSION
totalstock = [(value.get("stock")) for value in inventory]

print(sum(totalstock))

'''

# 6.2

'''
words = ["ape", "orangutan", "pig", "dog", "anaconda"]
above5 = 0

# OLD VERSION
for word in words:
    if len(word)> 5:
        above5 += 1

print(above5)

# NEW VERSION
above5_list = [(1 if len(word) > 5 else 0) for word in words]
above5 = sum(above5_list)

print(above5)
'''

# I prefer the old one here :)


# 6.3
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

# OLD VERSION
totalpages = []
for b in booklist:
    totalpages.append(b.get("pages"))
print(sum(totalpages))


# NEW VERSION
totalpages = sum([book.get("pages") for book in booklist])

print(totalpages)
'''

# PART B

# 1.
'''
numbers = list(range(1,11))

squares = {number : number ** 2 for number in numbers}

print(squares)
'''
# 2.
'''
words = ["Hey", "Ho", "Lets", "Go"]

lenght = {word : len(word) for word in words}

print(lenght)
'''

# 3.
'''
words = ["Hey", "Ho", "Lets", "Go", "Hey", "Go"]

no_dupes = {word.lower() for word in words}

print(no_dupes)
'''

# 4.
'''
booklist = [
    {"title": "brave new world", "author": "Aldous Huxley", "price" : 525, "genre": "fiction", "year" : 1946},
    {"title": "1984", "author": "George Orwell", "price" : 480, "genre": "fiction", "year" : 1944},
    {"title": "the angel of darkness", "author": "Caleb Carr", "price" : 625, "genre": "fiction", "year" : 1999},
    {"title": "the trial", "author": "Franz Kafka", "price" : 270, "genre": "fiction", "year" : 1951},
    {"title": "the transformation", "author": "Franz Kafka", "price" : 70, "genre": "fiction", "year" : 1946},
    {"title": "problems of knowledge", "author": "Michael Williams", "price" : 200, "genre": "non fiction", "year" : 2011},
    {"title": "the principles of morals", "author": "David Hume", "price" : 260, "genre": "non fiction", "year" : 1751},
    {"title": "group dynamics", "author": "Donelson R. Forsyth", "price" : 667, "genre": "non fiction", "year" : 2012},
    {"title": "business reseach methods", "author": "Emma Bell", "price" : 600, "genre": "non fiction", "year" : 2018}
    ]

below_500 = {book.get("title"):
             book.get("price")
             for book in booklist 
             if book.get("price") < 500}

print(below_500)
'''

# 5.
'''
student_list = [
    {"name": "Lisa",
     "score": 97}, 
     {"name": "Uno",
      "score": 1},
      {"name": "Bart",
       "score": 25},
       {"name": "Milhouse",
        "score": 75}
]

pass_fail = {student.get("name"): 
             ("PASS" if student.get("score") >= 70 else "FAIL")
             for student in student_list}

print(pass_fail)
'''

# PART C

# 1.
'''
playlist = ["Song1", "Song2", "Song3", "Song4", "Song5"]

for index, song in enumerate(playlist, 1):
    print(index,": ", song)

# We did this one before but it is now slightly improved with the "Index + 1" within enumarate instead of a beginner workaround :)
'''

# 2.
'''
tasks = ["clean house", "wash car", "feed dinosaur", "write song"]

for index, task in enumerate(tasks, 1):
    print (f"Task {index}: {task}")
'''

# 3.
'''
tasks = ["clean house", "wash car", "feed dinosaur", "write song", "cut grass"]
threshold = 3

for index, task in enumerate(tasks, 1):
    if index > threshold:
        print (f"Task {index}: {task}")
'''

# 4.
'''
numbers = [9, 5, 8, 3, 1, 4, 6, 4]

# range(len()):

for index in range(len(numbers)):
    outnum = numbers[index]
    print(index, "-", outnum)

# enumerate()

for index, number in enumerate(numbers):
    print(index, "-", number)


# I guess it's just clearer what it does, easier to follow. Maybe it is therelationship between the index and the other variable
# that becomes is more obvious to me at least, combined with the lack of that extra step.
# I was taught enumerate from the beginning so for me it is the choice for this kind of thing. 

'''

# PART D

# 1.
'''
student = ["Glenn", "Peter", "Ann", "Patricia"]

score = [48, 70, 82, 75]

for student, score in zip(student, score):
    print(student, score)
'''

# 2.

'''
student = ["Glenn", "Peter", "Ann", "Patricia"]

score = [48, 70, 82, 75]

student_score = dict(zip(student, score))

print(student_score)
'''

# 3.
'''
product_name = ["Magnolia", "Rose", "Oak-tree", "Pine"]
price = [65, 35, 3500, 4000]
stock = [58, 65, 5, 2]

for product_name, price, stock in zip(product_name, price, stock):
    print(product_name, price, stock)
'''
# 4.
'''
product_name = ["Magnolia", "Rose", "Oak-tree", "Pine", "Maple"]
price = [65, 35, 3500, 4000]

for product_name, price in zip(product_name, price):
    print(product_name, price)
'''
# zip stops "zipping" when the shortest list is exhausted

# 5.
'''
student = ["Glenn", "Peter", "Ann", "Patricia"]

score = [48, 70, 82, 75]

for student, score in zip(student, score):
    print(student)
    print(score)
'''

# 6.
'''
x, y = (5, 6)
print(x, y)

x, y = y, x
print(x, y)
'''

# PART E

# 1.
'''
words = ["Magnolia", "Rose", "Oak-tree", "Pine", "Maple"]

sorted_words = sorted(words,key=len)

print(sorted_words)
'''

# 2.
'''
student_list = [
    {"name": "Lisa",
     "score": 97}, 
     {"name": "Uno",
      "score": 1},
      {"name": "Bart",
       "score": 25},
       {"name": "Milhouse",
        "score": 75}
]


student_list_acending = sorted(
    student_list,
    key=lambda student:student["score"])

print(student_list_acending)

student_list_decending = sorted(
    student_list,
    key=lambda student:student["score"], reverse=True)

print(student_list_decending)
'''

# 3.
'''
booklist = [
    {"title": "brave new world", "author": "Aldous Huxley", "price" : 525, "genre": "fiction", "year" : 1946},
    {"title": "1984", "author": "George Orwell", "price" : 480, "genre": "fiction", "year" : 1944},
    {"title": "the angel of darkness", "author": "Caleb Carr", "price" : 625, "genre": "fiction", "year" : 1999},
    {"title": "the trial", "author": "Franz Kafka", "price" : 270, "genre": "fiction", "year" : 1951},
    {"title": "the transformation", "author": "Franz Kafka", "price" : 70, "genre": "fiction", "year" : 1946},
    {"title": "problems of knowledge", "author": "Michael Williams", "price" : 200, "genre": "non fiction", "year" : 2011},
    {"title": "the principles of morals", "author": "David Hume", "price" : 260, "genre": "non fiction", "year" : 1751},
    {"title": "group dynamics", "author": "Donelson R. Forsyth", "price" : 667, "genre": "non fiction", "year" : 2012},
    {"title": "business reseach methods", "author": "Emma Bell", "price" : 600, "genre": "non fiction", "year" : 2018}
    ]

sorted_booklist = sorted(
    booklist,
    key=lambda book:book["price"]
)

for book in sorted_booklist:
    print (book["title"],":", book["price"])
'''

# 4.
'''
booklist = [
    {"first_name" : "Aldous", "last_name" : "Huxley"},
    {"first_name" : "George", "last_name" : "Orwell"},
    {"first_name" : "Caleb", "last_name" : "Carr"},
    {"first_name" : "Franz", "last_name" : "Kafka"},
    {"first_name" : "Michael", "last_name" : "Williams"},
    {"first_name" : "David", "last_name" : "Hume"},
    {"first_name" : "Emma", "last_name" : "Bell"}
    ]

sorted_booklist = sorted(
    booklist,
    key=lambda lastname:lastname["last_name"]
)

print(sorted_booklist)
'''

# 5.


'''
words = ["Glenn", "Peter", "Ann", "Patricia"]

words_sorted = sorted(words,key=lambda word:len(word))

print(words_sorted)


words = ["Glenn", "Peter", "Ann", "Patricia"]

def lenght_key(word):
    return len(word)

words_sorted = sorted(words,key=lenght_key)

print(words_sorted)
'''




# Part F
'''
# 1.
booklist = [
    {"title": "brave   new world", "price" : 525, "stock" : 0},
    {"title": "1984  ", "price" : 480, "stock" : 5},
    {"title": "the angel of   darkness", "price" : 625, "stock" : 19},
    {"title": "the trial"  , "price" : 270, "stock" : 0},
    {"title": "the transformation", "price" : 70, "stock" : 1},
    {"title": "Problems of knowledge", "price" : 200, "stock" : 2},
    {"title": "the principles of morals", "price" : 260, "stock" : 0},
    {"title": "  group dynamics", "price" : 667, "stock" : 12},
    {"title": "business reseach methods", "price" : 600, "stock" : 10},
    {"title": "the sublime    object of ideology", "price" : 300, "stock" : 22},
    {"title": "reasonS  and persons", "price" : 500, "stock" : 0},
    {"title": "meTaphysics  ", "price" : 423, "stock" : 4}
    ]

# 2.

c_booklist = []

for book in booklist:
    book["title"] = book["title"].strip()
    book["title"] = book["title"].lower()
    if "  " or "   " in book["title"]:
        book["title"] = book["title"].replace("   ", " ")
        book["title"] = book["title"].replace("  ", " ")

    c_booklist.append(book)
# 3.
in_stock = [{book.get("title"):
            book.get("stock")
            for book in booklist 
            if book.get("stock") > 0}]

# 4.
categories = {"philosophy", "fiction", "reseach"}

# 5.
stock_value = {book["title"]: book["price"] * book["stock"]
               for book in booklist}

# 6.
sorted_value = sorted(
    booklist,
    key=lambda book:book["price"] * book["stock"], reverse=True
)
# 7.
#for index, book in enumerate(sorted_value, start=1):
    #print(index, book)

# 8.

stock_value = [stock_value]

#for book, book in zip(booklist, stock_value):
#    print (book)

'''

# 9.

'''
complicated = [
    number
    for numbers in [range(1, 101)]
    for number in numbers
    if any(number % value == 0 for value in [2])]

simple = [number for number in range(1, 101) 
          if number % 2 == 0]

print(simple)
print(complicated)
'''

# I guess this one is a bit too far out. But i guess: no nested comprehensions if not needed. And if there is a simpler way to calculate
# the thing, do that.


# Part G

# 1.
'''
list_of_lists = [[1, 2], [3, 4], [5, 6]]

list1 = [value for lists in list_of_lists for value in lists]

print(list1)
'''
# 2.
'''
multitable = [[v1 * v2 for v1 in range(1, 10)]
              for v2 in range(1, 10)]

print(multitable)

# Is it readable enough? Hard to say, a tentative... yes!?
# I have to underscore that i am new to reading (and writing) comprehentions, so read into that what you will. Ask me in two weeks :)
# The output could be prettier though I must say.
'''

# 3. 
'''
students = ["Glenn", "Peter", "Ann", "Patricia"]

scores = [48, 68, 82, 75]

passing_students = {student:score for student, score in zip(students, scores)
                    if score >= 70}

print (passing_students)
'''
# 4.
'''
scores = [45, 12, 65, 86]

counter = 0
for score in scores:
    if score != 0:
        counter += 1

if counter > 0:
    print(True)
else:
    print(False)

counter = 0
for score in scores:
    if score == 0:
        continue
    else:
        counter += 1

if counter == len(scores):
    print(True)
else:
    print(False)


print (any(scores)) # Are there any valid scores (not zero)

print (all(scores)) # Are all scores valid (not zero)
'''

# 5.

#one = [number for number in range(1, 101) 
#       if number % 2 == 0]

# I think this one is quite clean


#x, y = 1, 2
#x, y = y, x

# I dont know if its only Pyhon, but I can think of places where swapping is really good

#any()

#all()

# As shown in the prevous question...

# sorted() 
# this is crazy powerful. and strips away a whole lot of nonsense I can imagine