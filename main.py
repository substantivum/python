#Open for reading three main text files with general information
logins = open('Login.txt','r', encoding='utf-8')
passwords = open('Passwords.txt', 'r', encoding='utf-8')
books = open('library.txt', 'r', encoding='utf-8')

#Create main lists and dictionaries that we will be appending in future
books_and_prices={}
main_dict = {}
l = []
p = []
books_l = books.readlines()
titles = []
prices=[]

#We split our lines (book) in library.txt and append our titles list and prices list
for book in books_l:
    list_of = book.split()
    list_of_titles = book.rsplit(' ', 0)[0]
    titles.append(list_of_titles)
    for x in list_of:
        if x.isdigit():
            prices.append(int(x))


for index in range(len(books_l)):
    books_and_prices[titles[index].lower().rstrip()] = prices[index]

#test
print(books_and_prices)

for i in logins:
    l.append(i.rstrip())
for n in passwords:
    p.append(n.rstrip())
for i in range(len(l)):
    main_dict[l[i]] = p[i]

#test
print(main_dict)

#Buy book
def buy_book(user_login=None):
    fullname = input('Input your name and surname: ')
    account = input('Input your wallet amount: ')
    with open(f'Readers budget-{red_login}.txt', 'w+', encoding='utf8')as file:
        file.write(account)
    lines = open('Borrowed books', 'r', encoding='utf8')
    trigger = False
    for line in lines.readlines():
        if user_login in line:
            trigger = True
    if trigger:
        print('1) Buy the book\n2) Borrow the book\n3) Return the book')
        type_of_celling = input('Input 1, 2 or 3: ')
        if type_of_celling == '1':
            title = input('Enter the name or the genre of the book you want to buy: ')
            book_num = 0
            choosed_books = []
            for i in titles:
                if title in i:
                    choosed_books.append(i)
            for z in choosed_books:
                book_num += 1
                print(str(book_num) + ')', z)
            choose = int(input('choose number of the book: '))
            print(choosed_books[choose - 1])
            total = 0
            with open(f'Readers budget-{red_login}.txt', 'r+')as file:
                bank = file.readlines()
                for money in bank:
                    if int(money) < books_and_prices[choosed_books[choose - 1].lower().rstrip()]:
                        total = money
                        print('You do not have enough budget')
                    else:
                        try:
                            total = int(money) - books_and_prices[choosed_books[choose - 1].lower().rstrip()]
                            file = open('Bought books', 'a', encoding='utf8')
                            file.write(f'Client {fullname} {user_login} bought book {choosed_books[choose - 1]} ')
                            file.close()
                        except KeyError:
                            print('Book is not found ')
            with open(f'Readers budget-{red_login}.txt', 'w')as file:
                file.write(str(total))
                file.close()
        elif type_of_celling == '2':
            title = input('Enter the name or the genre of the book you want to borrow: ')
            book_num = 0
            choosed_books = []
            for i in titles:
                if title in i:
                    choosed_books.append(i)
            for z in choosed_books:
                book_num += 1
                print(str(book_num) + ')', z)
            choose = int(input('choose number of the book: '))
            print(choosed_books[choose - 1])
            if choosed_books[choose - 1].lower().rstrip() in books_and_prices:
                date = input('Enter the deadline date yy.mm.dd : ')
                file = open('Borrowed books', 'a', encoding='utf8')
                file.write(f'Client {fullname} {user_login} borrowed book {choosed_books[choose - 1].lower().strip()} {date}\n')
                file.close()
            else:
                print('Book is not found')
        elif type_of_celling == '3':
            print('Enter the name of the book you want to return')
            title = input('Enter: ')
            rent_lines = open('Borrowed books', 'r', encoding='utf8')
            file_data = ''
            for rent_line in rent_lines:
                if title.lower() in rent_line and user_login in rent_line:
                    continue
                file_data += rent_line
            rec_file = open('Borrowed books', 'w', encoding='utf8')
            rec_file.write(file_data)
            rec_file.close()
        else:
            reader_menu()

    else:
        print('1)Buy the book\n2)Borrow the book')
        type_of_celling = input('Input 1 or 2: ')
        if type_of_celling == '1':
            title = input('Input the name or the genre of the book you want to buy: ')
            book_num = 0
            choosed_books = []
            for i in titles:
                if title in i:
                    choosed_books.append(i)
            for z in choosed_books:
                book_num += 1
                print(str(book_num) + ')', z)
            choose = int(input('choose number of the book: '))
            print(choosed_books[choose - 1])
            total = 0
            with open(f'Readers budget-{red_login}.txt', 'r+')as file:
                bank = file.readlines()
                for money in bank:
                    if int(money) < books_and_prices[choosed_books[choose - 1].lower().rstrip()]:
                        total = money
                        print('You do not have enough budget')
                    else:
                        try:
                            total = int(money) - books_and_prices[choosed_books[choose - 1].lower().rstrip()]
                            file = open('Bought books', 'a', encoding='utf8')
                            file.write(f'Client {fullname} {user_login} bought book {choosed_books[choose - 1]} ')
                            file.close()
                        except KeyError:
                            print('Book not found ')
            with open(f'Readers budget-{red_login}.txt', 'w')as file:
                file.write(str(total))
                file.close()
        elif type_of_celling == '2':
            title = input('Enter the name or the genre of the book you want to borrow: ')
            book_num = 0
            choosed_books = []
            for i in titles:
                if title in i:
                    choosed_books.append(i)
            for z in choosed_books:
                book_num += 1
                print(str(book_num) + ')', z)
            choose = int(input('choose number of the book: '))
            print(choosed_books[choose - 1])
            if choosed_books[choose - 1].lower().rstrip() in books_and_prices:
                date = input('Enter the deadline date yy.mm.dd  : ')
                file = open('Borrowed books', 'a', encoding='utf8')
                file.write(f'Client {fullname} {user_login} borrowed book {choosed_books[choose - 1].lower().strip()} {date}\n')

                file.close()
            else:
                print('Book not found')
        else:
            reader_menu()

