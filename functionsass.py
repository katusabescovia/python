def gross(revenue,cogoodssold):
    grossprofit=revenue-cogoodssold
    return grossprofit
gross(500000,100000)


def net( grossprofit,totalexpenses):
    netprofit=grossprofit-totalexpenses
    return netprofit   
net(400000,100000)

def profit():
    income=net(400000,100000)-100000
    print(income)
profit()    

    
    
 