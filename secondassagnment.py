#i learnt different operators  where operators are characters that tells the computer to do with values.
#i also learnt values in python are called operands and an operator acts upon an operand.
#I also learnt different types of operators with different symbols as seen below
# summatoin operators are used when you want to find the total of given variable  after assigning  to their  values and  is represented by +: forexample num1=10,num2=20  and after you can print their total using summation operators.
#subtraction operators are used to get the difference between  variable you are using after assigning them to  values.
# I learnt modulo (%)returns the remainder of one number divided by another
# I learnt compulsion operators compare two values and return true or false
# I also learnt== is a sign used to mean a compulsion operators.(used to compare two values equal to(==))
#a statement that eveluates to a value is called an expression.
#I learnt  about loops where is defined as instructions given to the computer to do repeatedly untill something false is done / made.
#I learnt different types of loops forexample while and for loops.
#For Loop is  used when you know how many times you need to do something and you want  to be printed separately
"""forexample my_list=[2,5,6,8]
for items in my_list:
    print(items) and answer will be displayed separately.
    2
    5
    6
    8"""
#for loops normally works with the sequences forexample sets, list,tuple, string etc.and i in loops represents each items in the defined variable.
#Both involves similar process where they require initialization,conditions and increment where neccessary.
#While Loop is used when you need to keep doing something until a condition is met (e.g., keep packing until there are no more items left).
"""begin=1
end=5
while begin <=end:
    print(begin)
    begin+=1"""# that means begin will be printed five times.
# i learnt a block of code is a collection of related statements.(when the content is indented symbolised by :) is identified by indention.
#else mode is considered when the conditin is false.or when they have reached a false part unless there is a condition in for loops.
# I learnt that else is used when  the after  printing true values it wll read false that when else part comes into false.
# i learnt  also word continue used in loops means that the targeted value or operand should be skipped and print the next to it while break is used whn you want to stop at that targetd value and the remaining value wonot be printed.
#forexample
"""
x=0
while x<=5:
    if x==3:               
     break
    print(x)
    x+=1 answer will be displayed as 1,2,3

"""
"""
for i in range(5):
    if i == 3:
       continue
    print(i) answer will be displayed as 1,2,4.
"""

#function is a block of code and runs after calling it. where  block of code is defined as collection of related statements.
#function has got different types forexample  dynamic and static.
#dynamic function is a function with parametres in parenthesse while static function is a function without parameters in the parenthesses
#function is i dentified as indention.
#A keyword use in function is def meaning when defining a function 
#function are self contained block of code.things/ bse variable can't be accessed out of the function.variables we  put inside parenthesses are called paremeters, what we call a dynamic is   alsocalled parameterized function.
 # global variable can be accessed within  a function while local variables are variables within the function.
#def scovia (a,b):variables a and b are called paremeters while scovia(10,20)while value 10 and 20 are called arguments.
#i learnt calling functions is called invoke. and  also we define  afunction not creating a function.
"""
this is dynamic function.
def scovia(a,b):
    c=a*b
    print(c)
def scovia(200,3)    
     
"""

"""
this is static function.
def add():
    x=30
    y=90
    p=x+y
    print(p)
def add()    
     
"""
# I learnt "Return" is a term we use when we want a function or a piece of code to give back some information 
#module is a package python is build upon functionality:from a folder is called directory. and a file is called a script. to be reused  dat folder becomes a module and the folder is called a package when is reused  in another round way.