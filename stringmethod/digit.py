text="i have a care 2 "
words=text.split(" ")
for w in words:
    if w.isdigit():
        print(w)