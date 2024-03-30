def userdetails(name,email,age,gender):
    name=input("type here your name")
    email=input("type here your email")
    age= int(input("type here your age"))
    gender=input("type here your gender")
    print(name,email,age,gender)

userdetails("name","email","age","gender")



def net(paye,nssf, salary):

    salary=   int(input("type here your salary"))
    payerate= int(input("type here your rate"))
    nssfrate= int(input("type here your rate"))
    nssf=(nssfrate/100)*salary
    paye= (payerate/100)*salary
    netpay=salary-(paye+nssf)
    print(paye)
    print( nssf)
    print(netpay)
net("paye","nssf","salary")    
       







