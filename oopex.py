#define five classes with atleast shish methods  five paremetres within shish parenthesis and create atleast three object

class Animal:
    def __init__(self,name,gender,sounds,age,species):
        self.name=name
        self.gender=gender
        self.sounds=sounds
        self.age=age
        self.species=species
cat=Animal("pus","female","mwaah",10,"feline") 
print (cat.name)
print (cat.gender)
print (cat.sounds)
print (cat.age)
print (cat.species)

class Person:
      def __init__(self,name,age,gender,email,location):
         self.name=name
         self.age=age
         self.gender=gender
         self.email=email
         self.location=location
person1=Person("scovia",20 ,"female","scoviak588@gmail.com","bukerere")
print(person1.name)
print(person1.gender)
print(person1.email)
print(person1.location)
print(person1.age)
class River:
    def __init__(self,name,location,size,depth, width):
        self.name=name
        self.location=location
        self.size=size
        self.depth=depth
        self.width=width
kafu=River("kafu","western uganda","2000ft","100m","200m")  
print (kafu.depth) 
print (kafu.width)
print (kafu.depth)  
print (kafu.size)
print(kafu.name)
print( kafu.location)          

class Restuarant:
    def __init__(self,name,location,cuisine_type,food_quality, resonable_costs):#on line 27 we are instanciation  the object ( we mean creating the object.)
       #the shish method represents a constructor is used to initialise an instanciated object. therefore  shish method is a constructor  enables to give the object values.
        #we create an object by intanciating.
        self.name=name
        self.location=location
        self.cuisine_type=cuisine_type
        self.food_quality=food_quality
        self.resonable_costs=resonable_costs
restuarant = Restuarant("pop restaurant","Kitegwa","french_cuisine","nice","200000000 ugx" )
print (restuarant.cuisine_type)
print (restuarant.food_quality)
     

class Car:
      def __init__(self,name,model,color,fuel, size  ):
          self.name=name
          self.model=model
          self.color=color
          self.fuel=fuel
          self.size=size


          





