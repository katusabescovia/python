#Object Orientated programming:is a pyaramid /idea that avocates  for the developing of software based on real world objects. classes vs objects
#principles of oop
#polymophism
#inheritance
#Abstraction.
#encapsulation.

#class is a blue print( original copy of something) of an object
#class car has an objects such as involing different types of cars such as ranger rovers.
#objects takes on all feature sof an objects. but each objects  has its own attributes., properties
# an objects is an instance of a class
# a class is a group of objects. class gives existance of an objects
#instance is a duplicate of an objects
#attributes are called variables :class will have an attribute 0f animal are  name,age,color,number of legs
#a complete of set of attributes are an object.
#how to identify class of an object we use a phrase 'is a'
#e.g acat" is a" animal, therefore a cat is an object and class is animal.
# lake victioria "is a"lakes
#class of cats "we "

#on identifying classes we concrete on abstraction:refers to the ability of concreting of highest level of representation.of what you are talking about.
#class names are  singular e.g cat not cats and should start with capital letter.
#abstract are only limited to classes
#concept of inheritance:abstraction is ability to leave out an neccesary details of an object and you go with an important things and you put other things in later but classes is important while  a

#here we have parent and child
#toyota is a child of car# a class of car is a parent of toyota
#sumsang is a child of phone
#is ability by an object to taken on different attributes  of a class e.g toyota wish belong to class of toyota and toyota  belong to a class of car.

#polymorphism:refers to the ability to take  on different attributes of a class.that one brings about privacy or independent: ability for  an object taking on  multiple forms.
# encapulsion is  bility to have what to say and not what to say(share)
#Assignments:
#use two dyanamic fuctions that prompt a user to input name,age,email,gender and prints and a second function  should  prompt the user to input the rate of PAYE (30% )nssf (11%) and gross income/  amount salary   calculate net pay of individual:

#Abstractions:
class Arsenal:
      def originated(self):
          print("originated")


     #polymorphism:refers to the ability for an object taking on multiple forms
class WHT:
    #   def __init__(self,Wht):
    #      self.Wht=Wht 
      def calc (self):
            Wht =10000*0.06
            return Wht 
value=WHT() 
print(value.calc())              
               