f1=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\allstudents.txt")

f2=open("C:\\Users\\afisr\\Desktop\\july_pythonworks\\fileoperation\\failed.txt")

all_syudents={l.rstrip("\n")  for l in f1}

failed_students={l.rstrip("\n")  for l in f2}

passed_students=all_syudents.difference(failed_students)
print(passed_students)
f1.close()
f2.close()