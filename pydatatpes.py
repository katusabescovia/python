#datatypes in python
#numeric
#string
#sequence type
#mapping
#boolean
#set

#Numeric;we have intergers(int),float(float)and complex numbbers(complex)


#Examples
num1=10
print(num1, "is of type" ,type(num1))
num2 =100.0
print(num2, "is of type" ,type(num2))
num3 =1+3j
print(num3, "is of type" ,type(num3))
num6 =8
print(num6, "is of type", type(num6))

#string ia a group of characters
name="scovia" #or mane='scovia'
print(name, "is of type", type(name))
#semantics is the meaning of what you have written.
#typecasting
numx="20"
#example of typecasting
numy=int(numx)#conversion of the value of numx into an interger and store it in variable numy
print(numy, "is of type", type(numy))
numy =float(numx)
print(numy, "is of type", type(numy))
numy =str(numx)
print(numy, "is of type", type(numy))
#sequence datatype
# under sequence we have List,tuple,and range
#A list is a variable that can store more than one value 
my_list=[]
my_list.append("scovia")
print(my_list)
my_list.append(15)
print(my_list)
language=["python","javascript","cc+", "ruby","cobol"]
print (language[2])
print(language[3])
print(language[0])
print(language[-1])
print(language[-2])
print(language[-3])
country=["uganda","kenya", "Tazania",["Egypt","somalia",["sudan",["burundi",["togo"],["benin"]]]]]
print(country[3][2][0])
print(country[-1][-1][-1])
print(country[0])
print(country[3][2][1][0])
print(country[-1][-1][-1][-1])
country.append(10)
print(country)
world= [["uganda","tazania","kenya"],["south africa","nambia","zambia",["england"]],["tunisia","egypt"],"USA","brazil"]
print(world[0][1])
print(world[1][2])
print(world[1][-1])
print(world[1][3])
print(world[1][3][0])
print(world[-4][-1][-1])
print(world[-4][-4])


#dictonary
uganda={"name:":"uganda","popn:":45, "location:":"E.A"}
print(type(uganda))
print(uganda.keys())
print(uganda.values())

#sets
my_numbers={10,20,30,40,10,30}
print(my_numbers)


fruits=["apples",  "mangoes","oranges",["pawpaws","pears"]]
print(fruits[0])
print(fruits[3][0])
print(fruits[3][1])
print(fruits[-1][-1])
fruits.append("pineapple")
print(fruits)

#mapping
person={"name":"scovia", "age":20, "country":"uganda", "height":171}
print(person)
print(person.keys ())
print(person.values())
for keys,value in person.items():
    print(keys)


#set is  unordered collection of unique value
student_id ={100,200,300,500,500,}
print(student_id)
print(student_id)
print(student_id)
for keys,value in person.items():
    print(keys)
for keys,value in person.items():
    print(keys,value)
#assignment create a dictionary of lakes you know and use a loop to loop   through them and their values
    lakealbert={ "location:":"eastafricanrift valley:","formation:":"faulting","oil exploration:":"oil reserves"}
    for keys,value in lakealbert.items():
        print(keys,value)
    for keys,values in  uganda.items():
        print(keys,values)
