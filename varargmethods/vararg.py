# def add(*args):
#     res = 0  # Initialize the result to zero
#     for n in args:
#         res += n  # Add each argument to the result
#     return res  # Return the final result

# print(add(10, 20,30,50,60,80))

# def product(*args):
#     res=1
#     for n in args:

#         res*=n
#     return res

# print(product(10,20,40))

# def adder(*args):
#     return sum(args)

# num = input("Enter numbers separated by commas: ")
# num_list = [int(x) for x in num.split(",")]  # Split the input and convert to integers
# result = adder(*num_list)  # Pass the list of numbers to the adder function

# print(f"The sum of the numbers is: {result}")


# def cocat(*args):
#     res=""
#     for sg in args:
#         res+=sg
#     return res
# print(cocat("hello","hiii"))

# def concat(*args):

#     return " ".join(args)

# print(concat("hello","hii","good"))

# def rev_cocat(*args):
#     data=list(args)
#     data.reverse()
#     return " ".join(data)

# print(rev_cocat("red","green","blue"))

# def person(**kwargs):
#     return(kwargs)
# print(person(first="afreen",secound="mohamed",third="shaji"))

# def employ_detail(**kwargs):
    
#     for k,v in kwargs.items():
#         print(f"{kwargs['name']} has {kwargs['exp']} years of experience in {kwargs['dep']}")
#         break


# # o/p jhon has 2 yeras experiance in web development
# employ_detail(name="jhon",exp="2",dep="web development")

# def balance_enq(**kwargs):
#     name=kwargs.get("name")
#     acno=kwargs.get("acmo")
#     bal=kwargs.get("balance")
#     print(f"your {name} {acno} has balance of {bal}Rs")





# balance_enq(name="sbi",acmo="1223344",balance=22500)


def program(*args,**kwargs):
    num1,num2=args
    op=kwargs.get("operand")
    if op=="+":
        res=num1+num2
    elif op=="-":
        res=num1-num2
    elif op=="*":
        res=num1*num2
    else:
        return "invalid operend"
    return res


print(program(10,5,operand="*"))
