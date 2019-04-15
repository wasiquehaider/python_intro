# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list 
numbers = [1,2,3,4,5] # this is the most common way
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# use a constructor 
# numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)

# get a value  
print(fruits[2])

# get lenght of list 

print(len(fruits))

# Append to a list 

fruits.append('Mangoes')

# Remove from a list 

fruits.remove('Pears')

# Insert into position

fruits.insert(2,'Banana')

# Change value

fruits[0] = 'BlueBerry'


# Remove with pop

fruits.pop(2)

# Reverse List

fruits.reverse()

# Sort List
fruits.sort()

# Reverse Sort List
fruits.sort(reverse=True)


print(fruits)
