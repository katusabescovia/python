num=5
print(id(num))
#id function:is used to identify the address of variable.
name="scovia"
print(id(name))
a=10
b=a
print(id(b))
print(id(a))
print(id(10))
a=9
print(id(a))
#Numeric
PI=3.14
print(PI)
print(PI, "is type of",type(PI))
print(type(PI))
num1=5
print(num1, "is the type",type(num1))
num2=1+4j
print(num2,"type", type(num2))
#typecasting
num3= float (num1)
print(num3 , "type",type(num3))
k=6
b=5
c=complex(k,b)
print(c,"type",type(c))
#boolanedatatype is the conditoin where we use true or false.
e=k<b
print(e)
print(e,"type",type(e))
e=k>b
print(e)
#Tuple
t=(20,23,45,60)
print(t,type(t))
print(t[0])
#range
print(range(10))
print(list(range(10)))
print(tuple(range(10)))
print( list(range(4,10,4)))
print( list(range(2,10,2)))
print( list(range(6,10,6)))
print( list(range(1,9,5)))
#lists
list=[20,30,40,50]
list.append(60)
print(list)
list.remove(20)
print(list)
#mapping /dictionary:
dict={"name":"doreen","age":20}
print(dict.keys())
print(dict.values())
dict2={"scovia":"jovia","julian":"python","janet":"javascript"}
print(dict2.keys())
print(dict2.values())

#operattors is characters or something that tells a computer to do with operands.here we use different -arithmetic operators, assignment operators ,relational operators,logical operators,and unary operators.
#assignment operatoors:
x=4
#addition assgnment 
x=4
x+=6
print(x)
x-=2
print(x)
x*=2
print(x)
a,b=10,30
print(a,b)
#Unary operators:
#compulsion operators
a=6
b="scovia"
c=6
print(a==c)
print(a==b)
print(c!=b)
print(a!=c)
#logical operators:
a=5
b=4
print(False and True)
print(True and False)
print(True or False)
print(False or True)
print(not True)
print(not False)
#membership in python we use in or  not in  here we identify  variables.
mylist=[10,20,30]
mylist2=[10,20,30]
print(mylist is not mylist2)
print(mylist is mylist2)


#Bit wise operators:
#complement(~) the symbol is called "tidle-"
#and(&)
#or(|)
#xOR()
#right sheift(>>)
#left shift(<<)
#loops tells the computer to do repeatedly until the computer reaches the end of the  program.

#here we provide loop for, while
t=1#(initialization)
while t<=5:#(condition)
    print("i love listening to gospel music")
    t=t+1#(increment/decrement)
    p=5
    while p>=1:
        print("i love you")
        p-2
print(False and F)









