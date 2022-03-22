from datetime import date, datetime

def main() :

    today = date.today() 

    today_date = today.strftime("%B %d, %Y") 

    now = datetime.now() 

    time_now = now.strftime("%H:%M:%S") 

    f = open("py_test.txt", "w+", encoding = 'UTF-8')

    f.write("Today's date is {} and time now is {} {}".format(today_date, time_now, '😁'))

    f.close() 

if __name__ == '__main__' :
    main()
