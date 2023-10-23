# def add(n1,n2):
#     return n1+n2
# print(add(100,200))

# def sub(n1,n2):
#     return n1-n2
# print(sub(10,2))

# def product(n1,n2):
#     return n1*n2
# print(product(5,10))

# def cube(n):
#     return n**3
# print(cube(3))

# def div(n1,n2):
#     return n1/n2
# print(div(2,8))

# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(smart_sub(5,15))

# def leap_year(n1):
#     if(n1%)
    
year=int(input("enter a number"))
def leapyear(year):
    if year%100==0 and year%400==0:
        return "leap year"
    elif year%100!=0 and year%4==0:
        return "leap year"
    else:
        return "not leap year"
print(leapyear(year))
    


