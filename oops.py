3#defining an object in python3#defining an object in python.We use the keyword class followed by name of class with capital letter and full column a class is a block of code identified by full column of this class we have to define a default class
# a complete fulfillment of attribute  form is an object.
#features of a class are identified by dot operatos. 
#a complete set of values is an object. 
class Animal:
     color=""
     size=""
     gender=""
     name=""
     sounds=""
     age=0
     species=""
     def feed(self):# this is a method
         #print("by chewing")
         return 'by chewing'
#creating an object of class 'animal' we only concatenates /join things of sample type:  e.g only strings to strings + is a polymorphic operator bse it enables us to add same datatypes.
     #   what we  write in methods are called behaviours.
     # a function of  class is called method and the statement within the method are called behaviour

cat = Animal() 
  
cat.name = 'pus' 
cat.gender = 'male'
cat.sounds = '  mwo'
cat.species = 'local'
cat.age = 6
cat.species = 'feline'
cat.size='small'
cat.color = 'black'


#accessing objects by  excusting them
print(f" {cat.name} is {cat.age}  years old")
print( cat.name+ "  does" +   cat.sounds )
print(f" {cat.feed()}")

# cow=Animal()
# cow.name = 'cal' 
# cow.gender = 'male'
# cow.sounds = ' mowo'
# cow.species = 'local'
# cow.age = 6
# cow.species = '  Bos taurus'
# cow.size='medium'
# cow.color = 'brown'

# dog=Animal()
# dog.name = 'cal' 
# dog.gender = 'male'
# dog.sounds = ' mowo'
# dog.species = 'local'
# dog.age = 6
# dog.species = '  Bos taurus'
# dog.size='medium'
# dog.color = 'brown'


# goat=Animal()
# goat.name = 'cal' 
# goat.gender = 'male'
# goat.sounds = ' mowo'
# goat.species = 'local'
# goat.age = 6
# goat.species = '  Bos taurus'
# goat.size='medium'
# goat.color = 'brown'
