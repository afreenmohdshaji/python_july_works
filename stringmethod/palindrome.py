word="abba"
count=len(word)
p_str=""

for i in range(count-1,-1,-1):
    p_str+=word[i]

print("palindrom" if p_str==word else "not palindrome")