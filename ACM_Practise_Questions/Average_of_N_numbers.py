num=eval(input("Enter required number for average calculation: "))
add=0
for i in range(num):
    integers=eval(input("Enter the numbers>> "))
    add+=integers
print(f'Average of required numbers is ', add/num)