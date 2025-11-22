
def print1(*args):
    print(args)


print1(1,2,3,4)

def add(*args: int):
    print(sum(args))
    print(args[2])


add(1, 2, 3, 4, 5)

def calculate(**kwargs):
    print(kwargs)


calculate(a=1, b="steve")
