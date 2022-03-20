import sys

def multiply(a = 0, b = 0) :
    A = int(a) 
    B = int(b) 
    print(A * B)

if __name__ == '__main__' :
    args = sys.argv
    
    globals()[args[1]](*args[2:])