frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

# for fw in frameworks:
#     print(fw.get("name"))

# fw_works=[fw.get("name") for fw in frameworks]
# print(fw_works)

# all_rating=[fw.get("rating") for fw in frameworks]
# print(all_rating)

# all_dict=[fw for fw in frameworks]
# print(all_dict)

# fw_python=[fw.get("name") for fw in frameworks if fw.get("language")=="python"]
# print(fw_python)

# for fw in frameworks:
#     if fw.get("language")=="python":
#         print(fw)

# fw_rating=[fw.get("name") for fw in frameworks if fw.get("rating")==5]
# print(fw_rating)

# id_filter=[fw.get("name") for fw in frameworks if fw.get("id") in range(1,4)]
# print(id_filter)

# lowest_fw=min(frameworks,key=lambda fw:fw.get("rating"))
# print(lowest_fw)

# gretest_fw=max(frameworks,key=lambda fw:fw.get("rating"))
# print(gretest_fw)

srt=sorted(frameworks,reverse=True,key=lambda fw:fw.get("rating"))
print(srt)