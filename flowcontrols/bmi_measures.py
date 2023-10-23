weightin_kg=75
heightin_cm=180
heightin_m=heightin_cm/100
#eq=w_kg/h in m **2
bmi=weightin_kg/heightin_m**2
print(f"{bmi} is your body mass")
if(bmi<20):
    print("underweight")
elif(bmi>=20 and bmi<=25):
    print("normal")
elif(bmi>=25 and bmi<=30):
    print("over weight")
else:
    print("obseity")
