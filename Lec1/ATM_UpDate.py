#Initializing Nedded Varibales/Data Types

#list of Tuples
clients_list = [("saad",1234),("mohamed",5678),("fayed",3542)]

#Range used for looping over Number of Tries to Enter UserName , PW
x = range(3)       

#Dictionary for Holding the Avaliable Money in the ATM
ATMdict = {
  "Dollar": 1000 ,
  "Euro": 1000,
  "Yen": 1000,
  "Egyption Pound": 1000
}

def ATM_SYS():
    while True:
        print("1- Show All Avaliable Money In all Currencies")
        print("2- Show Avaliable Money In specific Currency")
        print("3- Withdraw")
        print("4- Deposit")
        print("5- Exit")
        Action = int(input("What Do You Want to do : "))
        if Action == 1:
            print(ATMdict)
        elif Action == 2:
            print("a- Dollar")
            print("b- Euro")
            print("c- Yen")
            print("d- Egyption pound")
            Cur = input("What Currency do you want : ")
            if Cur == 'a':
                print(ATMdict["Dollar"])
            elif Cur == 'b':
                print(ATMdict["Euro"])  
            elif Cur == 'c':
                print(ATMdict["Yen"])
            elif Cur == 'd':
                print(ATMdict["Egyption Pound"])
        elif Action == 3:
            print("a- Dollar")
            print("b- Euro")
            print("c- Yen")
            print("d- Egyption pound")
            Cur = input("What Currency do you want Withdraw From : ")
            if Cur == 'a':
                With_val = int(input("How much Money you want to Withdraw : "))
                ATMdict["Dollar"] -=  With_val
            elif Cur == 'b':
                With_val = int(input("How much Money you want to Withdraw : "))
                ATMdict["Euro"] -=  With_val  
            elif Cur == 'c':
                With_val = int(input("How much Money you want to Withdraw : "))
                ATMdict["Yen"] -=  With_val
            elif Cur == 'd':
                With_val = int(input("How much Money you want to Withdraw : "))
                ATMdict["Egyption Pound"] -=  With_val
        elif Action == 4:
            print("a- Dollar")
            print("b- Euro")
            print("c- Yen")
            print("d- Egyption pound")
            Cur = input("What Currency do you want Deposit to : ")
            if Cur == 'a':
                With_val = int(input("How much Money you want to Deposit : "))
                ATMdict["Dollar"] +=  With_val
            elif Cur == 'b':
                With_val = int(input("How much Money you want to Deposit : "))
                ATMdict["Euro"] +=  With_val  
            elif Cur == 'c':
                With_val = int(input("How much Money you want to Deposit : "))
                ATMdict["Yen"] +=  With_val
            elif Cur == 'd':
                With_val = int(input("How much Money you want to Deposit : "))
                ATMdict["Egyption Pound"] +=  With_val
        elif Action == 5:
            break



print("Welcome to BrokeBank")   #welcoming message

#User Name and PassWard Check Loops
for username_trials in x:
    user_name_flag = 0
    user_name = input("Please Enter Your User Name : ")
    for i in clients_list:
        if user_name == i[0]:
            user_name_flag = 1  
            break
    if user_name_flag==0:
        print("Wrong User Name")   
    else:
        for PassWard_trials in x:
            PassWard_flag = 0
            print("Hello",i[0])
            PassWard = int(input("Please Enter Your PassWard :"))
            if PassWard != i[1]:
                print("Wrong PassWard")  
            else:    
                ATM_SYS()
                break
        break      
