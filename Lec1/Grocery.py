#Initializing Nedded Varibales/Data Types

#Dictionary to Hold grocery Profits
porfitdic= {
  "Gain": 0 ,
  "Spend": 0,
  "Net_Profit": 0,
}

#Dictionary for Holding the Avaliable goods in the grocery
GRCdict = {
  "Banana": 1000 ,
  "Apple": 1000,
  "Egg": 1000,
  "Tomato": 1000
}

#Dictionary for Holding the Prices 
PRICEdict = {
  "Banana": 5 ,
  "Apple": 10,
  "Egg": 1,
  "Tomato": 3
}

while True:
    print("1- Show All Avaliable goods")
    print("2- Show All Prices")
    print("3- Remove Goods")
    print("4- Add Goods")
    print("5- Show Profits")
    print("6- Exit")
    Action = int(input("What Do You Want to do : "))
    if Action == 1:
        print(GRCdict)
    elif Action == 2:  
        print(PRICEdict)
    elif Action == 3:
        print("a- Banana")
        print("b- Apple")
        print("c- Egg")
        print("d- Tomato")
        Cur = input("What Product you want to choose: ")
        if Cur == 'a':
            amount = int(input("How many Banana you want to remove : "))
            GRCdict["Banana"] -=  amount
            porfitdic["Gain"] = PRICEdict["Banana"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"]          
        elif Cur == 'b':
            amount = int(input("How many Apple you want to remove : "))
            GRCdict["Apple"] -=  amount
            porfitdic["Gain"] = PRICEdict["Apple"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"] 
        elif Cur == 'c':
            amount = int(input("How many Egg you want to remove : "))
            GRCdict["Egg"] -=  amount
            porfitdic["Gain"] = PRICEdict["Egg"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"]
        elif Cur == 'b':
            amount = int(input("How many Tomato you want to remove : "))
            GRCdict["Tomato"] -=  amount
            porfitdic["Gain"] = PRICEdict["Tomato"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"]
    elif Action == 4:
        print("a- Banana")
        print("b- Apple")
        print("c- Egg")
        print("d- Tomato")
        Cur = input("What Product you want to choose: ")
        if Cur == 'a':
            amount = int(input("How many Banana you want to add : "))
            GRCdict["Banana"] +=  amount
            porfitdic["Spend"] = PRICEdict["Banana"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"]          
        elif Cur == 'b':
            amount = int(input("How many Apple you want to add : "))
            GRCdict["Apple"] +=  amount
            porfitdic["Spend"] = PRICEdict["Apple"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"] 
        elif Cur == 'c':
            amount = int(input("How many Egg you want to add : "))
            GRCdict["Egg"] +=  amount
            porfitdic["Spend"] = PRICEdict["Egg"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"]
        elif Cur == 'b':
            amount = int(input("How many Tomato you want to add : "))
            GRCdict["Tomato"] +=  amount
            porfitdic["Spend"] = PRICEdict["Tomato"] * amount
            porfitdic["Net_Profit"] = porfitdic["Gain"] - porfitdic["Spend"]        
    elif Action == 5:  
        print(porfitdic)
    elif Action ==6:
        break    