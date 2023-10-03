import sys
from datetime import datetime
from os import remove

print("\t\t\t\t\t\tWelcome to Mukenya car app!🚦")
print("\t\tChoose your choice: ")
print(f"1. Vehicle entry\n"
      f"2. Close program\n")

selection = int(input("Hi, kindly enter your choice: "))

if selection == 1:
    carName = input("Your car name: ")
    carModel = input("Car model: ")
    carPlate = input("Car number plate: ")
    today = datetime.today()
    print(f"{carName},{carModel},{carPlate} has Entered {today}")

    parkIt1 = ['🫣','🫣','🫣','🫣','🫣']
    parkIt2 = ['🫣','🫣','🫣','🫣','🫣']
    parkIt3 = ['🫣','🫣','🫣','🫣','🫣']
    parkIt4 = ['🫣','🫣','🫣','🫣','🫣']
    parkIt5 = ['🫣','🫣','🫣','🫣','🫣']

    zote = [parkIt1,parkIt2,parkIt3,parkIt4,parkIt5]
    print(f"{parkIt1}\n{parkIt2}\n{parkIt3}\n{parkIt4}\n{parkIt5}")

    car = input("Park your vehicle🅿️(2 digits to rep the row and column): \n")

    row = int(car[0])
    col = int(car[1])
    select_row = zote[row-1]
    select_row[col-1] = '🚘'
    print("Car parked successfully!!!!✅✅✅✅\n")
    print(f"Want to see where you have parked?⁉️ \n"
          f"1. Yes✔️\n"
          f"2. No❌")

    parked = int(input("Choice?:  "))
    if parked == 1:
        print(f"{parkIt1}\n{parkIt2}\n{parkIt3}\n{parkIt4}\n{parkIt5}")
        print("🤝🤝🤝🤝🤝🤝🤝")
        print("Screenshot to validate the date you have given us for reference\n Thank you.")
    else:
       sys.exit()

else:
    print("Shutting down the program...Bye!")
    sys.exit()










