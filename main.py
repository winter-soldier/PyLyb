class Librarian:

    def __init__(self, booklist):
        self.availableBooks = booklist

    def displayAvailablebooks(self):
        print('''
     ---------------PyLyb---------------
    |                                   |
      Books in shelf:
        ''')
        for book in self.availableBooks:
            print('    ', book)
        print('''    |                                   |
     ----------------------------------''')

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print('Borrowing successful!')
        else:
            print('Sorry, The book is not in the library at the moment')

    def addBook(self,  book):
        pass


class User:

    def requestBook(self):
        print('Enter the name of a book you want to borrow (Capitalized): ')
        self.book = input()
        return self.book

    def returnBook(self):
        print('Enter the name of the book you want to return (Capitalized): ')
        self.book = input()
        return self.book


def main():
    library = Librarian(['Ulysses', 'Lord of The Rings',
                         'War and Peace', 'Wings of Fire'])
    user = User()

    print('''
     ------------PyLyb------------
    |                             |
    | 1. Librarian                |
    | 2. User                     |
     -----------------------------
     ''')

    choice = int(input('Enter choice: '))
    if choice == 1:  # Librarian interface
        print('''
     ---------------PyLyb---------------
    |                                   |
    | 1. View Book Catalogue            |
    | 2. Add a new book                 |
    | 3. Update Availability            |
    | 4. Transactions                   |
    | 5. Renewals                       |
    | 6. New Members                    |
    | 7. Existing Members               |
    | 8. Book Details                   |
    | 9. Exit                           |
     -----------------------------------
     ''')

        choice = int(input('Enter choice: '))
        if choice == 1:
            library.displayAvailablebooks()

        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            pass

        elif choice == 8:
            pass

        elif choice == 9:
            pass

        else:  # error
            print('''
         ------------PyLyb------------- 
        |                              |
        | Please choose a valid option |
         ------------------------------ 
         ''')

    elif choice == 2:  # User interface
        print('''
     ---------------PyLyb--------------- 
    |                                   |
    | 1. New Membership                 |
    | 2. View Book Catalogue            |
    | 3. Lend Book                      |
    | 4. Return Book                    |
    | 5. Renew Book                     |
    | 6. Manage Dates                   |
    | 7. Delete Membership              |
    | 8. Exit                           |
     ----------------------------------- 
     ''')

        choice = int(input('Enter choice: '))
        if choice == 1:
            pass

        elif choice == 2:
            library.displayAvailablebooks()

        elif choice == 3:
            library.lendBook(user.requestBook())

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            pass

        elif choice == 8:
            pass

        elif choice == 9:
            pass

        else:  # error
            print('''
         ------------PyLyb------------- 
        |                              |
        | Please choose a valid option |
         ------------------------------ 
         ''')

    else:  # error
        print('''
     ------------PyLyb------------- 
    |                              |
    | Please choose a valid option |
     ------------------------------ 
     ''')


main()
