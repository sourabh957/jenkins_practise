# explore the click library 
# parameters, logging level(default = error), what operations do i want to perform, 
# introduce a check so that divide and sub are not called when more than 2 values are passed
#   
import fire
import logging
import click
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

# @click.command()
# @click.argument('--class_attribute')
# @click.argument('numbers', type = [])

class calculator :

    ans = 0
    prev_calculation = 0 
    def __init__(self) :
        self.ans = 0
        self.prev_calculation = 0

    # @click.option('--*args', prompt = 'List passed')
    def add(self, *args) :
        logging.info("The add function is called with these parameters {}".format([a for a in args]))  
        # error and trace
        #remove all print and return the value 
        #reuse the variable
        sum = 0 
        prev_calculation = 1
        for x in args : 
            sum += x 
        print(sum)
        return sum
    
    # def average(self, *args) :
    #     if(prev_calculation == 1) :
    #         return prev_calculation / len(args)
    #     return add(args) / len(args) 

    def mul(self, *args) :
        logging.info("The mul function is called") 
        sum = 1
        for x in args : 
            sum *= x 
        return sum

    def sub(self, a, b) : 
        logging.info("The sub function is called") 
        return (a - b)

    def div(self, a, b) :
        logging.info("The divide function is called") 
        if b == 0 : 
            return ('Divide by zero error')
        return a / b  


if __name__ == '__main__' : 

    fire.Fire(calculator)
    