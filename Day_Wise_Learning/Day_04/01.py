# # variable length arguments
# # def print_values(*args):
# #     for arg in args:
# #         print(arg)

# # print_values(1, 2, 3, 4, 5)

# # def print_all(*args):
# #     return sum(args)

# # print(print_all(1,2,3,4,5,6,7,8,9,10))

# from cmath import sqrt


# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")  

# print(print_values(name="Alice", age=30, city="New York"))


# def calculate_area(shape:str,**kwargs):
#     if shape=="square":
#         side = kwargs.get("length", 0)
#         return side * side
#     elif shape=="rectangle":
#         length = kwargs.get("length", 0)
#         width = kwargs.get("width", 0)
#         return length * width

# print(calculate_area("square", length=5))




# def SD1(numbers):

#     """_summary_

#     Returns:
#         _type_: _description_
#     """
#     n=len(numbers)
#     mean=sum(numbers)/n
#     sd=sqrt(sum((x-mean)**2 for x in numbers)/n)
#     return round(sd, 2)

# while True:
#     numbers = input("Enter numbers separated by spaces: ")
#     number_list = [float(num) for num in numbers.split()]
#     print("Standard Deviation:", SD1(number_list))
#     choice=input("Do you want to continue ? (y/n)").lower().strip()
#     if choice=='n':
#         break


power=lambda base,power :base**power
print(power(2,3))

##area of cuboid
area =lambda length,breadth,height : 2*(length*breadth + breadth*height + height*length)
print(area(20,22,5))