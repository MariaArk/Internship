import datetime


def date_in_future(integer):
    time = datetime.datetime.now()
    time1 = datetime.datetime.strftime(time, '%d-%m-%Y %H:%M:%S')
    if type(integer) != int:
        return time1
    day = datetime.timedelta(days=integer)
    time = time + day
    time1 = datetime.datetime.strftime(time, '%d-%m-%Y %H:%M:%S')
    return time1


x = date_in_future([])
print(x)

x = date_in_future(2)
print(x)