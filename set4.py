Products= { 'POOI': { 'Name': 'Smartphone', 'Category': 'Electronics', 'Price': 500, 'Description': 'Latest SG smartphone with 128GB storage', 'Stock': 30 }
          ,'POW': { 'Name': 'Microwave', 'Category': 'Home Appliances', 'Price': 150, 'Description': '800W Microwave with touch control', 'Stock': 20 },
          'POF': { 'Name': 'Earbuds', 'Category': 'Electronics', 'Price': 750, 'Description': 'Samsung earbuds', 'Stock': 10},
        'POM': { 'Name': 'Charger', 'Category': 'Electronics', 'Price': 800, 'Description': 'Samsung charger', 'Stock': 12},
        'POV': { 'Name': 'Bottel', 'Category': 'Home Appliances', 'Price': 550, 'Description': 'water bottel', 'Stock': 10}}
review_rating={'P001':{'Review': 'Great smartphone with amazing speed and camera quality.', 'Rating': 5},
               'P002':{'Review': 'Perfect microwave, heats evenly and quickly.', 'Rating': 1}}



def addnewpro():
    print()
    
def addreview():
    for i,j in Products.items():
        review=input(f"enter the review for {i}:-")
        r=input(f"enter the rating for {i}:-")
        Id=i
        review_rating[Id]={'Review': review, 'Rating': r}
        print(review_rating)
        
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
        addnewpro()
    if(ch==2):
        addreview()
    # if(ch==3):
    #     displayall()
    if(ch==4):
        badreviewed()
    if(ch==5):
        break;