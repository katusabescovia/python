name="scovia katusabe"
print(name)
name = "ada lovelace"
print(name.title())
gender="female"
print(gender.title())
#UPPERCASE IN string
name="ada lovelace"
print(name.upper())
print(name.lower())
name="ADA LOVELACE"
print(name.lower())



#USING AVARIABLE IN STRINGS:This is where we use a variable's value  inside a string For example, you might want to use two variables to represent a first name and  last name, respectively, and then combine those values to display someone’s full name: f string f""
#To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark 1. Put braces around the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed.These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value. The output from the previous code is:ada lovelace You can do a lot with f-strings. For example, you can use f-strings t
#The full name is used in a sentence that greets the user 1, and the title() method changes the name to title case. This code returns a simplebut nicely formatted greeting: Hello, Ada Lovelace!You can also use f-strings to compose a message, and then assign the
firstname="katusabe"
lastname="scovia"
fullname=f"{firstname} {lastname}"
print(fullname)
firstname="tugume"
lastname="Julian"
fullname=f"{firstname}{lastname}"
print(f"Hello,{fullname.title()}!")
#  You can also use f-strings to compose a message, and then assign the 
# entire message to a variable:
firstname="tushabe"
lastname="jacob"
fullname=f"{firstname}{lastname}"
message=f"hi,{fullname.title()}!"
print(message)
#Adding whitespace to strings with Tabs or Newlines
#  In programming, whitespace refers to any nonprinting characters, such as 
# spaces, tabs, and end-of-line symbols. You can use whitespace to organize 
# your output so it’s easier for users to readto add a tab to your text, use the character combination \t
print("python")
print("\tpython \nsomeone")

#  To add a newline in a string, use the character combination \n
print("languages:\npython\ncc+\njavascript")


#  You can also combine tabs and newlines in a single string. The string 
# "\n\t" tells Python to move to a new line, and start the next line with a tab. 
# The following example shows how you can use a one-line string to generate 
# four lines of output:
print("Languages:\n\tPython\n\tC\n\tJavaScript")

 #Stripping WhitespaceExtra whitespace can be confusing in your programs. To programmers, 
#'python' and 'python ' look pretty much the same. But to a program, they are two different strings. Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.It’s important to think about whitespace, because often you’ll want to compare two strings to determine whether they are the same. For example, 
# one important instance might involve checking people’s usernames when 
# they log in to a website. Extra whitespace can be confusing in much simpler situations as well. Fortunately, Python makes it easy to eliminate extra 
# whitespace from data that people enter.
#  Python can look for extra whitespace on the right and left sides of a 
# string. To ensure that no whitespace exists at the right side of a string we use #the rstrip() method
language="python"
print(language)
print(language.rstrip())



#  To remove the whitespace from the string, you strip the whitespace 
# from the right side of the string and then associate this new value with 
# the original variable 1. Changing a variable’s value is done often in pro
# gramming. This is how a variable’s value can be updated as a program is 
# executed or in response to user input.
#  You can also strip whitespace from the left side of a string using the 
# lstrip() method, or from both sides at once using strip():
favorite_language = ' javascript '
print( favorite_language.rstrip())

print(favorite_language.lstrip())
print(favorite_language.strip())
A="i love listening gospel music"
print(A.rstrip())#removes white spaces from the left side.
print(A.lstrip())
print(A.strip())#in the real world, these  stripping functions are  used most often to clean up user input before it's stored i program.

# for i in range(5):
#   for j in range(5):
#     if j==1:
#       continue
#     print(i,j)   
# for i in range(5):
#   for j in range (5):
#     # continue
#    print(i,j)

# for i in range(5):
#     for j in range(5):
#         if j==2:
#             break
#         print(i,j)
            
    
num=  "  John"
print(num)
print(num.rstrip())
print(num.lstrip())
print(num.strip())
#removing Prefixes:this involves removing prefixes of URL forexample prefixhttps://
ww="https://google.com"
print(ww.removeprefix("https://"))
simp="https://youtube.com/watch"
print(simp.removeprefix("https://"))

#exercises:about dealing with strings page 24
firstname="katusabe"
lastname=" Eric"
fullname=f"{firstname}{lastname}"
message=(f"Hello, {fullname} would you like to learn some python today?")
print(message)

name="Tugume Scovia"
print(name.lower())
print(name.title())
print(name.upper())

firstname="Albert"
lastname=" Einstein"
fullname=f"{firstname}{lastname}"
message=(f'{fullname} once said,"A person who made a mistake never tried anything new."')
print(message)



print("\t\n Ajuna joshua")
name="Ajuna Joshua"
print(name.lstrip())
print(name.rstrip())
print(name.strip())
filename="python_notes.txt"
print(filename.removesuffix(".txt"))#suffix used to remove file extension:

# dealing with numbers on page 28
print(5+3)
print(4*2)
print(16/2)
print(16-8)

favorite_number=100
message=(f"this is my favorite number{favorite_number}")
print(message)

#lists:
name=[" scovia","julian","mike"]
name=f"I love my name{name[0]}"
print( name)

cyclists=["car"," mortycle","bicyle"]
message=f"I would like to own a honda{cyclists[1]}"
print( message)
cyclists=["car"," mortycle","bicyle"]
#replacing:
cyclists[0]="bic"
print(cyclists)

#adding of elements in lists

cyclists=[]
cyclists.append("car")
cyclists.append("bicycle")
cyclists.append("mortycle")

print(cyclists)


#inserting  in the list
cyclists=["bic","motor"]
cyclists.insert(0,"car")
cyclists.insert(1,"bicycle")
cyclists.insert(2,"mortycle")
print(cyclists)
#deleting elements in lists

cyclists=["car","bicycle","mortycle"]
cyclists.remove("bicycle")
print(cyclists)
cyclists=["car","bicycle","mortycle"]
cyclists.pop(1)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


  
class Car:
    """A simple attempt to represent a car."""
 

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
 
        return long_name.title()
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())