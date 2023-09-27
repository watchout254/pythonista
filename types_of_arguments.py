#default, positional, keyword, arbitrory
#Positional argument
def greet(name,subject, dept = "IT"):
    print(f"Hi {name}")
    print(f"From Department {dept}")
    print(f"fDo you teach {subject}?")

greet("Daniel", "Python")


