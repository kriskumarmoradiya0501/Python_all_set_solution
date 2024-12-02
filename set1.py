Library = {
         'BK001': {
             'BookDetails': ['python', 'Nov-20', 790, 'Basic and advance python'],
             'AuthorDetails': ['guido Van']},
         'BK102': {
             'BookDetails': ['Java', 'Jun-18', 790, 'servlet in java'],
             'AuthorDetails': ['Ivan Bayross', 'cynthia Bayross']},
   
        'BK103': {
            'BookDetails': ['C++', 'Mar-15', 650, 'Object-Oriented Programming with C++'],
            'AuthorDetails': ['Bjarne Stroustrup']},
        'BK104': {
            'BookDetails': ['JavaScript', 'Jan-22', 550, 'Modern JavaScript: ES6 and Beyond'],
            'AuthorDetails': ['Kyle Simpson']},
        'BK105': {
            'BookDetails': ['Data Science', 'Aug-21', 1200, 'Introduction to Data Science'],
            'AuthorDetails': ['Joel Grus']}
}
def addnew():
    bid=input("enter the bookid:-")
    bname=input("enter the book name:-")
    date=input("Enter the released date:-")
    price=int(input("Enter the price:-"))
    des=input("Enter the book description:-")
    author=input("Enter the author details:-")
    
    Library[bid]={'BookDetails':[bname,date,price,des],'AuthorDetails':[author]}
    
def modifyrecord():
    bid=input("enter the bookid:-")
    
    if bid in Library.keys():
        price=int(input("Enter the price to Change:-"))
        for i in Library:
            Library[bid]['BookDetails'][2]=price
    else:
        print("book not found")
        
def removeauthorname():
    bid=input("enter the bookid:-")
    name=input("enter the author name:-")
    
    if bid in Library.keys() and  name in Library[bid]['AuthorDetails']:
        Library[bid]['AuthorDetails'].remove(name)
        print("author name deleted")
    else:
        print("name not found")
        
def searchbook():
    des=input("Enter the book description:-")
    for key,value in Library.items():
        BookDetails=value['BookDetails']
        AuthorDetails=value['AuthorDetails']
        vb=",".join(AuthorDetails)
        if des.lower() in BookDetails[3].lower():
            print(f"book id={key}")
            print(f"bookname={BookDetails[0]}")
            print(f"Publised date={BookDetails[1]}")
            print(f"price={BookDetails[2]}")
            print(f"Description={BookDetails[3]}")
            print(f"Authorname={vb}")
        else:
            print("des not found")
       
        
def printall():
    for key,value in Library.items():
        BookDetails=value['BookDetails']
        AuthorDetails=value['AuthorDetails']
        vb=",".join(AuthorDetails)
        print("==============================")
        print(f"book id={key}")
        print(f"bookname={BookDetails[0]}")
        print(f"Publised date={BookDetails[1]}")
        print(f"price={BookDetails[2]}")
        print(f"Description={BookDetails[3]}")
        print(f"Authorname={vb}")
        print("==============================")

while(True):
    ch=0
    print("1. add new")
    print("2. modify record")
    print("3. remove author name")
    print("4. search book")
    print("5. print all book")
    print("6. Exit")
    ch=int(input("Enter the choice:-"))
    if(ch==1):
        addnew()
    if(ch==2):
        modifyrecord()
    if(ch==3):
        removeauthorname()
    if(ch==4):
        searchbook()
    
    if(ch==5):
        printall()
    
    if(ch==6):
        break
    
    
    
    
    