# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:46:58 2024

@author: 8student1
"""

saving = [[1001,"Krish",5000],[1002,"Harsh",10000]]

current = [[2001,"Krish",500000],[2002,"Smit",1000]]

while True:
    print("Enter 1 if you have saving account")    
    print("Enter 2 if you have current account")
    print("Enter 3 if you want to exit")
    ch = int(input("Enter Your choice : "))
    
    if ch == 1:
        ano = int(input("Enter Your account NO : "))
        for i in saving:
            if ano == i[0]:
                acco = i
                break
            else :
                print("Not Found")
                print("for you account oppening")
                a=ano
                b = input("Enter Your Name : ")
                c = int(input("Enter Your first deposite"))  
                saving.append([a,b,c])
                acco=([a,b,c])
                
        print(acco)
        print("Enter 1 for check current balance")
        print("Enter 2 for deposite")
        print("Enter 3 for  withdraw")
        print("Enter 4 for interest")
        print("Enter 5 for exit")     
        cho = int(input("Enter Your choice : "))
        if cho == 1:
            print("Your current balance  = ",acco[2])
            
        elif cho == 2:
            dep = int(input("Enter Amount to deposite : "))
            acco[2] = acco[2]+dep
            
        elif cho == 3:
            wid = int(input("Enter Your widthdraw Ammount :"))
            if wid > acco[2]:
                print("You have not sufficiant balance")
                
            else:
                acco[2] = acco[2]-wid
        elif cho == 4:
            interest = (acco[2]*10)/100
            print("interest",interest)
        else:
            print("Not Found")
            print("for you account oppening")
            a=ano
            b = input("Enter Your Name : ")
            c = int(input("Enter Your first deposite"))  
            saving.append([a,b,c])
            acco=([a,b,c])
    elif ch == 2:
        ano = int(input("Enter Your account NO : "))
        for i in current:
            if ano == i[0]:
                acco = i
                break
            else :
                print("Not Found")
                print("for you account oppening")
                a=ano
                b = input("Enter Your Name : ")
                c = int(input("Enter Your first deposite"))  
                saving.append([a,b,c])
                acco=([a,b,c])
                break
        print(acco)
        print("Enter 1 for check current balance")
        print("Enter 2 for deposite")
        print("Enter 3 for  withdraw")
        print("Enter 4 for interest")
        print("Enter 5 for exit")     
        cho = int(input("Enter Your choice : "))
        if cho == 1:
            print("Your current balance  = ",acco[2])
            
        elif cho == 2:
            dep = int(input("Enter Amount to deposite : "))
            acco[2] = acco[2]+dep
            
        elif cho == 3:
            wid = int(input("Enter Your widthdraw Ammount :"))
            if wid > acco[2]:
                print("You have not sufficiant balance")
                
            else:
                acco[2] = acco[2]-wid
        elif cho == 4:
            interest = (acco[2]*10)/100
            print("interest",interest)
    elif ch == 3:
        print("exit")
        break
    