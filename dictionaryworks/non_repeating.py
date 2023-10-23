text="ABCABDCEFG"

rp={}

for r in text:
    if r not in rp:
        rp[r]=1
    else:
        rp[r]+=1

for k,v in  rp.items():
    if v==1:
        print(k)
    
    

  
