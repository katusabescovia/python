#how to make afunction to communicate with the other.
#if he says it takes on  he means paremeters:
#return in this function a function that wants to share must return that actual value you want  to share to another function..must return a value to the calling function.#returns makes a value or variable global
def vat(rate,price):
    frate=int((rate/100)*price)
    return frate
    print(frate)
vat(18,20000)   
#value which you pass / values you use while invoking a function are called  arguments.
#return is the  last statement they execute in the function.
#using parameterized function create three function which share values. the last function should print out.
#two of them should be dynamic;
#last one should be receiving values from sholdnot parameterised 
# what  "from then and nowwhat are your learning takeaway with examples in code" 

def netprice():
    actvat=vat(18,20000)
    actualprice=actvat+20000
    print(actualprice)
    print(actvat)
netprice() 

#ptython is extremely module and orientation
#module is a package python is build upon functionality:frm a folder is called directory. and a file is called a script. to be reused  dat folder becomes a module and the file is called a package when is reused  in another round way.
 #yesterday we started by understanding what a folder is in python and we realised that it is not called a folder but rather a directory.
#we also got to know that a file named within the directory is called a script and you emphasised that for your code to be resusable by another programmer,your directory becomes a module and your file becomes a package.
#We also learn how to create a directory using commnad prompt by typing mkdir
#A valid package of python should by dafault have two underscores init dot py even if the file is empty.

   
