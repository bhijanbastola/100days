#Generators
def num_generator(start,end):
    for num in range(start,end+1):
        yield num


gen=num_generator(15,25)

for num in gen:
    print(num)

