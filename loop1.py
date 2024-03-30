#break allows you to exit a loop when an external condition is met.you can use a break statement with both for and while loops.break is used to exit the loop prematurely.
#here's an example

for i in range(5):
    if i == 3:
       break
    print(i)


for letter in 'Python':     
    if letter == 'h':
       break
    print ('Current Letter :', letter)

for item in range(1,6):
    print (item)
    break

#while with the break statement
num = 0
while num < 10:
    print("Current number is", num)
    if num == 5:
        print("Encountered 5, breaking the loop.")
        break
    num += 1

#Nested Loop Example
#in a nested loop,break will stop the execution of the inner most loop.the flow of the program resumes at the next line of code.

for i in range(3):
    for j in range(3):
        if i == j == 2:
          break
        print(i, j)

#break is also used in while statement e.g

var = 10                    
while var > 0: 
    var = var -1 
    print("The value of variable is", var)  
    if var == 5:
        break
print ("goodbye")
   

#continue is used within loops to skip the rest of the code inside the loop for the current iteration and continue to the next iteration.e.g
for i in range(5):
    if i == 2:
        continue
    print(i)

#when encountered in nested loops,it only skips the current iteration of the innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
    print(i, j)

#continue can also be used when iterating over data structures like lists or dictionaries,allowing you to skip processing certain elements based on conditions e.g
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)


#languages = ["python", "java", "swift", "C", "c++"] a for loop that skips swift and c++
languages = ["python", "java", "swift", "C", "c++"]

for language in languages:
    if language == "swift" or language == "c++":
        continue
    print(language)

#while loop with continue
num = 0
while num < 10:
    num += 1
    if num == 5:
        print("Encountered 5, breaking the loop.")
        break
    elif num % 2 == 0:
        print("Skipping", num)
        continue
    print("Current number is", num)


#switch case
#there is no direct equivalent of a switch statement in python.however you can achieve similar functionality using various constructs e.g

def case1():
    print("This is case 1")

def case2():
    print("This is case 2")

def default_case():
    print("Default case")

switch_case = {
    1: case1,
    2: case2
}

choice = 2
#The get() method of dictionaries in Python retrieves the value associated with a given key.
# If the choice exists in the dictionary, call the corresponding function
# If not, call the default_case function
switch_case.get(choice, default_case)() #function call operator


def switch_case(choice):
    if choice == 1:
        print("This is case 1")
    elif choice == 2:
        print("This is case 2")
    else:
        print("Default case")

choice = 3
switch_case(choice)


def case1():
    print("This is case 1")

def case2():
    print("This is case 2")

def default_case():
    print("Default case")

choice = 2
#match is a new statement available only in python 3.10 and other later versions
match choice:
    case 1:
        case1()
    case 2:
        case2()
    case _: #wildcard
        default_case()




#switch statements can achieve similar functionality using dictionaries and functions.
def case_one():
    print("This is case one")

def case_two():
    print("This is case two")

def case_default():
    print("This is the default case")

switch_dict = {
    1: case_one,
    2: case_two
}

case_number = 2
if case_number in switch_dict:
    switch_dict[case_number]()
else:
    case_default()
    
    
def case1():
    print("Case 1")

def case2():
    print("Case 2")

def case3():
    print("Case 3")

# Define the dictionary mapping case numbers to functions
switch_dict = {
    1: case1,
    2: case2,
    3: case3,
}

# Call the function based on the case number
case_number = 2
switch_dict[case_number]()
user={"scovia:":{
    "first":"katusabe",
    "last":"scovia",
    "email":"scoviak588@gmail.com",
    "location":"Hoima",
    "gender ":"female",},
    "julian":{
        "first":""
    }}

for users, user_info in user.items():
    print(f"\nusername:{user}")
    thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(len(thisdict))
