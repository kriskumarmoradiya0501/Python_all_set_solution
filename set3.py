Products={'P001': { 'Name': 'Smartphone', 'Category': 'Electronics', 'Price': 500, 'Description': 'Latest SG smartphone with 128GB storage', 'Stock': 10},  
            'P002': { 'Name': 'Microwave', 'Category': 'Home Appliances', 'Price': 150, 'Description': '800W Microwave with touch control', 'Stock': 20 },
            'P003': { 'Name': 'Earbuds', 'Category': 'Electronics', 'Price': 750, 'Description': 'Samsung earbuds', 'Stock': 10},
          'P004': { 'Name': 'Charger', 'Category': 'Electronics', 'Price': 800, 'Description': 'Samsung charger', 'Stock': 12},
          'P005': { 'Name': 'Bottel', 'Category': 'Home Appliances', 'Price': 550, 'Description': 'water bottel', 'Stock': 10}}
cart={}

def addcart():
    pro=input("enter the product id to add in cart eg.001,002:-")
    List=pro.split(',')
    for i in List:
        product_found=False
        for j in Products.items():
            if j[0]==i:
                product_found=True
                if product_found:
                    qty=int(input(f"enter the quantity {i}:-"))
                    if qty>Products[i]['Stock']:
                        print("product qty is out of stock")
                    else:
                        cart[i]=qty
                        
        if not product_found:
            print("invalid id")

def viewcart():
    print("productname   Price      qty        ta")
    for key,value in Products.items():
        if key in cart.keys():
            ta=Products[key]['Price']*cart[key]
            print(Products[key]['Name'],"\t\t",Products[key]['Price'],"\t\t",cart[key],"\t\t",ta)
        
        
def removeproduct():
    
    if not cart:
        print("cart is empty")
    else:
        pro=input("enter the product id to remove in cart :-")
        if pro in cart.keys():
            cart.pop(pro)
            print(pro,"is removed")
        else:
            print("product is not their")

def bill():
    tbill=0
    for Key,value in cart.items():
        ta=Products[Key]['Price']*cart[Key]
        tbill+=ta
        Products[Key]['Stock']-=cart[Key]
    if tbill<=0:
        print("no product")
    else:
        print("total bill=",tbill)
        print(Products)
        cart.clear()
        
while True:
    print("1. add to  cart")
    print("2. view cart ")
    print("3. remove product")
    print("4. buy from cart")
    print("5. exit")
    ch=int(input("enter the choice:-"))
    if(ch==1):
        addcart()
    if(ch==2):
        viewcart()
    if(ch==3):
        removeproduct()
    if(ch==4):
        bill()
    if(ch==5):
        break;