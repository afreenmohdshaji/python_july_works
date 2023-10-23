word="a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses"

words=word.replace(",","").split(" ")

wc={}

for w in words:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)