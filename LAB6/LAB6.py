

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
totalpages = [book.get("pages") for book in booklist]

totalpages = sum(totalpages)
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

# Q == Rewrite a range(len(...)) loop using enumarate and explain why the new version is clearer.

# REVISIT WHEN I FIND ONE!


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
