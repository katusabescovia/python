#   Here we are looking at different datatypes.
some_string = 'Python is fun' 
# we are declairing a variable of some_string and assign it to  a value of  string python is fun
a, b, c = 5, 3.2, 'Hello'

print(a)  #here the output will be  value  of 5 
print(b)  # output will be value of 3.2
print(c)  # Here the output will be value  with a string of hello

# here we are looking at  different numeric datatypes.
num1 = 5
# here we are declairing a variable of num1 and assign it to a value  of 5
print(num1, 'is of type', type(num1))
#5 is of type  an interger number
num2 = 2.0
#Here we are declairing a variable of num2 and assign it to a value of 2.0
print(num2, 'is of type', type(num2))
# the output will be 2.0 is of type of a float number.
num3 = 1+2j
#Here we are declairing a variable of num3 and assign it to a value of 1+2j
print(num3, 'is of type', type(num3))
# the output will be 1+2j is of type of complex number
languages = ["Swift", "Java", "Python"]

# here we are declairing a variable of list of languages and assign it to  value of three  string elements.
print(languages[0])   # 'swift'

# here we  are displaying  the first element in a list of languages
print(languages[2])   #  'python'

#here we are displaying the third element in a list of languages.  
product = ('Microsoft', 'Xbox', 499.99)

# we are declaring a variable of tuple of product and assign it to a value of three string elements.
print(product[0])   # Microsoft

# here we are displaying the  first element in a tuple of product using their index position.
print(product[1])   # Xbox


#Here we  are displaying the   second  element in a tuple 0f product  using their index position.
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
#here we  are declairing a variable of dictionary of capital_city and assign it to three key-values pairs.
print(capital_city)


#here the out put will be  showing keys and value {'nepal:'kathmandu', 'Italy':'Rome', 'England':'london'} 
student_id = {112, 114, 116, 118, 115}

# we are declairing the variable of set of student_id and assign it to value of five elements represented by braces brackets.
print(student_id)

# the out put will be{112, 114,116,115}
print(type(student_id))

# student_id is of type of set.
fruits = ["apple", "mango", "orange"] 
# here we are declairing a variable of lists of fruits and assign it to value of three string elements
print(fruits)

# here the output will be ['apples','mango','oranges']
numbers = (1, 2, 3) 
#here we are declairing a variable of tuple of numbers and assign it to operand of three elements
print(numbers)

# here the out put will be(1,2,3)
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#we a declairing a variable of dictionary of alphabets and assign it to three key-value pairs.
print(alphabets)

# here the out put will be {'a':'apple','b':'ball','c':'cat'}
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


# output is{'a','e','i','o','u'}
student_id = {112, 114, 116, 118, 115}

# here  we are declairing  a variable of set of student_id and assign it to a value of five elements.
print(student_id)

# out put is {112,114,116,118,115}
print(type(student_id))
#  student_id is of type of set.
product = ('Microsoft', 'Xbox', 499.99)

# we are declaring a variable of tuple of product and assign it to a value of three string elements
print(product[0])     # Microsoft

#  here we are displaying the  first element in a tuple of product using their index position.
print(product[1])   # Xbox




#Here we are looking at operators.
a = 7
b = 2

#here we are looking at summation operators 
print ('Sum: ', a + b)  

# here the out put is 9
print ('Subtraction: ', a - b)   

# here the out put will be 5
print ('Multiplication: ', a * b)  

# here the out put will be 14
print ('Division: ', a / b) 

# here the out put will be 3.5
print ('Floor Division: ', a // b)

# here the out put will be 3
print ('Modulo: ', a % b)  

#here the out put is 1 
print ('Power: ', a ** b)   


# here the out put will be 49
a = 10

# Here we are declairing a variable of a  and assign it to a value of 10.
b = 5 

# Here we are declairing a variable of a  and assign it to a value of 5
a += b      #here we are looking at summation assignment.
print(a)
# Output: 15


#  here we are looking at different compulsion  operators
print('a == b =', a == b)

# here the out put is False
print('a != b =', a != b)

# here the out put is  True
print('a > b =', a > b)

#  here is the out put is True
print('a < b =', a < b)

#  here the out put is false
print('a >= b =', a >= b)

# Here the out put is True
print('a <= b =', a <= b)
# Here the out put is False
print((a > 2) and (b >= 6)) 

# here the out put is False.
print(True and True)     #here the out put is True. 
print(True and False)    # here the out put is False.

# logical OR
print(True or False)     # here the out put is True.

# the expression evaluates True bescause or returns true. 
print(not True)          #  here the out put is False

# here it means it take a not true to be not true and true to be true. 
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# here we are looking at identity operators
print(x1 is not y1)  # True
#here it means the identity of x1 is not as the same as   y1 which returns the an expression to be true.
print(x2 is y2)  # False
#here it is false bescause the identity of x2 is different from identity of y2 which returns an expression to be false.
print(x3 is y3)  # False
##here it is false bescause the identity of x3 is different from identity of y3 which returns an expression to be false.
message = 'Hello world'
#here we are  declairing a variable of message  and assign it to a value of string hello world.
dict1 = {1:'a', 2:'b'}
#here we are  declairing a variable of dictionary of dict1 and assign it to two keys-values pairs.
print('H' in message)  # print(message[0])  the out put will be H.


# here we are looking at membership operators.
print('hello' not in message)  # True

# It is true bescause  a string of hello is not  a member of variable of message
print(1 in dict1)  # True

# it is true bescause  value of 1 is a member in dictionary of dict1 .
print('a' in dict1)  # True
















