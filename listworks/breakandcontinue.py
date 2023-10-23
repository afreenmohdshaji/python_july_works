# for i in range(0,26):
#     if i==10:
#         # continue
#         break
#     print(i)

# print("program executed completed")

lst=[10,20,22,1,34,5]

num=int(input("enter a element"))

for i in range(0,len(lst)):
    if num==lst[i]:
        print("element is found")
        break
else:
    print("element not found")