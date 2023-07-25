import cProfile
def add(x,y):
    return x+y

n,m=eval(input("Enter the numbers>> "))
cProfile.run('add()')