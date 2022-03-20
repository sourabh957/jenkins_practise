import sys

def sub(a, b) :
    A = int(a)
    B = int(b)
    print(A - B) 

if __name__ == '__main__' :
    args = sys.argv
    
    globals()[args[1]](*args[2:])