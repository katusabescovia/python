class person :
    def __init__(self,name,age,gender,email):

        self.name=name
        self.age=age
        self.gender=gender
        self.email=email
p=person("scovia",20,"female","scoviak@gmail.com")
print(p.name)        
print(p.age)
print(p.gender)
print(p.email) 
print(p.name,p.age,p.name,p.gender,p.email) 

#The __init__() function is called automatically every time the class is being used to create a new object.
#se the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
#the  __str__() function The __str__() function controls what should be returned when the class object is represented as a string.
class Person:
    def __init__(self,name,age,gender,):
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return f"{self.name} {self.age} {self.gender}"
c= Person("julian","23","female")
print(c)
#object methods;Objects can also contain methods. Methods in objects are functions that belong to the object.
# Attributes:
# Attributes are variables associated with a class. They hold data that characterizes the class. You can access attributes using the dot notation (object.attribute). Attributes can be either class attributes (shared among all instances of the class) or instance attributes (unique to each instance of the class).

# Methods:
# Methods are functions defined within a class. They define behaviors or actions that the objects of the class can perform. Methods can take arguments and operate on the attributes of the class or perform other tasks. The first argument of any method within a class is typically self, which represents the instance of the class itself.

# Constructor:
# The constructor method, __init__, is a special method in Python classes. It is called when an instance of the class is created. It is used to initialize the attributes of the class.

# Instance Creation:
# You create an instance of a class by calling the class name followed by parentheses. This invokes 
class animal:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
cat=animal("catpet",12,"female") 
print(cat.age)
print(cat.name)           
print(cat.gender)  

#The self ParameterThe self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#calling functions in classes:
#Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Animal:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def myfunc(self):
        print("Hello my name is"+self.name)
cat=Animal(" dogpet",12, "male")
cat.myfunc()

class person:
     def __init__(abc,name,age,gender,email):
         abc.name=name
         abc.age=age
         abc.gender=gender
         abc.email=email
     def myfunc(abc):     
         print("Hello my name is"+abc.name)
mysillyobject=person 

#Python InheritanceInheritance allows us to define a class that inherits all the methods and properties from another class.Parent class is the class being inherited from, also called base classChild class is the class that inherits from another class, also called derived class.

#class parent
class person:
     def __init__(self,firstname,lastname):
         self.firstname=firstname
         self.lastname=lastname
     def printname(self):
        print(f"hello {self.firstname} {self.lastname}")   
p=person("katusabe","Scovia")          
p.printname()  


#class child students using  class person
# class person:
#      def __init__(self,firstname,lastname):
#          self.firstname=firstname
#          self.lastname=lastname
#      def printname(self):
#       class student(person): 
#               pass
         
# x = ("katusabe","Scovia")          
# x.printname()  
#if we want to store some thing in an object we have to define variables /attributes andwhen we want to define behaviours we have to define methods/function.action defines our behaviour
#things we put in class behaviour methods /function, attributes variables:

#DEFINE:
class computer:
    def config(self):
        print("15,16gb,1TB")
comp1=computer()
comp2=computer()       
comp1.config()
comp2.config()

class computer:
    def __init__(self,cpu,rm):
       self.cpu=cpu
       self.rm=rm
    def config(self):
        print(self.cpu,self.rm)  
compi=computer("15","19")
comp2=computer("Ryzen",8 )
compi.config() 
comp2.config()  

#constructor and self


# class student(person):
#      def __init__(self,firstname,lastname):
#          super().__init__( self,firstname,lastname)
#          self.firstname=firstname
#          self.lastname=lastname
        
# x=student("mike","katusabe")
# print(x.firstname)
# print(x.lastname)
# print(x.year)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()