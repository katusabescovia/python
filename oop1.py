#classes define properties to the 

#__init__() is called shish method  is a special method we use in python when identifying properties of  individual object soon coming/class/object. is  first pararemeters in the shish  parenthesis refers to an individual class and self is the first property to identify other properties of a class:Any method within function should have self paremetres within parenthesis of methods and should take the first parameter.
#after assignment those attributes  becomes our values.
#self is used to 

class Lake:
     def __init__(self,name,formation,location,depth,size,width,ltype):
          self.name=name
          self.formation=formation
          self.location=location
          self.depth=depth
          self.size=size
          self.width=width
          self.ltype=ltype


#creating objects of class lakes
lake1=Lake("l.albert","faulting","western rift valley","200ft","100m","100m","fresh water") 
print(lake1.name)        
print(lake1.formation)
print(lake1.location)
print(lake1.depth)
print(lake1.size)
print(lake1.width)
print(lake1.ltype)
      

class River:
     def __init__(ozzy,name,formation,location,depth,size,width,ltype):
          ozzy.name=name
          ozzy.formation=formation
          ozzy.location=location
          ozzy.depth=depth
          ozzy.size=size
          ozzy.width=width
          ozzy.ltype=ltype

          #




