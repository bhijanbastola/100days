number=56

if isinstance(number,int):
    print(f'Squared root : {number**0.5}')

else:
    raise TypeError(f"value should be of int,not {type(number)}")


def divide(x,y):
    if y==0:
        raise ValueError("cannot divide by 0")

    return x/y

divide(2,0)