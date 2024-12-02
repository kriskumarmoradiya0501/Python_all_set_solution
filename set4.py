Products= { 'POOI': { 'Name': 'Smartphone', 'Category': 'Electronics', 'Price': 500, 'Description': 'Latest SG smartphone with 128GB storage', 'Stock': 30 }
          ,'POW': { 'Name': 'Microwave', 'Category': 'Home Appliances', 'Price': 150, 'Description': '800W Microwave with touch control', 'Stock': 20 },
          'POF': { 'Name': 'Earbuds', 'Category': 'Electronics', 'Price': 750, 'Description': 'Samsung earbuds', 'Stock': 10},
        'POM': { 'Name': 'Charger', 'Category': 'Electronics', 'Price': 800, 'Description': 'Samsung charger', 'Stock': 12},
        'POV': { 'Name': 'Bottel', 'Category': 'Home Appliances', 'Price': 550, 'Description': 'water bottel', 'Stock': 10}}
review_rating={'P001':{'Review': 'Great smartphone with amazing speed and camera quality.', 'Rating': 5},
               'P002':{'Review': 'Perfect microwave, heats evenly and quickly.', 'Rating': 1}}



def addnewproduct():
    pn=input("Enter the p  name:-")
    cat=input("enter the publised date eg, nov-20:-")
    price=int(input("enter the price:-"))
    des=input("enter the description:-")
    stock=input("enter the primary author:-")
    
    key=Products.keys()
    key=list(key)
    Id=key[-1]
    Id=Id.split("P")
    Id=Id[1]
    Id=int(Id) 
    Id+=1
    Id=str(Id)
    Id="P"+Id
    
    Products[Id]={'Name':pn,'Category':cat,'Price':price,'Description':des,'Stock':stock}
    print("record Inserted")
    
def addprorev():
    pro=input("enter the product id:-")
    product_found=False
    for j in Products.items():
        if j[0]==pro:
            product_found=True
            if product_found:
                review=input("Enter your feedback")
                rating=int(input(f"rating of {pro}:-"))
                review_rating[pro]={'Review':review,'Rating':rating}
                    
    if not product_found:
            print("invalid id")

def DisplayAll():
    for key,value in Products.items():
        print(Products[key]['Name'])
        print(Products[key]['Category'])
        print(Products[key]['Price'])
        print(Products[key]['Description'])
        print(Products[key]['Stock'])
        if key in review_rating.keys():
            print(review_rating[key]['Review'])
            print(review_rating[key]['Rating'])


# def addreview():
#     for i,j in Products.items():
#         review=input(f"enter the review for {i}:-")
#         r=input(f"enter the rating for {i}:-")
#         Id=i
#         review_rating[Id]={'Review': review, 'Rating': r}
#         print(review_rating)
        
def badreviewed():
    for i,j in review_rating.items():
        if j['Rating']<2.5:
            print(i,"is",j['Rating'],"rated")

    

while True:
    print("1. add new product")
    print("2. add review and rating")
    print("3. display all record")
    print("4. generate report ")
    print("5. exit")
    ch=int(input("enter the choice:-"))
    if(ch==1):
        addnewproduct()
    if(ch==2):
        addprorev()
    if(ch==3):
         DisplayAll()
    if(ch==4):
        badreviewed()
    if(ch==5):
        break;
