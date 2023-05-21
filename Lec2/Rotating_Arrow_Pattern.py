import time 
import os
       
def arrow_Left(n):
    for i in range(1,n):
        print(' ' * ((n-i)*2)+'*')       
    print('* ' * ((n*2)-1))      
    for i in range(n-1,0,-1):
        print(' ' * ((n-i)*2)+'*')
           
def arrow_Right(n):
    count1 = ((n-1)*2)
    count2 = ((n*4)-6)
    for i in range(1,n):
        print('  '*(n+3) + ' ' * (count1)+'*')    
        count1 += 2    
    print('  '*(n+3) + '* ' * ((n*2)-1))      
    for i in range(n-1,0,-1):
        print('  '*(n+3) + ' ' * (count2)+'*')    
        count2 -= 2
        
def arrow_Down(n):
    for i in range(n-1):
        print(' '*(n+1) + '  '*n+'*')
    for j in range(1,n):
        print(' '*(n+1) + '  '*((j)-1)+'* ' + '  '*(n-j)+'*' + '  '*(n-j)+' *')
    print(' '*(n+1) + '  '*n+'*')  
    
def arrow_Up(n):
    print('  '*(n-2) + '  ' * n + '*' )
    for i in range(n-1,0,-1):
        print('  '*(n-2) + '  '*(i-1)+'* ' + '  '*(n-i)+'*' + '  '*(n-i)+' *')
    for i in range(n-1):
        print('  '*(n-2) + '  '*n+'*')
        
n = 5
while True:	  
    Direction = int(input("1 ==> Rotate Right\n2==> Rotate Left\nEnter Direction Of Rotation : "))
    Duration = int(input("Enter Duration Time in Sec : "))
    end_t = time.time() + Duration
    if(Direction == 1):
        while (time.time() < end_t):
            print("\n"*(n+1))
            arrow_Left(n)
            time.sleep(0.1)  
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"*(n-3))
            arrow_Up(n)
            time.sleep(0.1)  
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"*(n+1))
            arrow_Right(n)
            time.sleep(0.1) 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"*(n*2))
            arrow_Down(n) 
            time.sleep(0.1) 
            os.system('cls' if os.name == 'nt' else 'clear')  
    elif(Direction == 2):
        while (time.time() < end_t):
            print("\n"*(n+1))
            arrow_Left(n)
            time.sleep(0.1)  
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"*(n*2))
            arrow_Down(n) 
            time.sleep(0.1) 
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("\n"*(n+1))
            arrow_Right(n)
            time.sleep(0.1) 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"*(n-3))
            arrow_Up(n)
            time.sleep(0.1)  
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Invalid Entry")
           
            