from json import load

f="C:\\Users\\afisr\\Desktop\\july_pythonworks\\process_json\\student.json"


with open(f) as st:
    data=load(st)

rol=[sd.get("rol") for sd in data ]
print(rol)