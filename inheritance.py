# class Animal:
#      name=""
#      def eat(self):
#           print("I can eat")
#           #inheriting from class Animal.
#  #in that sense class dog is taking all properties of animal-dog is a subclass of Animal that mean a dog is derived class from animal then the animal becomes a superclass  or base class or parent class then the dog becomes child class                 
# class Dog(Animal):
#      def display(self):
#           print('My name is',self.name)
#           print(f"My name is,{self.name}")  
# gshepherd=Dog()
# gshepherd.name="police"
# print(gshepherd.name)
# gshepherd.display()
# gshepherd.eat()

# #create 3 superclasses with corresponding atleasttwo sub classes from each  and create 3 objects from them.
class Car:
      name=""
      def fuel(self):
          print("I have fuel")
class Elictriccar(Car):
      def display(self):
        print("My electric car is",self.name)
Teslamodel=Elictriccar()
Teslamodel.name="tesla"
print(Teslamodel.name)
Teslamodel.display () 
Teslamodel.fuel()
Nissanleaf=Elictriccar()
Nissanleaf.name="nissan"
Nissanleaf.display()
Nissanleaf.fuel()
BMWI3=Elictriccar()
BMWI3.name="bmwi"
print(BMWI3.name)
BMWI3.display()
BMWI3.fuel()

class Sportscar(Car):
       def display(self):
           print("My sportscar is",self.name)
Porsche911=Sportscar()
Porsche911.name="porsche"
print(Porsche911.name)
Porsche911.display()
Chevroletcorvette=Sportscar()
Chevroletcorvette.name="chevrolet"
print(Chevroletcorvette.name)
Chevroletcorvette.display()
Chevroletcorvette.fuel()
FordMustang=Sportscar()
FordMustang.name="ford"
print(FordMustang.name)
FordMustang.display()
FordMustang.fuel()




class River:
      sizes=""
      def location(self):
           print("I am located in Netherlands")
class Lowlandriver(River):
      def width(self): 
           print(f"I have a width of ,{self.sizes}") 
Mississipiriver=Lowlandriver()
Mississipiriver.sizes="2000ft"
print(Mississipiriver.sizes)
Mississipiriver.location()
Mississipiriver.width()
Amazonriver=Lowlandriver()
Amazonriver.sizes="1000ft"
print(Amazonriver.sizes)
Amazonriver.location()
Amazonriver.width()
Yangtzeriver=Lowlandriver()
Yangtzeriver.sizes="500ft"
print(Yangtzeriver.sizes)
Yangtzeriver.location()
Yangtzeriver.width()


class Mountainriver(River):
      def width(self): 
           print(f"I have a width of ,{self.sizes}")

Coloradoriver=Mountainriver()
Coloradoriver.sizes="3000ft"
print(Coloradoriver.sizes)
Coloradoriver.location()
Coloradoriver.width()
snakesriver=Mountainriver()
snakesriver.sizes="5000ft"
print(snakesriver.sizes)
snakesriver.location()
snakesriver.width()
rhineriver=Mountainriver()
rhineriver.sizes="800ft"
print(rhineriver.sizes)
rhineriver.location()
rhineriver.width()

class Lake:
      depth=""
      def width(self):
           print(f"I have a width of ,{self.depth}")
class Freshwater(Lake):
      def size(self):
           print(f"I have a size of ,{self.depth}")
lBaikal = Freshwater()
lBaikal.depth="100m"
print(lBaikal.depth)
lBaikal.width()
lBaikal.size()
greatlakes = Freshwater()
greatlakes.depth="200m"
print(greatlakes.depth)
greatlakes.width()
greatlakes.size()
Deadsea = Freshwater()
Deadsea.depth="300m"
print(Deadsea.depth)
Deadsea.width()
Deadsea.size()
class saltylake(Lake):
      def size(self):
           print(f"I have a size of ,{self.depth}")
lkyoga=saltylake()
lkyoga.depth="400m"
print(lkyoga.depth)
lkyoga.width()
lkyoga.size()
lkatwe=saltylake()
lkatwe.depth="500m"
print(lkatwe.depth)
lkatwe.width()
lkatwe.size()
lmunyampala=saltylake()
lmunyampala.depth="600m"
print(lmunyampala.depth)
lmunyampala.width()
lmunyampala.size()



     
              
