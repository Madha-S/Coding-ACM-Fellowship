import time
def myfunc():
    start_time=time.time()
    s=0
    for i in range(x+1):
        s=s+i
    end_time=time.time()
    return s, end_time-start_time

x=eval(input("Enter a number>> "))
print(myfunc())