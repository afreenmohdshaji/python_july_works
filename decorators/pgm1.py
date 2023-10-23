def swaf_num(fn):
    def inner(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner

@swaf_num
def sub(n1,n2):
    return n1-n2

@swaf_num
def div(n1,n2):
    return n1/n2

# print(sub(2,10))

# print(div(4,8))

def capitalize(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper

@capitalize
def gd_greetngs():
    return "good morning"

@capitalize
def evng_greetings():
    return "good evening"

# print(gd_greetngs())

# print(evng_greetings())



import datetime
@capitalize
def greeting():
    current_time=datetime.datetime.now()
    current_hour=current_time.hour
    if(5>current_hour<12):
        return "good motning"
    elif(12>=current_hour<=18):
       return "good afternoon"
    else:
        return "good night"

print(greeting())