# -*- coding: utf-8 -*-

def cube(n):
    """Return the cube of n."""
    return n **3
print(cube(3))

def is_even(n):
    """Return True if n is even, otherwise False."""
    return n % 2 == 0
print(is_even(3))

def is_even(n):
    """Check if n is even without using modulus."""
    return (n // 2) * 2 == n
print(is_even(3))

def is_even(n):
    """Check if n is even using bitwise operator."""
    return (n & 1) == 0
print(is_even(3))

def is_even(n):
    """Return True if n is even, otherwise False."""
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(6))

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    f = c * 9/5 + 32
    return f
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

"""ACSST Lession 2"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"
print(Dog("Fido").make_sound())
print(Cat("Luna").make_sound())
print(Cow("Spot").make_sound())

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def get_animal_sounds(animals):
    return [animal.make_sound() for animal in animals]

print(get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def get_animal_sounds(animals):
    return [animal.make_sound() for animal in animals]

def create_and_get_sounds():
    animals = [
        Dog("Fido"),
        Cat("Luna"),
        Cow("Spot")
    ]
    return [a.make_sound() for a in animals]

print(create_and_get_sounds())
print(get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))
print(create_and_get_sounds() == get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))
print(create_and_get_sounds() == create_and_get_sounds())
print(create_and_get_sounds() is create_and_get_sounds())
print(get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]) == get_animal_sounds([Dog("Fido"), Cat("Luna"), Cow("Spot")]))

import sqlite3

# connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre VARCHAR(50),
    year_published INTEGER
);
""")

conn.commit()
conn.close()

import sqlite3

def create_employee_table() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE employees (
            emp_id INTEGER,
            emp_name TEXT,
            department TEXT,
            salary REAL
        )
    """)
    conn.commit()
    return conn

    # Create table
conn = create_employee_table()
c = conn.cursor()

# Insert some sample data
employees = [
    (1, 'Prabath', 'CS', 90000),
    (2, 'Lilly', 'LS', 80000),
    (3, 'Charlie', 'HR', 55000)
]
c.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)
conn.commit()

# Query and print the results
for row in c.execute("SELECT * FROM employees"):
    print(row)

import sqlite3

def create_books_table() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE books (
            isbn TEXT PRIMARY KEY,
            title TEXT,
            author TEXT
        )
    """)
    conn.commit()
    return conn

import sqlite3

def create_library_db() -> list[tuple]:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    # Create tables
    c.execute("""
        CREATE TABLE authors (
            author_id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    c.execute("""
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
        )
    """)

    # Insert data
    c.executemany("INSERT INTO authors (author_id, name) VALUES (?, ?)", [
        (1, 'George Orwell'),
        (2, 'Jane Austen')
    ])
    c.executemany("INSERT INTO books (book_id, title, author_id) VALUES (?, ?, ?)", [
        (1, '1984', 1),
        (2, 'Animal Farm', 1),
        (3, 'Pride and Prejudice', 2)
    ])

    # Query with JOIN
    c.execute("""
        SELECT books.title, authors.name
        FROM books
        JOIN authors ON books.author_id = authors.author_id
    """)
    return c.fetchall()

"""ACSST Session 4"""

def estimate_vo2(distance_km):
    return round((distance_km * 1000 - 504.9) / 44.73, 1)
print(estimate_vo2(1))

def calculate_trimp(avg_hr, max_hr, duration):

    ratio = avg_hr / max_hr

    trimp = duration * ratio * 0.64 * 2.718 ** (1.92 * ratio)

    return round(trimp, 2)
print(calculate_trimp(150, 190, 60))

def analyze_sprint(splits):
    distances = [10, 20, 30] # meters
    return [round(d / t, 1) for d, t in zip(distances, splits)]
print (analyze_sprint([100, 200, 300]))
print (analyze_sprint([200, 400, 600]))

def assess_risk(weight, height):

    bmi = weight / (height ** 2)

    if bmi < 18.5:

        return "Underweight - High injury risk"

    elif 18.5 <= bmi < 25:

        return "Normal - Low risk"

    else:

        return "Overweight - Moderate risk"
print(assess_risk(70, 1.68))
print(assess_risk(79, 1.78))

def analyze_sprint(splits):
    """
    Given a list of split times (in seconds) for distances [10m, 20m, 30m],
    return a list of average speeds (m/s), rounded to 1 decimal place.
    """
    distances = [10, 20, 30]  # meters
    speeds = []

    for dist, time in zip(distances, splits):
        speed = dist / time
        speeds.append(round(speed, 1))

    return speeds
print(analyze_sprint([1.5,1.2,1,1]))