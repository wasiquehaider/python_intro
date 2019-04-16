# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  #Constructor
  def __init__(self,name,email,age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My Name is {self.name} and I am {self.age}'

  def hasBirthDay(self):
    self.age += 1


# Extend Class

class Customer(User):
  #Constructor
  def __init__(self,name,email,age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self,balance):
    self.balance = balance

  def greeting(self):
    return f'My Name is {self.name} and I am {self.age} and my balance is {self.balance}'


#Init User Object
wasique = User('Wasique Haider', 'wasique@gmail.com', 25)
#Init Customer Object
janet = Customer('Janet', 'janet@gmail.com', 25)

janet.set_balance(500)
print(janet.greeting())


wasique.hasBirthDay()
print(wasique.greeting())