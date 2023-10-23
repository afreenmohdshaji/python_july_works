n1=int(input("enter a number:"))
n2=int(input("enter a number:"))

try:
    res=n1/n2
    print(f"result {res}")
except Exception as e:
    n2=int(input("enter another number:"))
    res=n1/n2
    print(f"result {res}")
finally:
    print("all the reslut havee shown")


expression="10-22*3"
print(eval(expression))