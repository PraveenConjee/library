def start():  # Defines main function
    userInput()



allBooks = [  # This creates a list of all books in the library
                ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
                ['9780134494166',"The Human Body","Dave R",1,[]],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
           ]

borrowedBOOKs = []  # This creates a list of all borrowed books in the library

def printMenu(): #Menu
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')


def userInput():  # Asks for user input
    while True:  # Boolean to keep while loop going
        printMenu()
        select = input("Your selection> ")
        if select.isdigit():
            pass
        else:
            select = select.lower()
        # If user selects one of these options, execute the corresponding function
        if select == "1" or select == "a":
            addBook()

        elif select == "2" or select == "r":
            borrowBook()

        elif select == "3" or select == "t":
            returnBook()

        elif select == "4" or select == "l":
            listBook()

        elif select == "5" or select == "x":
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            listBook()
            break

        else:
            print("Wrong selection! Please selection a valid option.\n")
            # If user enters an invalid input, it prints this line and loops back


def addBook():  # adds a book to the library
    name = input("Book name> ")
    while "*" in name or "%" in name:  # Loops this till the user enters valid book name
        print("Invalid book name!")
        name = input("Book name> ")

    author = input("Author name> ")  # Author name has no restriction

    edition = input("Edition number> ")

    while edition.isdigit() == False:  # while loop till edition is only a number
        print("Invalid edition number!")
        edition = input("Edition number> ")

    sum = 0
    multiply = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    isbn = input("ISBN> ")
    while isbn.isdigit() == False  or len(isbn) != 13:  # loop till isbn is 13 digit number
        print("Invalid ISBN number!")
        isbn = input("ISBN> ")

    for i in range(13): # multiplies each index in the both lists in order and sums it
        sum += int(isbn[i]) * multiply[i]

    if sum % 10 == 0:  # if the sum is divisible by 10 the isbn is valid
        allBooks.append([isbn, name, author, edition, []])
        print("A new book is added successfully")

    else:
        print("Invalid ISBN number!\n")


def borrowBook():  # allows user to borrow a book
    borrower = input("Enter the borrower name> ")
    search = input("Search term> ")
    bookIsFound = False
    if search[-1] == "*":  # if the last index is *
        search = search[:-1]  # removes the last index
        for i in range(len(allBooks)):
            if search.lower() in allBooks[i][1].lower():
                allBooks[i][4].append(borrower)  # if the book is found, it adds the borrower
                                                 # in the list of borrowers
                borrowedBOOKs.append(allBooks[i])
                print("-\"{}\" is borrowed!".format(allBooks[i][1]))
                bookIsFound = True


    elif search[-1] == "%":  # if the last index is %
        search = search[:-1]  # removes the last index
        length = len(search)
        for i in range(len(allBooks)):
            if search.lower() == allBooks[i][1][0:length].lower():
                allBooks[i][4].append(borrower)
                borrowedBOOKs.append(allBooks[i])
                print("-\"{}\" is borrowed!".format(allBooks[i][1]))
                bookIsFound = True

    else:
        for i in range(len(allBooks)):
            if search.lower() == allBooks[i][1].lower():
                allBooks[i][4].append(borrower)
                borrowedBOOKs.append(allBooks[i])
                print("-\"{}\" is borrowed!".format(allBooks[i][1]))
                bookIsFound = True

    if bookIsFound != True:
        print("Book is not found!")


def returnBook():  # allows user to return book
    isbnReturn = input("ISBN> ")
    sum = 0
    multiply = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    if isbnReturn.isdigit() is False or len(isbnReturn) != 13:  # if conditions arent met, it prints code
        print("Invalid ISBN number!")

    else:
        for i in range(13):  # multiplies each index in the both lists in order and sums it
            sum += int(isbnReturn[i]) * multiply[i]

        if sum % 10 == 0:  # if the sum is divisible by 10 the isbn is valid
            for i in range(len(borrowedBOOKs)):
                if isbnReturn in borrowedBOOKs[i][0]:
                    borrowedBOOKs.pop(i)
                    for j in range(len(allBooks)):
                        if isbnReturn in allBooks[j][0]:
                            allBooks[j][4].pop()
                            print("Book has been returned successfully!")
                else:  # if the returning isbn is not in the borrowed books list, prints code
                    print("No book is found! ")

        else:
            pass



def listBook():  # creates a list of all books
    for book in allBooks:  # executes this loop for the number of books in list of all books
        borrowed = False
        for i in borrowedBOOKs:  # executes this loop for the number of books in list of borrowed books
            if book in borrowedBOOKs:  # if the book is in the borrowed books list, borrowed is set to true
                borrowed = True
                break  # breaks out of the borrowed books for loop to check the next book in all books list
        print("---------------")
        if not borrowed:
            print("[Available]")  # if book is not borrowed, then it is available
        else:
            print("[Unavailable]")

        print(book[1], "-", book[2])
        print("E: {} ISBN: {}".format(book[3], book[0]))
        print("borrowed by: {}".format(book[4]))


start()  # runs the main function