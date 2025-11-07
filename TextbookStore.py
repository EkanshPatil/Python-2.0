books = {
    "physics":"300"
}

#A
books["physics"] = "200"

#B
books["english"] = "300"
books["maths"] = "350"

while True:
    print("Welcome to the textbook shop!, enter one of the following ")
    print("1 - view a price of a book")
    print("2 - view all books")
    print("3 - exit shop")
    choice = int(input("Pick one of the above "))

    if choice ==1:
        view = input("Enter the book that you want to see the price of: ")
        if view in books:
            print("Book '{}' :  '{}'".format(view,books[view]))
        else:
            print("Book not found, please check for spelling and re-enter")
    
    elif choice ==2:
        for key,value in books.items():
             print(f"{key}:{value}")
    
    elif choice ==3:
        print("Exiting bookstore....")
        break

    else:
        print("Invalid number entered please enter the number 1,2 or 3")