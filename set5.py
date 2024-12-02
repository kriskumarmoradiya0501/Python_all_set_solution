expenses = { 
    'Monday': [ 
        {'Amount': 50, 'Category': 'Groceries', 'Description': 'Bought vegetables'}, 
        {'Amount': 20, 'Category': 'Transport', 'Description': 'Bus fare'}, 
        {'Amount': 200, 'Category': 'Entertainment', 'Description': 'Netflix Subscription'} ], 
    'Wednesday': [ 
        {'Amount': 30, 'Category': 'Transport', 'Description': 'Bus fare'}, 
         {'Amount': 30, 'Category': 'Entertainment', 'Description': 'Movie ticket'}] }


def addcd():
    am=int(input("enter the amount:-"))
    c=input("enter the cat:-")
    d=input("enter the des:-")
    expenses['Wednesday'].append({'Amount': am, 'Category': c, 'Description': d})
    
    print(expenses['Wednesday'])
    
    
def newex():
    am=int(input("enter the amount:-"))
    c=input("enter the cat:-")
    d=input("enter the des:-")
    expenses['Thursday']={'Amount': am, 'Category': c, 'Description': d}
    print(expenses)

def genrepcat():
    tg=0
    tt=0
    te=0
    for key,value in expenses.items():
        for j in value:
            if j['Category']=='Groceries':
                tg+=j['Amount']
            if j['Category']=='Transport':
                tt+=j['Amount']
            if j['Category']=='Entertainment':
                te+=j['Amount']
        
    print("Transport:-",tt)
    print("Groceries:-",tg)
    print("Entertainment:-",te)
     
    
def seboted():
    d=input("enter the des:-")
    for key,value in expenses.items():
        for j in value:
            if j['Description']==d:
                print(f"day of expense is ={key}")
                print(f"amount={j['Amount']}")
      
def eaedcd():
    day=input("enter the day to update des")
    for key,value in expenses.items():
        if day in key:
            d=input("enter the des:-")
            expenses[day][0]['Description']=d
    print(expenses)
   
        
while True:
    print("1. Add Expense on Current Day by user input ")
    print("2. Start adding expenses for new day(Thursday) with one single expense.")
    print("3. Generate reports of expenses categories wise")
    print("4. Search Expense based on the expense description ")
    print("5. Edit any expense description of current day ")
    print("6. exit")
    ch=int(input("enter the choice:-"))
    if(ch==1):
        addcd()
    if(ch==2):
        newex()
    if(ch==3):
        genrepcat()
    if(ch==4):
        seboted()
    if(ch==5):
        eaedcd()
        
        
    if(ch==6):
        break;