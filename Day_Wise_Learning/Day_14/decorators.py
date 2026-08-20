#Implementation 

def decorator(func):
    def wrapper():
                
        print("Before Function Call")
        print(func().upper()) #<- Actual Function Call
        print("After Function Call")

    return wrapper

@decorator
def greet():
    return "hello world"

greet()