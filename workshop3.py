# -*- coding: utf-8 -*-
"""workshop3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JF3I2Fl-CCbl7Nrn-8ya2RzVXyHdopgY

WORKSHOP DAY 3
"""

print(type([]))

class sample:
  pass

x=sample()

print(type(x))

class Dog:
  def __init__(self,breed):
    self.breed=breed

max=Dog(breed='lab')
tison=Dog(breed='huskie')

max.breed

tison.breed

class Dog:
  species='mammal'
  def __init__(self,breed,name):
    self.breed=breed
    self.name=name

my_dog=Dog('lab','jerry')

my_dog.name

my_dog.breed

my_dog.species

class circle:
  pi=3.14
  def __init__(self,radius=1):
    self.radius = radius
    self.area = radius * radius * circle.pi
    
    
  def setRadius(self,new_radius):
      self.radius=new_radius
      self.area=new_radius* new_radius* self.pi

  def getCircumference(self):
      return self.radius*self.pi*2

c1 =  circle()
print('The Radius is:', c1.radius)
print('The Radius is:', c1.area)
print('The Circumference is:', c1.getCircumference())

c1.setRadius(4)
print('The Radius is:', c1.radius)
print('The Radius is:', c1.area)
print('The Circumference is:', c1.getCircumference())

class track:
  def __init__(self, coor1,coor2):
    self.coor1=coor1
    self.coor2=coor2


  def distance(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


  def distance(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


  def slope(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return (y2 - y1)/(x2 -x1)

c1 = (12,9)
c2 = (3,8)

find = track(c1,c2)

find.distance()

find.slope()

class Account:
  def __init__(self,owner,balance=0):
    self.owner = owner
    self.balance = balance


  def __str__(self):
    return f'Account owner:          {self.owner}\nAccount balance:          ${self.balance}'


  def deposit(self,dep_amt):
    self.balance += dep_amt
    print("Deposit Accepted")


  def withdraw(self,wd_amt):
    if self.balance>= wd_amt:
      self.balance -= wd_amt
      print("withdraw Accepted")

    else:
      print("Funds Unavailable")

acc1 = Account('Dushyant', 50000)

print(acc1)

acc1.owner

acc1.balance

acc1.deposit(600)

acc1.balance

acc1.withdraw(60000)

acc1.withdraw(30000)

acc1.balance

