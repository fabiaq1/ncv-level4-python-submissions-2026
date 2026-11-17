fcode = []
name = ''
hours = 0
rate = 0
amt = 0
def amount_due(fcode, hours):
    hours= float(input("Please enter hours \n:"))
    #amtdue = hours * rates
    #return amtdue
    fcode = ['Squash', 'Swim', 'Gym', 'Wei']
    facility = ['Squash court', 'Swimming', 'Gym', 'Weight']
    rates =[13.00, 12.00, 11.00, 8.00]
    code = input('Please enter facility code \n:')
    print('Facility', '\t', 'Facility code', '\t', 'Rate per hour')
    for x in range(len(fcode)):
        print(facility[x], '\t', fcode[x], '\t', rates[x])
        
    for y in range (len(fcode)):
        if fcode == fcode[y]:
            rate= hours * float(rates[y])
        elif fcode == fcode
    
def final_amount(amt):
     vat = 0.14
     
     return amt - (amt * vat)

def display(name, final_amount):
    print(f'Customer name : {name}')
    print(f'Final amount : R{final_amount}.2f')
    
def process_payments():
    name= input("Please enter the name \n: ")
    amount_due(fcode, float(hours))
    final_amount(amt)
    display(name, final_amount)
    
process_payments()
    
    
    
    

     
     

