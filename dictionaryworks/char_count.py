text="ABAACCD"
# text_set=set(text)
# dictionary=dict()

# for i in text:
#     if i in dictionary:
#         continue
#     elif i==" ":
#         continue
#     else:
#         dictionary[i]=text.count(i)

# print(dictionary)
tc={}

for t in text:
    if t not in tc:
        tc[t]=1
    else:
        tc[t]+=1

print(tc)