lst=[1,2,5,8,10,11]

# cubes=[num**3   for num in lst]
# print(cubes)

# squares=[num**2 for num in lst]
# print(squares)

# add_two=[num+2 for num in lst]
# print(add_two)

# floor=[num//2 for num in lst]
# print(floor)

# odds=[num for num in lst if num%2!=0]
# print(odds)

# evens=[num for num in lst if num%2==0]
# print(evens)

# years=[y for y in range(1800,2025)]
# print(years)

# c_years=[c for c in range(1800,2025) if c%100==0]
# print(c_years)

leap_years=[l for l in range(1800,2025) if (l%100==0 and l%400==0)or(l%100!=0 and l%4==0)]
print(leap_years)