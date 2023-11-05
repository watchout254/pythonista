import sys

print("\t\t\t\t\t\t\tWelcome to check if it is an even or odd number")

biggie = 100


chukua = int(input("Enter any number(1-100): "))

while chukua < biggie:
    if chukua %2 == 0:
        print(f"{chukua} is an even number")
        chukua+=1
    elif chukua %2:
        print(f"{chukua} is an odd number")
        chukua+=1
    else:
        sys.exit()

