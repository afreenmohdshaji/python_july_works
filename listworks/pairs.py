sum=int(input("enter a number"))
arr=[2,3,1,5,6,9,7,8]

arr.sort()

low=0
upp=len(arr)-1

while(low<upp):
    cur_sum=arr[low]+arr[upp]

    if(cur_sum==sum):
        print("pairs",arr[low],arr[upp])
        low+=1
        upp-=1
    elif(cur_sum<sum):
        low+=1
    elif(cur_sum>sum):
        upp-=1
