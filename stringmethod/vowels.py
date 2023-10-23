words="jjhgierikhbjhbafhbhibalhidbyfi1bhghbshjbghjbgbysdbfyhytidbhsljoabhibhbvlkhbkbfiba"
vowels="a","e","i","o","u"
v_count=0
c_count=0

for ch in words:
    if ch in vowels:
        v_count +=1
    elif ch.isalpha():
        c_count+=1

print(f"total numbers={len(words)}")
print(f"vowels={v_count}")
print(f"consonents={c_count}")
    