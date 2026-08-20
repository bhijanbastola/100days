import time
def times(func):

    def wrapper():
        print("Calculating Time")
        start=time.time()
        func()
        end=time.time()
        print("completed after",end-start)

    return wrapper

@times
def cal():
  
    for i in range(1,100000):
        print(i)

    
print(cal())