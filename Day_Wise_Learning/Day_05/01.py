def get_cubes(numbers):
    return numbers **3

ls=[1,2,3,4,5]
maped_cubes=map(get_cubes,ls)
#print(list(maped_cubes))

filtered_cubes=filter(lambda x:x%2==0,maped_cubes)
print(list(filtered_cubes))


from functools import reduce
def add(x,y):
    return x+y

list1=[1,2,3,4,5]
result=reduce(add,list1)
print(result)

