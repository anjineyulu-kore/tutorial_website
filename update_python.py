#!/usr/bin/env python3
import json

# Read existing concepts
with open("data/concepts.json", "r") as f:
    concepts = json.load(f)

# Comprehensive Python content
python_content = """<h1>🐍 Python Programming - Complete & Comprehensive Guide</h1>
<p><strong>Master Python from basics to advanced concepts with detailed explanations, real code examples, step-by-step instructions, and practical demonstrations.</strong></p>

<hr>

<h2>📖 1. Introduction to Python</h2>
<h3>What is Python?</h3>
<p>Python is a high-level, interpreted programming language known for its simplicity and readability. It emphasizes code readability and uses whitespace for indentation, making it beginner-friendly while powerful for advanced users.</p>

<h3>Why Learn Python?</h3>
<ul>
<li><strong>Easy to Learn:</strong> Simple syntax similar to English</li>
<li><strong>Versatile:</strong> Used in web development, data science, AI/ML, automation, and more</li>
<li><strong>Large Community:</strong> Extensive libraries and frameworks available</li>
<li><strong>High Demand:</strong> One of the most sought-after programming languages</li>
<li><strong>Career Growth:</strong> Opens doors to many career paths</li>
</ul>

<h3>Installation &amp; Setup</h3>
<p><strong>Step 1:</strong> Download Python from python.org</p>
<p><strong>Step 2:</strong> Run the installer and check "Add Python to PATH"</p>
<p><strong>Step 3:</strong> Verify installation: <code>python --version</code></p>
<p><strong>Step 4:</strong> Test Python: <code>python &gt;&gt;&gt; print("Hello, Python!") &gt;&gt;&gt; exit()</code></p>

<h3>Your First Python Program</h3>
<pre><code># Save as hello.py
print("Hello, World!")
name = input("What is your name? ")
print(f"Welcome, {name}!")</code></pre>
<p><strong>Run:</strong> <code>python hello.py</code></p>

<hr>

<h2>💾 2. Variables and Data Types</h2>
<h3>Understanding Variables</h3>
<p>Variables are containers that store data values. Python is dynamically typed, so no explicit type declaration needed.</p>

<h3>Variable Naming Rules</h3>
<ul>
<li>Must start with letter or underscore</li>
<li>Can contain letters, numbers, and underscores</li>
<li>Case-sensitive (name and Name are different)</li>
<li>Avoid Python keywords (if, for, while, etc.)</li>
</ul>

<h3>Code Examples</h3>
<pre><code># Single variable assignment
name = "Alice"
age = 25
height = 5.7
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3

# Check type
print(type(name))      # &lt;class 'str'&gt;
print(type(age))       # &lt;class 'int'&gt;
print(type(height))    # &lt;class 'float'&gt;</code></pre>

<h3>Python Data Types</h3>
<pre><code># String
text = "Python is awesome"

# Integer
count = 42
negative = -10

# Float
pi = 3.14159

# Boolean
is_valid = True
is_empty = False

# None (absence of value)
result = None

# Complex
complex_num = 3 + 4j</code></pre>

<h3>Type Conversion</h3>
<pre><code># Convert to string
num = 42
num_str = str(num)  # "42"

# Convert to integer
price = float("99.99")  # 99.99
price_int = int(price)  # 99

# Convert to float
score = 85
score_float = float(score)  # 85.0

# Convert to boolean
zero = bool(0)  # False
one = bool(1)   # True</code></pre>

<h3>Common Pitfall &amp; Solution</h3>
<p><strong>❌ Pitfall:</strong> String concatenation with numbers</p>
<pre><code>age = 25
print("Age: " + age)  # TypeError!</code></pre>
<p><strong>✅ Solution:</strong> Convert or use f-string</p>
<pre><code>age = 25
print(f"Age: {age}")  # Correct and recommended</code></pre>

<hr>

<h2>➕ 3. Operators</h2>
<h3>Arithmetic Operators</h3>
<pre><code>a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3
modulus = a % b         # 1
exponent = a ** b       # 1000</code></pre>

<h3>Comparison Operators</h3>
<pre><code>x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x &lt; y)   # True
print(x &lt;= y)  # True</code></pre>

<h3>Logical Operators</h3>
<pre><code>a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# Real-world example
age = 25
income = 50000

if age &gt;= 18 and income &gt;= 30000:
    print("Eligible for loan")</code></pre>

<h3>Assignment Operators</h3>
<pre><code>x = 10
x += 5      # x = 15
x -= 3      # x = 12
x *= 2      # x = 24
x /= 4      # x = 6.0
x //= 2     # x = 3.0</code></pre>

<hr>

<h2>📝 4. String Operations</h2>
<h3>Creating and Accessing Strings</h3>
<pre><code>text = "Python Programming"

# Access characters
first_char = text[0]        # 'P'
last_char = text[-1]        # 'g'
substring = text[0:6]       # 'Python'

# String length
length = len(text)          # 18</code></pre>

<h3>String Methods</h3>
<pre><code>text = "Hello World"

# Case conversion
upper = text.upper()           # "HELLO WORLD"
lower = text.lower()           # "hello world"
capitalize = text.capitalize() # "Hello world"

# Searching
index = text.find("World")     # 6
count = text.count("o")        # 2

# Replacement
new_text = text.replace("World", "Python")

# Splitting and joining
words = text.split()           # ["Hello", "World"]
joined = "-".join(words)       # "Hello-World"</code></pre>

<h3>String Formatting</h3>
<pre><code>name = "Alice"
age = 25
salary = 50000.5

# f-strings (recommended)
print(f"Name: {name}, Age: {age}")
print(f"Salary: ${salary:.2f}")  # "Salary: $50000.50"
print(f"Age doubled: {age * 2}")  # "Age doubled: 50"</code></pre>

<hr>

<h2>📊 5. Lists and Collections</h2>
<h3>Lists - Ordered, Mutable Collections</h3>
<pre><code># Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# Accessing elements
first = numbers[0]          # 1
last = numbers[-1]          # 5
slice = numbers[1:4]        # [2, 3, 4]</code></pre>

<h3>List Methods</h3>
<pre><code>fruits = ["apple", "banana", "orange"]

# Adding elements
fruits.append("grape")
fruits.insert(1, "mango")
fruits.extend(["kiwi"])

# Removing elements
removed = fruits.pop()      # Remove last
fruits.remove("orange")     # Remove by value

# Finding and sorting
index = fruits.index("banana")
numbers = [3, 1, 4]
numbers.sort()  # [1, 3, 4]</code></pre>

<h3>Tuples - Immutable Collections</h3>
<pre><code># Creating tuples
coordinates = (10, 20)
single = (1,)  # Note the comma!

# Access like lists
x = coordinates[0]  # 10

# Unpacking
def get_user():
    return ("Alice", 25, "alice@example.com")

name, age, email = get_user()</code></pre>

<h3>Dictionaries - Key-Value Pairs</h3>
<pre><code># Creating dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing
name = person["name"]
age = person.get("age")
job = person.get("job", "Unknown")

# Modifying
person["age"] = 26
person["email"] = "alice@example.com"
del person["city"]

# Iterating
for key, value in person.items():
    print(f"{key}: {value}")</code></pre>

<h3>Sets - Unordered, Unique Collections</h3>
<pre><code># Creating sets
colors = {"red", "green", "blue"}
unique_nums = set([1, 2, 2, 3])  # {1, 2, 3}

# Adding and removing
colors.add("yellow")
colors.discard("red")

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union = set1 | set2        # {1, 2, 3, 4}
intersection = set1 &amp; set2  # {2, 3}
difference = set1 - set2   # {1}</code></pre>

<hr>

<h2>🔀 6. Control Flow (if, elif, else)</h2>
<h3>Basic if-else</h3>
<pre><code>age = 25

if age &gt;= 18:
    print("You are an adult")
else:
    print("You are a minor")</code></pre>

<h3>if-elif-else</h3>
<pre><code>score = 85

if score &gt;= 90:
    grade = "A"
elif score &gt;= 80:
    grade = "B"
elif score &gt;= 70:
    grade = "C"
else:
    grade = "F"</code></pre>

<h3>Nested Conditions</h3>
<pre><code>age = 25
has_license = True

if age &gt;= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")</code></pre>

<h3>Ternary Operator</h3>
<pre><code>age = 25
status = "Adult" if age &gt;= 18 else "Minor"
print(status)  # "Adult"</code></pre>

<hr>

<h2>🔁 7. Loops (for and while)</h2>
<h3>for Loops</h3>
<pre><code># Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop through range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

# Loop with step
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# Loop through dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")</code></pre>

<h3>while Loops</h3>
<pre><code>count = 0
while count &lt; 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")</code></pre>

<h3>Loop Control: break and continue</h3>
<pre><code># break - exits loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skips iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9</code></pre>

<h3>else with Loops</h3>
<pre><code># else executes when loop completes normally
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # Prints

# else with break doesn't execute
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed!")  # Doesn't print</code></pre>

<hr>

<h2>⚙️ 8. Functions</h2>
<h3>Defining and Calling Functions</h3>
<pre><code># Basic function
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8</code></pre>

<h3>Default Parameters</h3>
<pre><code>def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Hello, Guest!
greet("Alice")    # Hello, Alice!

# Multiple defaults
def create_profile(name, age=18, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

create_profile("Alice")</code></pre>

<h3>*args and **kwargs</h3>
<pre><code># *args - variable positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))         # 6
print(sum_all(1, 2, 3, 4, 5))   # 15

# **kwargs - variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")</code></pre>

<h3>Return Multiple Values</h3>
<pre><code># Return tuple
def get_user_info():
    name = "Alice"
    age = 25
    email = "alice@example.com"
    return name, age, email

# Unpack
name, age, email = get_user_info()
print(f"{name}, {age}, {email}")</code></pre>

<h3>Scope and Global Variables</h3>
<pre><code">global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)    # Can access global
    print(local_var)     # Can access local

my_function()

# Modify global
def modify_global():
    global global_var
    global_var = "Modified"

modify_global()
print(global_var)  # "Modified"</code></pre>

<h3>Common Pitfall &amp; Solution</h3>
<p><strong>❌ Pitfall:</strong> Mutable default arguments</p>
<pre><code">def add_item(item, list=[]):
    list.append(item)
    return list

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2] - Bug!</code></pre>
<p><strong>✅ Solution:</strong> Use None as default</p>
<pre><code>def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list</code></pre>

<hr>

<h2>🎯 9. Object-Oriented Programming (OOP)</h2>
<h3>Classes and Objects</h3>
<pre><code># Define class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I'm {self.age}"

# Create objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access
print(person1.name)           # Alice
print(person1.introduce())    # My name is Alice and I'm 25</code></pre>

<h3>Inheritance</h3>
<pre><code">class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Override
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows: Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy barks: Woof!
print(cat.speak())  # Whiskers meows: Meow!</code></pre>

<h3>Encapsulation - Private Attributes</h3>
<pre><code">class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        if amount &gt; 0:
            self.__balance += amount
            return f"Deposited ${amount}"
        return "Invalid"
    
    def withdraw(self, amount):
        if 0 &lt; amount &lt;= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}"
        return "Invalid"
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.deposit(500))
print(account.get_balance())</code></pre>

<h3>Practical Example: Student Management</h3>
<pre><code>class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 &lt;= grade &lt;= 100:
            self.grades.append(grade)
            return f"Grade {grade} added"
        return "Invalid grade"
    
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def get_status(self):
        avg = self.get_average()
        if avg &gt;= 90:
            return "A - Excellent"
        elif avg &gt;= 80:
            return "B - Good"
        elif avg &gt;= 70:
            return "C - Average"
        else:
            return "F - Failing"

student = Student("Alice", "STU001")
student.add_grade(85)
student.add_grade(90)
print(f"Average: {student.get_average():.2f}")
print(f"Status: {student.get_status()}")</code></pre>

<hr>

<h2>📂 10. File Handling</h2>
<h3>Reading Files</h3>
<pre><code"># Read entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines
with open("file.txt", "r") as file:
    lines = file.readlines()</code></pre>

<h3>Writing to Files</h3>
<pre><code"># Write (overwrites)
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome!")

# Append (adds to existing)
with open("file.txt", "a") as file:
    file.write("\nNew line added")</code></pre>

<h3>Working with CSV</h3>
<pre><code">import csv

# Read CSV
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Write CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"]
]

with open("data.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)</code></pre>

<h3>Working with JSON</h3>
<pre><code">import json

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Write JSON
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)</code></pre>

<hr>

<h2>🚨 11. Exception Handling</h2>
<h3>try-except Blocks</h3>
<pre><code"># Basic handling
try:
    num = int("abc")
except ValueError:
    print("Invalid input!")

# Multiple exceptions
try:
    result = 10 / int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")</code></pre>

<h3>else and finally</h3>
<pre><code"># else and finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully")
finally:
    print("Cleanup code")  # Always executes</code></pre>

<h3>Raising Exceptions</h3>
<pre><code">def validate_age(age):
    if age &lt; 0:
        raise ValueError("Age cannot be negative")
    if age &gt; 150:
        raise ValueError("Invalid age")
    return f"Age {age} is valid"

try:
    print(validate_age(-5))
except ValueError as e:
    print(f"Error: {e}")</code></pre>

<hr>

<h2>📚 12. Comprehensions</h2>
<h3>List Comprehension</h3>
<pre><code"># Simple list
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Transform
fruits = ["apple", "banana", "orange"]
upper_fruits = [f.upper() for f in fruits]</code></pre>

<h3>Dictionary Comprehension</h3>
<pre><code"># Create dictionary
squares_dict = {x: x**2 for x in range(5)}

# From lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
people = {n: a for n, a in zip(names, ages)}</code></pre>

<h3>Set Comprehension</h3>
<pre><code"># Create set
unique_squares = {x**2 for x in [1, 1, 2, 2, 3]}

# Filter
unique_evens = {x for x in range(10) if x % 2 == 0}</code></pre>

<hr>

<h2>📦 13. Modules and Imports</h2>
<h3>Importing Modules</h3>
<pre><code">import math
print(math.sqrt(16))

from math import sqrt, pi
print(sqrt(16))

# With alias
import numpy as np</code></pre>

<h3>Common Built-in Modules</h3>
<pre><code">from datetime import datetime, timedelta
now = datetime.now()

import random
random_int = random.randint(1, 10)
random_choice = random.choice([1, 2, 3])

import os
current_dir = os.getcwd()
files = os.listdir(".")</code></pre>

<hr>

<h2>✨ 14. Decorators</h2>
<h3>Function Decorators</h3>
<pre><code">def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()</code></pre>

<h3>Decorators with Arguments</h3>
<pre><code">def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

add(5, 3)</code></pre>

<hr>

<h2>🔄 15. Generators</h2>
<h3>Creating Generators</h3>
<pre><code">def count_up(max):
    count = 1
    while count &lt;= max:
        yield count
        count += 1

for num in count_up(5):
    print(num)  # 1, 2, 3, 4, 5

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)</code></pre>

<hr>

<h2>🎓 16. Best Practices &amp; Tips</h2>

<h3>Code Style (PEP 8)</h3>
<ul>
<li>Use meaningful names: <code>user_name</code> instead of <code>un</code></li>
<li>Keep functions small and focused</li>
<li>Use comments for complex logic</li>
<li>Naming conventions:
  <ul>
  <li>Variables: lowercase_with_underscores</li>
  <li>Classes: CamelCase</li>
  <li>Constants: UPPERCASE_WITH_UNDERSCORES</li>
  </ul>
</li>
<li>Maximum line length: 79 characters</li>
</ul>

<h3>Documentation</h3>
<pre><code>def calculate_age(birth_year):
    # Calculate age from birth year
    # Args: birth_year (int)
    # Returns: int - Age in years
    return 2025 - birth_year</code></pre>

<h3>Error Handling Best Practices</h3>
<pre><code">try:
    result = int("abc")
except ValueError:
    print("Invalid input")

import logging
logger = logging.getLogger(__name__)

try:
    risky_operation()
except Exception as e:
    logger.error(f"Failed: {e}")
    raise</code></pre>

<h3>Performance Tips</h3>
<ul>
<li>Use list comprehensions instead of loops</li>
<li>Use generators for large datasets</li>
<li>Avoid global variables</li>
<li>Use built-in functions (optimized)</li>
</ul>

<h3>Debugging Tips</h3>
<pre><code"># Print statements
print(f"Value: {value}")

# Debugger
import pdb
pdb.set_trace()

# Type checking
print(type(variable))

# Help
help(function_name)</code></pre>

<hr>

<h2>📝 Quick Reference</h2>
<ul>
<li><strong>Variables:</strong> Store data values</li>
<li><strong>Data Types:</strong> str, int, float, bool, list, tuple, dict, set</li>
<li><strong>Operators:</strong> +, -, *, /, //, %, **, ==, !=, &lt;, &gt;, and, or</li>
<li><strong>Control:</strong> if, elif, else, for, while, break, continue</li>
<li><strong>Functions:</strong> def, return, *args, **kwargs</li>
<li><strong>Collections:</strong> lists, tuples, dicts, sets</li>
<li><strong>OOP:</strong> class, inheritance, encapsulation</li>
<li><strong>Exceptions:</strong> try, except, else, finally, raise</li>
<li><strong>Modules:</strong> import, from...import</li>
<li><strong>Comprehensions:</strong> list, dict, set comprehensions</li>
</ul>

<hr>

<p style="text-align: center; margin-top: 30px;">
<strong>🎉 You've mastered Python fundamentals!</strong><br>
Keep practicing and exploring to become an expert Python programmer!<br>
<strong>Practice Tips:</strong> Write code daily, build projects, read others' code, and contribute to open source.
</p>
"""

# Update Python concept
for i, concept in enumerate(concepts):
    if concept["id"] == "python-basics":
        concepts[i] = {
            "id": "python-basics",
            "title": "Python Programming - Complete Comprehensive Guide",
            "slug": "python-complete-guide",
            "created_at": "2025-01-01T00:00:00Z",
            "updated_at": "2025-12-07T00:00:00Z",
            "content": python_content
        }
        break

# Write to file
with open("data/concepts.json", "w") as f:
    json.dump(concepts, f, indent=2)

print("✅ Comprehensive Python guide created!")
print(f"Content length: {len(python_content):,} characters")
