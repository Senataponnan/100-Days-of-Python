print("Hello World") 

name=input("what is your name ?")

name_count = len(name)

print(f'THE "{name}" has "{name_count}" letters')


a = input('a:')
b = input('b:')

c = a
a = b
b = c 

print( a, b)


# 1. Create a Greeting for your Program.
print('Welcome come to my band name Calculator')

# 2. Ask the user for the city that they grow up in 

city = input("what city did you grow in? \n ")

# 3. Ask the user for the name of a pet
pet = input("What is the name of your pet?\n")

# 4. Combine the name of their city and pet and show them their band name.
print(f" Your band name is {pet}{city}")
