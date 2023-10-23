color=["red","blue","green","red","blue","yellow"]
# color.append("yellow")  #append
# for i in range(0,len(color)):
# print(color.count("yellow"))
# print(color.index("green"))
# color.insert(3,"black")
# color.sort()
# color.remove("red")
# color.pop(2)
# print(color)
cpy_colors=color.copy()
print(cpy_colors==color)
print(id(color))
print(id(cpy_colors))