#favorite book
def add_favorite(user_input):
    book_num = 0
    choosed_books = []
    for i in titles:
        if user_input in i:
            choosed_books.append(i)
    for z in choosed_books:
        book_num += 1
        print(str(book_num) + ')', z)
    choose = int(input('choose your favorite book: '))
    print(choosed_books[choose-1])
    file = open(f'Favorite {red_login}', 'a', encoding='utf8')
    file.write(choosed_books[choose-1])
    file.close()
    print('Book successfully has been added to favorite!')
    reader_menu()

def add_readed(user_input):
    book_num = 0
    choosed_books = []
    for i in titles:
        if user_input in i:
            choosed_books.append(i)
    for z in choosed_books:
        book_num += 1
        print(str(book_num) + ')', z)
    choose = int(input('choose the book you have already read: '))
    print(choosed_books[choose-1])
    file = open(f'Read {red_login}', 'a', encoding='utf8')
    file.write(choosed_books[choose-1])
    file.close()
    print('Book have successfully been added to read ones!')
    reader_menu()

#main meny of reader
def reader_menu():
    menu_num = int(input('input: '))
    if menu_num == 1:
        book_num = 0
        poisk = input('enter the name or the genre of the book: ')
        for i in books_l:
            book_num += 1
            if poisk in i:
                print(str(book_num) + ')',i)
        reader_menu()
    elif menu_num == 2:
        add_readed(input('enter the name or the genre of the book: '))
    elif menu_num == 3:
        add_favorite(input('enter the name or the genre of the book: '))
    elif menu_num == 4:
        try:
            file = open(f'Favorite {red_login}', 'r', encoding='utf8')
            print(file.read())
            reader_menu()
        except:
            print('You do not have favorite books')
    elif menu_num == 5:
        try:
            file = open(f'Readers budget-{red_login}.txt', 'r')
            print(file.read())
        except:
            print('You are poor')
        reader_menu()
    elif menu_num == 6:
        buy_book(red_login)
        reader_menu()
    elif menu_num == 7:
        print('See you soon')
        exit()
    else:
        print('invalid input, retry')
        reader_menu()

