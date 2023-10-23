expenses=[12000,14000,25000,11000,10000,45000,100000]

count=len(expenses)

total=0

for i in range(0,count):
    print(expenses[i])

for i in range(0,count):
    total=total+expenses[i]

print(f"total is {total}")
sm_number=min(expenses)
print(f"smallest number is {sm_number}")

lg_number=max(expenses)
print(f"larg number is {lg_number}")

srt_exp=sorted(expenses,reverse=True)
print(srt_exp)


expenses[1]=15000
print(expenses)