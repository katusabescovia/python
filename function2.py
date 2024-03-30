def add ():
    num1,num2 =10,20
    sum = num1+num2
    print(sum)
add() 
def add2(num1,num2):
    sum=num1+num2
    print(sum)  
add2(10,20)
add2(100,50)
add2(200,45)

def sub1(num1,num2):
    sub =num1-num2
    print(sub)
sub1(95,60)    

def multi(num1,num2):
    multi =num1*num2
    print(multi)
multi(12,10)

def div(num1,num2):
    div =num1/num2
    print(div)
div(120,12)    

def power(num1,num2):
    power=num1**num2
    print(power)
power(10,2)    

def modulo(num1,num2):
    modulo =num1%num2
    print(modulo)
modulo(100,200) 

def floordivision(num1,num2):
    floordivision =num1//num2
    print(floordivision)
floordivision(7,3)


def multidata(name, num1,num2,flt):
    print(name)
    print(num1)
    print(num2)
    print(flt)
multidata( "scovia",10,20,20.9)    


def data(district, num1,num2,flt):
    print(district)
    print(num1)
    print(num2)
    print(flt)
data( "Hoima",50,70,70.9)    

def tidata(name, age,gender,email):
    print(name)
    print(age)
    print(gender)
    print(email)
tidata( "scovia",20,"female","scoviak588@gmail.com")  


def hack(name,yob,district):
    print(name)
    print(yob)
    print(district)
    currentyear=2024
    age =currentyear-yob
    print(age)
hack("scovia",2003,"hoima")    

def ack(name,yob,district):
    # print(district)
    currentyear=2024
    age =currentyear-yob
    print( name,"is",age)
ack("scovia",2003,"hoima")    


