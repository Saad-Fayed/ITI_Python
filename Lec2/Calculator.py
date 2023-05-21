ModeList = '''
1 ==> Programmer Mode
2 ==> Scientific Mode
'''
POPList = '''
&  ==> And
|  ==> OR
^  ==> XOR
~  ==> Not
>> ==> Shift Right
<< ==> Shift Left
'''
SOPList ='''
+  ==> Add 
-  ==> Subtraction
*  ==> Multiplication
/  ==>Division
%  ==> Modulus 
** ==>Exponintiation
// ==>Floor Division
'''

def ScientificMode():
    print(SOPList)

    while True:
        print("Enter Operation : ")
        Num1 , Op , Num2 = input().split(" ",3)
        Num1 = int(Num1)
        Num2 = int(Num2)

        if Op == '+':     #Add operation
            print("Result is : ",Num1+Num2)
        elif Op == '-':   #Sub operation
            print("Result is : ",Num1-Num2)
        elif Op == '*':   #Mul operation
            print("Result is : ",Num1*Num2)
        elif Op == '/':   #Div operation
            if Num2 == 0:
                print("Math Error Can't Devide by Zero")
            else:
                print("Result is : ",Num1/Num2)
        elif Op == '%':   #Modulus operation
            print("Result is : ",Num1%Num2)
        elif Op == '**':   #Exponintiation operation
            print("Result is : ",Num1**Num2)
        elif Op == '//':   #Floor Division operation
            print("Result is : ",Num1//Num2)
        else:
            break

def ProgrammerMode():
    print(POPList)
    while True:
        print("Enter Operation : ")
        Num1 , Op , Num2 = input().split(" ",3)
        Num1 = int(Num1)
        Num2 = int(Num2)

        if Op == '&':     #And operation
            print("Result is : ",Num1&Num2)
        elif Op == '|':   #OR operation
            print("Result is : ",Num1|Num2)
        elif Op == '^':   #XOR operation
            print("Result is : ",Num1^Num2)
        elif Op == '~':   #NOT operation
            print("Result is : ",~Num1)
        elif Op == '>>':   #Shift Right operation
            print("Result is : ",Num1>>Num2)
        elif Op == '<<':   #Shift Left operation
            print("Result is : ",Num1<<Num2)
        else:
            break


while True:
    print(ModeList)

    select = int(input("Please Enter the Mode you Want : "))
    if (select == 1):
        ProgrammerMode()
    elif(select == 2):
        ScientificMode()
    else:
        print("Invalid Entry")





