Library = {  'BK001':{
            'BookDetails': { 'Title': 'Python', 'Published': 'Nov-20', 'Price': 790, 'Description': 'Basic and advanced Python' }, 
            'AuthorDetails': { 'PrimaryAuthor': 'Guido Van Rossum', 'CoAuthors': [] },  
            'StockDetails': { 'AvailableCopies': 10, 'TotalCopies': 50, 'IsInStock': True }  }, 
            'BK102': {
            'BookDetails': { 'Title': 'Java', 'Published': 'Jun-18', 'Price': 820, 'Description': 'Servlet in   Java' },  
            'AuthorDetails': { 'PrimaryAuthor': 'Ivan Bayross', 'CoAuthors': ['Cynthia Bayross'] },  
            'StockDetails': { 'AvailableCopies': 0, 'TotalCopies': 25, 'IsInStock': False } } }

def sellingbook():
    bid=input("enter the bookid:-")
    if bid in Library.keys():
        if Library[bid]['StockDetails']['AvailableCopies']==0:
            Library[bid]['StockDetails']['IsInStock']=False
            print("Book is not in stock")
        else:
            Library[bid]['StockDetails']['AvailableCopies']-=1
            print("1 book sold")
            if Library[bid]['StockDetails']['AvailableCopies']==0:
                Library[bid]['StockDetails']['IsInStock']=False
            else:
                Library[bid]['StockDetails']['IsInStock']=True
                
                
            
    else:
        print("book not found")
    
def displayall():
    for key,value in Library.items():
        bk=value['BookDetails']
        ad=value['AuthorDetails']
        sd=value['StockDetails']
        print(f"Book id:-{key}")
        print(f"title:-{bk['Title']}")
        print(f"publised:-{bk['Published']}")
        print(f"Price:-{bk['Price']}")
        print(f"Description:-{bk['Description']}")
        print(f"primary Author :-{ad['PrimaryAuthor']}")
        print(f"co author :-{ad['CoAuthors']}")
        print(f"available copies :-{sd['AvailableCopies']}")
        print(f"Total copies :-{sd['TotalCopies']}")
        print(f"is in stock :-{sd['IsInStock']}\n")

        
        
def restockbook():
        bid=input("enter the bookid:-")
        if bid in Library.keys():
            if Library[bid]['StockDetails']['AvailableCopies']==0:
                Library[bid]['StockDetails']['AvailableCopies']+=1
                print("1 book added")
                Library[bid]['StockDetails']['IsInStock']=True  
                
            else:
                    Library[bid]['StockDetails']['IsInStock']=False
                 
        else:
            print("book not found")
            
def purchasenewbook():
    bt=input("Enter the book title:-")
    pd=input("enter the publised date eg, nov-20:-")
    price=int(input("enter the price:-"))
    des=input("enter the description:-")
    pa=input("enter the primary author:-")
    ca=input("enter the coauthor:-")
    ac=input("enter the available copies:-")
    tc=input("enter the total copies:-")
    isins=input("enter the stock status eg,True,False:-")
    
    key=Library.keys()
    key=list(key)
    Id=key[-1]
    Id=Id.split("K")
    Id=Id[1]
    Id=int(Id)
    Id+=1
    Id=str(Id)
    Id="BK"+Id
    
    Library[Id]={'BookDetails':{'Title':bt,'Published':pd,'Price':price,'Description':des},
                 'AuthorDetails':{'PrimaryAuthor':pa,'CoAuthors':[ac]},
                 'StockDetails':{'AvailableCopies':ac,'TotalCopies':tc,'IsInStock':isins}}
    print("record Inserted")
    
def checkstock():
    for i in Library:
        sd=Library[i]['StockDetails']
        print("stock status of",i,"is ",sd['IsInStock'])
        
while(True):
    ch=0
    print("1. selling book")
    print("2. purchase book")
    print("3. restock a book")
    print("4. check stock")
    print("5. display book")
    print("6. Exit")
    ch=int(input("Enter the choice:-"))
    if(ch==1):
        sellingbook()
    if(ch==2):
        purchasenewbook()
    if(ch==3):
        restockbook()
    if(ch==4):
       checkstock()
    
    if(ch==5):
       displayall()
    if(ch==6):
        break
    
    