val=input("enter your no:")

# if val.isdigit()==False:
#     raise Exception("only int allowed")
# else:
#     print("allowed")

if val.isalnum()==False:
    raise Exception("not allowed")
else:
    print("allowed")