#main menu of librarian
def librarian_menu():
    menu_num = int(input('input: '))
    if menu_num == 1:
        print(main_dict)
        librarian_menu()
    elif menu_num == 2:
        file = open('Borrowed books', 'r', encoding='utf8')
        file2 = open('Bought books', 'r', encoding='utf8')
        login = input('name of reader: ')
        borrowed = []
        buyed = []
        for i in file.readlines():
            borrowed.append(i.rstrip())
        for i in borrowed:
            if login in i:
                print(i)
        for i in file2.readlines():
            buyed.append(i.rstrip())
        for i in buyed:
            if login in i:
                print(i)

        librarian_menu()
    elif menu_num == 3:
        poisk = input('book: ')
        book_num = 0

        for i in books_l:
            book_num += 1
            if poisk in i:
                print(str(book_num) + ')', i)
        librarian_menu()
    elif menu_num == 4:
        print('This subsection contains the requirements for the program and outlines the functionality of each step, when the user interacts with the system. All actions performed by the user and how it works are described sequentially.',
              '\n', '<Functional Requirement 1>: Login your account for Reader type and Librarian type', '\n',
              '- Enable user to run a code', '\n', '- Enable users to choose the type of account between librarian and reader', '\n', '- Authenticate and Login user to the program', '\n', '- Exit if Username or Password are incorrect',
              '\n', '<Functional Requirement 2>: Reader - search function',
              '\n', '- Enable user choose 1 (first)', '\n', '- Enable user input the name or genre of the book he needs',
              '\n', '<Functional Requirement 2>: Reader - List of the books user have already read',
              '\n', '- Enable user choose 2 (second)', '\n', '- Enable user input the name of the book or its genre', '\n', '- Choose the number of the book',
              '\n', '<Functional Requirement 2>: Reader - Adding to the list of favorite books',
              '\n', '- Enable user choose 3 (three)', '\n', '- Enable user input the name or the genre of the book', '\n', '- Choose the number of matching books to make a decision',
              '\n', '<Functional Requirement 2>: Reader - Reading the list of favorite books',
              '\n', '- Enable user choose 4 (fourth)',
              '\n', '<Functional Requirement 2>: Reader -  Show the user’s budget',
              '\n', '- Enable user choose 5 (fifth)',
              '\n', '<Functional Requirement 2>: Reader - Menu of choice',
              '\n', '- Enable user choose 6 (sixth)', '\n', '- Input the name of the user', '\n', '- Input the budget of the user',
              '\n', '<Functional Requirement 3>: Reader - Buying the book',
              '\n', '- Enable user choose the first option', '\n', '- Enable user input the name or the genre of the book', '\n', '- Choose the number of the book the user needs',
              '\n', '<Functional Requirement 3>: Reader - Borrowing the book',
              '\n', '- Enable user choose the second option (2)', '\n', '- Enable user input the name or the genre of the book', '\n', '- Choose the number of the book the user needs', '\n', '- Input the deadline date',
              '\n', '<Functional Requirement 4>: Librarian - list of readers',
              '\n', '- Enable user choose 1 and put it in input', '\n', '- Exit if input is incorrect',
              '\n', '<Functional Requirement 4>: Librarian - last user’s actions',
              '\n', '- Enable user choose 2 (second)', '\n', '- User should input the reader’s name', '\n', '- Exit if the reader is not found',
              '\n', '<Functional Requirement 4>: Librarian - Reserve a book for a reader',
              '\n', '- Enable a user to choose 3 (third)', '\n', '- Enable user to search a book by its name or genre', '\n', '- Input the reader’s name and surname',
              '\n', '<Functional Requirement 4>: Librarian - Exit the program',
              '\n', '- Enable user input 5', '\n', '- Program will end')
        librarian_menu()

    elif menu_num == 5:
        print("See you soon")
        exit()
    else:
        print('invalid input, retry')
        librarian_menu()

#start menu
login = input("Enter the type of your account: ")

#reader login
if login == 'reader' or login == 'Reader':
    red_login = input("Login of reader: ")
    red_pass = input("Password of reader: ")
    for i in main_dict:
        if red_login == i:
            if red_pass == main_dict[i]:
                print('Greetings dear Reader, please dial the menu number to work with the program, if finished, dial 7:')
                print('Choose the action:',
                      '\n', '1. Search the book you need',
                      '\n', '2. Add the book you have already read',
                      '\n', '3. Add the book to the list <My favorite books>',
                      '\n', '4. Show <My favorite books>',
                      '\n', '5. Show my budget balance',
                      '\n', '6. Open options for buying or borrowing',
                      '\n', '7. Exit the program',)
                reader_menu()
            else:
                print('Sorry, your password is wrong')
#librarian login
elif login == "librarian" or login == 'Librarian':
    lib_login = input("Login of librarian: ")
    lib_pass = input("Password of librarian: ")
    if lib_login == 'cookie' and lib_pass == 'admin':
        print("Greetings dear Librarian! Please dial the menu number to work with the program, if finished, dial 5:")
        print('Choose the action:',
              '\n', '1. Show list of readers',
              '\n', '2. Show last users actions by the name',
              '\n', '3. Search the book by its name or genre',
              '\n', '4. Get the instructions of the program',
              '\n', '5. Exit the program')
        librarian_menu()
    else:
        print("Sorry, but we did not find this type of account or your username and / or password is incorrectly entered, please repeat")


else:
    print("Sorry, but we did not find this type of account or your username and / or password are incorrectly entered, please repeat.")