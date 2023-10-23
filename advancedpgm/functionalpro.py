min_two=lambda n1,n2:n1 if n1<n2 else n2

max_two=lambda n1,n2:n1 if n1>n2 else n2

add_two=lambda n1,n2:n1+n2

odd_even=lambda n:"even" if n%2==0 else "odd"

num_ck=lambda n:"+ve" if n>0 else "-ve"

print(min_two(20,10))
print(max_two(50,80))
print(add_two(34,40))
print(odd_even(8))
print(num_ck(-5))