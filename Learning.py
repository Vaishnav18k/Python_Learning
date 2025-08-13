a=6
b=5
print((a**2)+(b**2)+(2*a*b))

fruits = ['mango', 'orange','pineapple']
print(fruits)

fruits.append("banana")
print(fruits)

fruits.insert(1,'grapes')
print(fruits)

fruits.remove('banana')
print(fruits)

del(fruits[0])
print(fruits)

fruits.append(['icherry','iberry'])
print(fruits)

fruits.extend(['cherry','berry'])
print(fruits)

fruits.extend(['apple'])
print(fruits)

print(fruits[3][0]) 

# Tuple
fruit =  ('mango', 'orange','pineapple','apricot')
print(fruit)

# fruit.insert(1,'grapes')
# print(fruit)
# 'tuple' object has no attribute 'insert'

# fruit.extend('apple')
# print(fruit)
# tuple' object has no attribute 'extend'

# fruit.remove('mango')
# print(fruit)

# fruit.remove([0])
# print(fruit)
# 'tuple' object has no attribute 'remove'

# fruit.append('apple')
# print(fruit)
# tuple' object has no attribute 'append'  

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:7])
print(numbers[2:7:2]) # jumps with 2 interval
print(numbers[:7])
print(numbers[2:])
print(numbers[:])
print(numbers[::2])
print(numbers[-2])
print(numbers[2])
print(numbers[-2-6])
print(numbers[6:2])
print(numbers[-6:-2])
print(numbers[::-1])


data = {
"name":"john",
"age":25,
'subject':['Tamil','English','Maths']    
}
print(data)

print(data['age'])
print(data['name'])
print(data['subject'][1])
print(data['subject'][0])

data['city']='chennai'
print(data)

del (data['subject'][2])
print(data)


name='Rahul'
age=25
city='Chennai'

print(name + " is " +  str(age) + " years old guy from " + city)
print("{0} is {1} years old guy from {2}".format(name,age,city))
print(F"{name} is {age} years old guy from {city}")

print("John's car")
print("John\'s car")