print("*************************************")

customernames = ['naveen','phani','sagar','srinu','kumar']
customerpins = ['9745','1245','6300','9666','1238']
customersbalance = [1000,9998.9,1110,5000,7000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0


while True:

    print("***********************************************************************")

    print("=--------------WELCOME TO STATE BANK OF INDIA-------------------------=")

    print("=======================================================================")

    print("<<<<<<<<<<<<<<< 1.OPEN A NEW ACCOUNT-----------------------------------")

    print("<<<<<<<<<<<<<<< 2.WITHDRAWAL MONEY----------------------------------------")

    print("<<<<<<<<<<<<<<< 3.DEPOSIT MONEY-------------------------------------")

    print("<<<<<<<<<<<<<<< 4.CHECK THE BALANCE & CUSTOMERS------------------------")

    print("<<<<<<<<<<<<<<< 5.EXIT-------------------------------------------------")

    print("***********************************************************************")


    choiceNumber = input("Select any  number from above words :- ")
    if choiceNumber == "1":
        print("choice number 1 is selected by the customers")
        NOC = eval(input("Number of customers : "))
        i=i+NOC

        if i > 5:
            print("\n")
            print("customer registration exceed maximum limit")
            i=i - NOC
        else:
            while counter_1 <= i:
                name = input("Input FullName :- ")
                customernames.append(name)
                pin = str(input("enter your account pin number :- "))
                customerpins.append(pin) 
                balance = 0
                deposition = eval(input("Enter the money for sendig to your bank account"))
                balance =deposition + balance
                customersbalance.append(balance)
                print("\n NAME = ", end = "")
                print(customernames[counter_2])
                print("pin = ", end= "")
                print(customerpins[counter_2])
                print("balance = ", end = "")
                print(customersbalance[counter_2], end= "")
                print("-/RS")
                counter_1 = counter_1+1
                counter_2 = counter_2+1  
                print("\n YOUR NAME IS ADDED TO CUSTOMERS SYSTEM")
                print("\n YOUR PIN IS ADDED TO CUSTOMERS SYSTEM")
                print("\n YOUR BALANCE IS ADDED TO CUSTOMERS SYSTEM")
                print("------===== NEW ACCOUNT CREATED SUCCESSFULLY=====-----")     
                print("\n")
                print("your name  is availbale on the customers list now : ")
                print(customernames)
                print("\n")
                print("NOTE! Please remember the name and pin") 
                print("---------------------------------------")

        mainMenu = input("please press enter key to go back to the main menu :-")
    elif choiceNumber == "2":
        j = 0
        print("choice number 2 is selected by the customer")
        while j < i:
            k = -1
            name = input("please input name : ")
            pin = input("please enter your pin :- ")

            while k < len(customernames) - 1:
                k = k+1
                
                if name == customernames[k]:
                    if pin == customerpins[k]:
                        j = j+1
                        print("yourcurrent balance:- ",end = " ")
                        print(customersbalance[k], end = " ")
                        print("-/RS\n")
                        balance = (customersbalance[k])
                        withdrawal = eval(input("input value to withdrawal the money:- "))
                        if withdrawal > balance:
                            deposition = eval(input("please deposit a higher value bacause your balance mentioned above is not enough:- "))
                            balance  = balance + deposition
                            print("your balance :- ",end = " ")
                            print(balance, end = "")
                            print("-/RS\n")
                            balance = balance - withdrawal
                            print("-/n")
                            print("***********************WITHDRAWAL SUCCESSFULL***************")
                            customersbalance[k] = balance
                            print("your new balance:-",6*" ",balance,end =" ")
                            print("-/RS\n\n")
            if j < 1:
                print("your name and pin does not match! \n")
                break
        mainMenu = input("please press enter key to go back to mani menu:- ")
    elif choiceNumber == "3":
        print("choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k = -1
            name = input("enter your name :- ")
            pin = input("enter your pin:- ")
            while k < len(customernames) - 1:
                k = k + 1
                if name == customernames[k]:
                    if pin == customerpins[k]:
                        n = n + 1
                        print("your balance:-", end =" ")
                        print(customersbalance[k],end =" ")
                        print("-/RS\n")
                        balance =(customersbalance[k])
                        deposition = eval(input("Enter your value want to deposit the money:- "))
                        balance = balance +deposition
                        customersbalance[k] = balance
                        print("\n")
                        print("************************DEPOSIT SUCCESSFULL !***********************")
                        print("your balance:-",9*" " ,balance,end ="")
                        print("-/RS\n\n")
            if n < 1:
                print("your name and pin does not match !\n")
                break
        mainMenu = input("please press enter key to back to main menu:- ")
    elif choiceNumber == "4":
        print("choiceNumber 4 is selected by the customer")
        k = 0
        print("customer name list and balance mentioned below:-")
        print("\n")
        while k <=len(customernames) - 1:
            print("*** < -.customer =",customernames[k])
            print("*** < -.balance =", customersbalance[k], end = " ")
            print("-/RS")
            print("\n")
            k = k + 1
        mainMenu = input("please enter any key to go backt o the mainmenu :- ")
    elif choiceNumber == "5":
        print("choice number is 5 is selected by the customer")
        print("thank you for using our banking system")
        print("\n")
        print("come again")
        print ("******************************THANK YOU****************************")
        break
    else:
        print("invalid option selected by the customer")
        print("please try again")
        mainMenu = input("please press enter key tom go back to main menu:- ")
