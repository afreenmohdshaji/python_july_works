for row in range(1,7):
    for sp in range(5,row-1,-1):
        print(end=" ")
    for col in range(1,row+1):
        print("* ",end="")
    print()    

