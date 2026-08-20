lst = ['a', 'b', 'c', 'd']

def get_element(index):
  
    return lst[index]
try:
    print(get_element(2))  
    print(get_element(5))  

except IndexError as e:
    print("out of range")
    print(get_element(-1))