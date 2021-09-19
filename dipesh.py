print("Welcome to Dipesh Bank")


restart = ('y')
chance = 3
balance = 900
while chance >=0:
    pin=int(input("Please enter tyour 4 digit pin: "))
    if pin == (1234):
        print("You enter your pin correctly\n")
        while restart not in('n',"No","no","N"):
            print("Please press 1 for balance\n")
            print("Please press 2 for withdrawal\n")
            print("Please press 3 for pay in\n")
            print("Please press 4 for return your card\n")
            option = int(input("What would you like to choose?: "))
            if option==1:
                print("your balance is $",balance,'\n')
                restart = input("Would you like to go back: ")
                if restart in ('n','No','no','N'):
                    print("Thank you for banking with Dipesh")
            elif option ==2:
                option2 = ("y")
                withdrawl = float(input("How much would you like to withdraw \n$10/$20/$30/$40/$50/$60/$70/$80/$90/100/200/300/400/500/600/700/800/900 for other input :" ))
                if withdrawl in  [10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900]:
                    balance = balance - withdrawl
                    print("\n your balance is now $", balance)
                    restart = input("What would you like to do : ")
                    if restart in ('n','NO','no','N'):
                        print("Thank you for banking with Dipesh bank")
                        break

                elif  withdrawl != [10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900]:
                    print("invalid amount, please re-try\n")
                    restart =('y')
                elif withdrawl ==1:
                    withdrawl = float(input("Please enter your desidre amount: "))
            elif option==3:
                pay_in = float(input("How much woild you like to pay in: "))
                balance = balance+pay_in
                print("\n Your balance is now in $", balance)
                restart = input("Would you like you go back?: ")
                if restart in ('n',"No",'N',"no"):
                    print("Thank you for banking with Dipesh:")
                    break
            elif option==4:
                print("Print Wait while your card is return...\n")
                print("Thank you for banking with Dipesh")
                break
            else:
                print("Please enter the correct number: \n")
                restart = "Y"
    elif pin!=("1234"):
        print("Incorrect password")
        chance = chance-1
        if chance==0:
            print('\n No More tries, contact dipeshkarki6612@gmail.com ')
            break

