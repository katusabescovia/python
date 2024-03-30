def add(x,y):
    p=x+y
    print(p)
add(5,9) 
add(5,10) 
add(12,20)
def add(x,y):
    p=x*y
    print(p)
add(5,9) 
add(5,10) 
add(12,20)
#arguments in functions.this is information that are passed into:they are specified after writing  named afunction and written within parenthesses.
def my_function(x):
    print(x)
my_function(9) 
def my_loop(a,x): 
    print("a:",a ,"x:",x )
    print(id(x))
    print(id(a))
my_loop(10,8)
my_loop(12,10)#Pass by value or Pass by reference:
#pass by value is when you are passing a value not the address while pass by reference is when am passing a ddress not a value.
def add(a,c,d,e):
    f=a+c+d+e
    print(f)
add(3,4,6,6)
add(6,8,9,4)# called values are called actual arguments.
#we have different types of argumentsthat is actual,formal arguments.(a,g)can be called variable/ formal arguments.
#actual arguments has four different four types forexample position,keywords,default and variable length.
#position position comes when you want to know 
def persons(name,age):
    print(name,age-2)
persons("scovia",20)   
#keyword( name="scovia",age=30)s
#default*y is seen as tuple when you try to run it please  it helps when you dont want ot be adding on same fuction with different arguments within parenthesses: within :

def add(x,*y):
    print(x)
    print(y)
add(2,3,45)    
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
        print(c)
sum(3,7,8,4) 
def p(*b): 
    a=0
    for i in b:
        a=a+i
        print(a)
p(2,3,4,4)  

#keyworded variable length. aurgements for data or variable we use**

def add(a,*b):
    p=a
    for i in b:
        p=p+i
        print(p)
add(10,20,30)   
a=1
while a <=5:
     a+=1
     print("scovia")
     
#function Aurgements (modularity,)   how to pass paremeters to the function. and different types of function.
def poo(x):
    x=8
    print ("x:",x)
    print(id(x))
    a=10
    print("a:",a)
    print(id(a))
poo( a)


def po(x):
    print(id(x))
    x=4
    print("x",x)
a=5
print(id(a))
po(a) 
print("a",a)   

#global keyword in python:
#scope:we will be creating variable inside function.
a=10# variable written outside function is called global
# variable writteninside function is called local variable:
a=10
b=30
def some():
    a=20 
    b=40
    print("inside:",a)
    print("inside:",b)
some()
print( "outside:",a)
print( "outside:",b)

a=7
print(id(a))
def thing():
    a=9
    x=globals()["a"]
    print(id(x))
    print("infun",a)
    globals()["a"]=1   
thing() 
#Return" is a term we use when we want a function or a piece of code to give back some information or a value after it finishes running. "result" is the answer or outcome of something, and "return" is the action of giving back that answer or outcome from a function or a task in a program. They're both important concepts in programming because they help us get the information we need to make our programs work correctly.
#below is the meaningSo, when you call do(10, 2), the function calculates 10 * 2, which equals 20, and returns this value. This returned value (20) is then assigned to the variable result. Therefore, after running this code, the variable result will hold the value 20.

def do(x,u): #return is used to keep my vales 
    c=x*u
    return(c)
result=do(10,2)
print(result)
#this is how we write when i want to return two values
def add_sub(e,d):
    c=e+d
    b=e-d
    return(c,b)
result1,result2=add_sub(10,2)
print(result1,result2)
=