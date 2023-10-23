n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
lst=[10,20,40]
loc=int(input("enter the number:"))
try:
    print(lst[loc])
except Exception as e:
    print(e.args)

try:
    res=n1/n2
    print(f"result {res}")
except Exception as e:
    print(e.args)



print("hello, result have shown")