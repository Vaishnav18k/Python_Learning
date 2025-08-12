# Data Types in python
# Integer Whole numbers, positive or negative.
age = 25
temperature = -2
print(age)
print(temperature)
# print(type(temperature))

name = "Alice"
greeting = "Hi newbie"
print(name)

print(greeting)

""" Multiline command
print(type(name))
print(type(greeting))
"""

name="hello world"
print(name.upper())

# List Ordered, changeable (mutable) collection, allows duplicates.
fruits = ["apple","banana","cherry"]
print(fruits[1])
print(fruits[0:2])
fruits.append("strawberry")
print(fruits)
fruits.remove("cherry")
print(fruits)

# Tuple Ordered, unchangeable (immutable) collection, allows duplicates.

coordinates = (10,20)
print(coordinates)
print(coordinates[1])

# Dict 
person = {
    "name": "Harish",
    "age":22,
    "city": "Chennai"
}
print(person)
print(person["name"],person["age"])

person.update({"gender":"male"})
print(person)

print(person.get("age"))


# Set Unordered, unchangeable (immutable) collection, does not allow duplicates.
unique_numbers= {1,2,3,4,5,1,3,4}
print(unique_numbers)

# Operator Arithmatic

a=10
b=3
c=a+b
print(c)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# Operator Relational
x=10
y=3
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)


# Logical Operator
# And Or Not 

age=25
# age=15
age_verified = True
can_watch_coolie =(age>=18) and age_verified 
print(can_watch_coolie)

can_watch_coolie = (age>=18) or age_verified
print(can_watch_coolie)

can_watch_coolie =(age<18) or not age_verified
print(can_watch_coolie)
