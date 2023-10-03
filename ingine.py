import datetime
import sys

print("\t\t\t\t\tWelcome to Jawabu Schools\n")
print("Pick your choice\n")
print(f"1.Login(Student)\n"
      f"2.Login(Staff)\n"
      f"3.Borrow Book\n"
      f"4.Return Book\n"
      f"5. Exit\n")

ans = int(input("You have picked: "))

match ans:
    case 1:
        username = input("Your name: ")
        password = input("Password: ")


    case 2:
        staffUser = input("Username: ")
        staffPass = input("Password: ")

    case 3:
        bookTitle = input("Title of the book: ")
        bookAuthor = input("Book Author: ")
        bookISBN = input("Book ISBN: ")
        bookPublication = input("Book Publication year: ")
        print("Successfully borrowed!!!")

    case 4:
        date = datetime.datetime
        copies = input("How many copy/ies: ")

    case 5:
        sys.exit()




