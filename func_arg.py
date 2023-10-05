#Types of arguments
#default, positional, keyword, arbitrory


def greet(name):
    print(f"Hi {name}")
    print(f"Are you from Information Technology Department")

greet("Daniel")
greet("mukenya")

def add(a,b,d):
    c = a+b+d
    print(f"Sum is {c}")
add(5,7,8)
add(8,9,3)


def add(a,b):
    c = a+b
    #print(c)
    return c
result = (add(5,4))
print(result)


def format_name(first,last):
    fmat = first.title()
    fnat = last.title()
    return f"{fmat} {fnat}"
      
print(format_name("daniel","MUKENYA"))
