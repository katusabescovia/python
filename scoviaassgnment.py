def tests(test1, test2):
    # here we comparing variable  test1 and variable test2
    if test1 == test2:
        #if test1 is equal to test2 ,return test1
        return test1
    else:
        #else if test1 is not equal to test2, return test2
        return test2
# The statement below prompt the user to enter test two marks and test one marks.

test2 = int(input('Please enter Marks for test two: '))
test1 = int(input('please enter Mark for testone: '))
'''
his section seems to be a multiline comment which defines the function coursework that calculate and prints the final coursework marks.
'''
def courseWrk(cswork,test1,test2):
    #  This line is attempting to call another function named tests and assign  the result to a variable named testmark  
    testsMark = tests(test1,test2)
    # The statement below calculate the average of coursework and test marks.
    avgtestsCswork = (cswork + testsMark)/2
    # The statement below calculate the final coursework marks.
    fnltestsCswork = avgtestsCswork * (40/100)
    # This line of print creates a visual line of dots helping to separate and organize  information for easier reading.
    print('..............................')
    #  The statement below outputs  the final coursework marks is fnltestscwork.
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
# The statement below prompt  the user to enter coursework marks
cswork = int(input('Please enter your course work Marks: '))
#invoke or call the cooursework function with coursework marks,test1 and test2 as  an arguments
courseWrk(cswork,test1,test2,)
