
# Part A

# 1.
""" 
languages = ["Python", "Java", "JavaScript", "R", "C", "C#", "C++", "Rust"]
print(languages[0])
print(languages[-1])
print(languages[2])
print(languages[-2])
 """
# 2.
""" 
languages = ["Python", "Java", "JavaScript", "R", "C", "C#", "C++", "Rust"]
print(languages[1:3])
print(languages[3:5])
print(languages[5:])
print(languages[::-1])
 """
# 3.
""" 
languages = ["Python", "Java", "JavaScript", "R", "C", "C#", "C++", "Rust"]
languages.append("test")
print(languages)
languages.insert(0, "test2")
print(languages)
languages.remove("test")
print(languages)
residual = languages.pop(0)

print(languages)
print(residual)
 """

# 4.
""" 
nums = [1, 2, 5, 4, 8]

print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))
 """

# 5.
""" 
nums = [1, 2, 5, 4, 8]

nums_s = sorted(nums) # Sorted returns a new list wheras sort changes the old one
nums.sort

print(nums_s)
print(nums)
nums.reverse()
print(nums)
 """

# 6.
""" 
nums_a = [1, 2, 5, 4, 8]

nums_b = nums_a
nums_b.append(4) #append also happens to nums_a

print(nums_a)
print(nums_b)

nums_a = [1, 2, 5, 4, 8]

nums_b = nums_a.copy()
nums_b.append(5)

print(nums_a)
print(nums_b)
 """


# Part B

# 1.
""" 
rgb = (155, 20, 255)
r, g, b = rgb

print(r)
print(g)
print(b)
 """

# 2.
""" 
person = ("Chris", 42, "STHLM")
name, age, city = person

print(name)
print(age)
print(city)
 """

# 3.

# Tuples are immutable so you can't just assign a value in them, this makes them useful for showing that something should not be changed.

# 4.
'''
coordinates = [
    (10, 20),
    (50, 80),
    (100, 50),
    (20, 50)
]

x = coordinates[1][0]
y = coordinates[1][1]

print(x)
print(y)
'''


# Part C

# 1.
""" 
course_names = ["Py1", "Py2", "Py3", "Py1", "Py1"]

print(len(course_names))

course_names = set(course_names)

print(len(course_names))
 """

# 2.
""" 
dev1 = {"C", "C++", "C#", "Python"}
dev2 = {"C#", "Python", "Java"}

print(dev1 & dev2) # shared
print(dev1 - dev2) # only first
print(dev1 | dev2) # either one (union)
 """

# 3.
""" 
set1 = {"C", "C++", "C#", "Python"}

set1.remove("C")
print(set1)
set1.add("C")
print(set1)
print("C" in set1)
print("Beaver" in set1)
 """

# 4.

# If we have a system that need unique usernames but usernames are created remotly by the users. That would be a good case.


# Part D

# 1.
"""  
lap1 = {"brand" : "Dell", "model" : "XPS", "RAM" : "32GB", "storage" : "2TB", "price" : 3000}

print(lap1.get("brand"))
print(lap1.get("model"))
print(lap1.get("RAM"))
print(lap1.get("storage"))
print(lap1.get("price"))
# 2.
lap1["price"] = 3500
lap1["OS"] = "win95"
print(lap1.get("price"))
print(lap1.get("OS"))

del lap1["model"]
print(lap1.keys())
# 3.
print(lap1.get("OS"))
print(lap1.get("model")) # since we removed "model" this returns None where as an indexing error would halt the program
# 4.
print(lap1.keys())
print(lap1.values())
print(lap1.items())
 """
# 5.
""" 
courses = {"Py1" : 100, "Py2" : 50, "Py3" : 200, "Py4" : 300, "Py5" : 1000}

print(sum(courses.values()))
 """

# Part E

# 1.
""" 
booklist = [
    {"title": "brave new world", "author": "Aldous Huxley", "pages" : 525, "available": True},
    {"title": "1984", "author": "George Orwell", "pages" : 480, "available": True},
    {"title": "the angel of darkness", "author": "Caleb Carr", "pages" : 625, "available": True},
    {"title": "the trial", "author": "Franz Kafka", "pages" : 270, "available": True},
    {"title": "the transformation", "author": "Franz Kafka", "pages" : 70, "available": True}
    ]

# 2.

print(booklist[2]["title"])
print(booklist[-1]["available"])

# 3.

booklist[4]["available"] = False
print(booklist)

booklist[4]["Good?"] = True
print(booklist)
 """

