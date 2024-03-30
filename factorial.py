#Factorial functions:Here we are  trying to find the factorial of 5

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
x=5
result =fact(x)

print(result)

#recurrssion in python:it means you are calling a fuction to it'self

# import sys
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())#if you write this statement you print 100 automatically comes.
# def add():
#     print("hello world")
#     add()
# add()    

#Object Oriented Programming:python supports different programming such as functional,object oriented and precedure orinted programming:
#functional programming means you can achieve certain task 00PS:
#object  helps us to store variables data and behaviors.
#if we want to define behavior we have to use methods:
#functions in object oriented programming are called methods.
#how can we connect this function we look at object,class Abstract c,encapsulation and polymorphism
#class -design for an object. and object -instance
 #Things we can put in after defining a class  below it attributes and behaviors.
#attributes - variables and behaviors are called metthods(function)
class computer:
    def constructor(self):
        print("15,16gb,1TB")
#special variables and special behaviors()        

com1=computer()
com2=computer()
# computer.constructor(com1) 
# computer.constructor(com2)
com1.constructor()
com2.constructor()       

# class add():
#     def __init__(self,cpu,memory):

# com1 =add(200,100)
# com2=add()



# for i in range (3):
#     for j in range (3):
#         if i == j == 2:
#             break
#         print(i,j)


for i in range (3):
    for j in range (3):
        if i == j == 2:
            break
    print(i,j)
       






