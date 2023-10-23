text="ABBACDD"

wc=dict()

for ch in text:
    if ch not in wc:
        wc[ch]=1
    else:
        print(ch,"first recursive")
        break
    



