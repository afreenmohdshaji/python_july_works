# lst=[i for i in range(1,8)]
# print(lst)
# day=["holiday" if d in(1,7) else "weekday" for d in lst]
# print(day)

lst=[-3,2,6,5,3,9,10,12]

numbers=[num for num in lst if (num>0 and num%3==0)]
print(numbers)