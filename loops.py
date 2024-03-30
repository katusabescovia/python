list=[10,20,30,40,50] #we are declaring 
#a statement that eveluates to a value is called an expression.
#an operator is something what tells a computer what to do with operand(values.) 
#an operator acts upon an operand.
#a value in programming is called an operand.
#below is an iteration /continue/repeatedly of value in a list of numbers 
def loop1():
  list=[10,20,30,40,50,60]
  for i in list: 
      print(i)#it means printing  value in list each at once separately i represents item.a loop is mechanism in programming which tells a comp
def loop2():
    for i in range(10):
        print(i)
def loops3():
    item = 1
    for item in range(1,10):

         print(item)
def loop4():      
    for i in range(1,21):
        if i%5==0:
           print(i)
         
def loop5():
    for i in range (1,20): 
        if i% 2 == 0 :
           print(i)
def loop6():           
    for i in range(1,20):#a block of code is a collection of related statements.(when the content is indented symbolised by :)
        if i%2 !=0 :
           print(i) # the above is a syntax for  for loops:


        # else mode is considered when the conditin is false.or when they have reached a false part. unless there is a condition in for loops:else is used when  the after  printing tue values it wll read false that whe else part comes into false:
def loop8():           
    digits =[23,67,50,70,89]
    for i in digits:
        print(i)  
    else:
        print("no items left")

loop8() 
loop6()      
