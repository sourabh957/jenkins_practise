import sys

def divide(a = 0, b = 1) :
    A = int(a) 
    B = int(b) 

    if B == 0 :
        print('Divide by zero error') 
    else :
        print(A / B) 

if __name__ == '__main__' :
    args = sys.argv
    
    globals()[args[1]](*args[2:])