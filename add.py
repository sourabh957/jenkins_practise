import sys

def add(a = 0, b = 0) :
    A = int(a) 
    B = int(b) 
    print(a + b) 

if __name__ == '__main__' :
    args = sys.argv
    
    globals()[args[1]](*args[2:])
