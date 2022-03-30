
import fire

class calculator :

    ans = 0
    def __init__(self) :
        self.ans = 0

    def add(self, s) :
        l = list(map(int, s.split())) 
        sum = 0 
        for x in l : 
            sum += x 
        print(sum)

    def mul(self, s) :
        l = list(map(int, s.split())) 
        sum = 1
        for x in l : 
            sum *= x 
        print(sum)

    def sub(self, s) : 
        l = list(map(int, s.split()))
        ans = l[0] - l[1] 
        print(ans)

    def div(self, s) :
        l = list(map(int, s.split()))
        a = l[0] 
        b = l[1]
        if b == 0 : 
            print('Divide by zero error')
        else :
            ans = a / b
            print(ans) 


if __name__ == '__main__' : 
    fire.Fire(calculator)
