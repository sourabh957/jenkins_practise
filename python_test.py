
import fire
import logging

logging.basicConfig(format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger(__name__)

# logger.setLevel(logging.DEBUG)

class calculator :

    ans = 0
    def __init__(self) :
        self.ans = 0

    def checkLevel(s) : 
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')

    def setDebugLevel(self, *args) : 
        s = str(args[0])
        # print(s)
        if s.upper() == 'CRITICAL':
            print("test")
            logger.setLevel(logging.CRITICAL)
        if s.upper() == 'ERROR':
            logger.setLevel(logging.ERROR)
        if s.upper() == 'INFO':
            logger.setLevel(logging.INFO)
        if s.upper() == 'DEBUG':
            logger.setLevel(logging.DEBUG)
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')

    def add(self, *args) :
        logging.info("The add function is called") 
        sum = 0 
        for x in args : 
            sum += x 
        return sum

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
        else :
            ans = a / b
            return (ans) 


if __name__ == '__main__' : 

    fire.Fire(calculator)
    