# 4.
"""  
employees = {"sales" : ["George", "Glen", "Tina"], "production" : ["Lisa", "Jörgen", "Ishmail"]}
print(employees)
 """
# 5.
""" 
courses = [
    {"name" : "Py1",
     "teacher" : "Aladdin",
     "topics" : ["data types", "operators"]
     },
     {"name" : "Py2",
      "teacher" : "Haithem",
      "topics" : ["collections", "variables"]
      }, 
      {"name" : "Py3",
       "teacher" : "Aladdin",
       "topics" : ["loops", "OOP"]
       }
]

print(courses[0]["topics"][0])
 """

# Part F

# 1 - 2
""" 
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
 """
# 3.
""" 
genre = []

for books in booklist:
    genre.append(books.get("genre"))

genre = set(genre)

print(genre)
 """
# 4.
""" 
years = []

for books in booklist:
    title = books.get("title")
    year =  books.get("year")

    years.append((title, year))

print(years)
 """ 

# 5.
""" 
print(booklist[0]["author"])
print(booklist[0]["title"])
print(len(booklist))

totalpages = []
for b in booklist:
    totalpages.append(b.get("pages"))
print(sum(totalpages))

booklist[0]["year"] = 1945
print(booklist[0]["year"])

alltitles = []
for b in booklist:
    alltitles.append(b.get("title"))
print(alltitles)

newbook = {"title": "test", "author": "Herr Test", "pages" : 2, "genre": "fiction", "year" : 2026}
booklist.insert(3, newbook)

removed = booklist.pop(3)
print(booklist)
print(removed)

print("We have:")
for books in booklist:
    print(f"{books.get("title", 0)}, {books.get("pages", 0)} pages")

booklist2 = booklist + booklist
print(booklist2)

book1 = booklist[0]
del book1["year"]
print(book1)
 """

# 6.
""" 
print(f"{booklist[0]["author"]} - {booklist[0]["title"]}")
print(f"{booklist[1]["author"]} - {booklist[1]["title"]}")
print(f"{booklist[2]["author"]} - {booklist[2]["title"]}")
print(f"{booklist[3]["author"]} - {booklist[3]["title"]}")
print(f"{booklist[4]["author"]} - {booklist[4]["title"]}")
print(f"{booklist[5]["author"]} - {booklist[5]["title"]}")
print(f"{booklist[6]["author"]} - {booklist[6]["title"]}")
print(f"{booklist[7]["author"]} - {booklist[7]["title"]}")
print(f"{booklist[8]["author"]} - {booklist[8]["title"]}")
 """

# Part G

# 1.
"""  
list_a = ["apan1", "bison99", "flojten"]
list_b = ["apan1", "maktor12", "jens94"]

list_c = list_a + list_b
duplicates = set(list_a) & set(list_b)
unique = set(list_c) - duplicates

print(duplicates)
print(unique)
 """


# 2.
""" 
course_platform = [
    {"courses" : ["literature1"],
     "teacher" : "teacher1",
     "students" : ["Ann", "Bjorn", "Camilla"],
     "topics" : ["classic", "modern", "post-modern"]
    },
    {"courses" : ["literature2"],
     "teacher" : "teacher2",
     "students" : ["Axl", "Bella", "Cecilia"],
     "topics" : ["poetry", "lyrics"]
    }
]

print(course_platform)
 """

# 3.
""" 
inventory = [
    {"i_number" : 0,
     "prodname" : "prod1",
     "stock" : 2 
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

inventory[0]["stock"] = 52
totalstock = []
for i in inventory:
    totalstock.append(i.get("stock"))

print(sum(totalstock))
 """

# 4.

# lists are good for when things need to be indexed and changed, works very well to nest dicts into.
# tuples are immutable and are therefore useful when data should not be changed. Heavily used to store multivariate data in embedded systems.
# sets are useful when duplicates are not allowed.
# dicts are useful for searchability among other things, since they rely on keys rather than indexation. 
# There can be a lot of information connected to a key easily avalible for search in dicts.


list1 = ["1", "2", "3"]

residual = list1.pop(1)

print(residual)