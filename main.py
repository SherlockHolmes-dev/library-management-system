import os.path
import uuid
from os.path import exists
class Book:
    def __init__(self):
        self.id=uuid.uuid1()
    def addBook(self):
        self.title = input("Enter Book title here: ")
        self.publisher = input("Enter publisher name here: ")
        self.authorname=input('Enter Author name here: ')
        self.copies=input('Enter number of copies here: ')
        if (os.paxth.exists('temp.txt')):
            if(self.searchByTitle(self.title)==1 and self.searchByAuthor(self.authorname)==1 and self.searchByPublisher(self.publisher)==1):
                reading_file = open("temp.txt", "r")
                chek=0
                new_file_content = ""
                for line in reading_file:
                    stripped_line = line.strip()
                    toSearch = f'title:{self.title}'.lower()
                    if chek != 0:
                        chek+=1
                    if toSearch in stripped_line:
                        chek=1
                    if chek == 4:
                        old_copies=int((line.split(":")[1].strip()))
                        new_file_content +=f'copies:{old_copies+int(self.copies)}' + '\n'
                        chek=0
                    else:
                        new_file_content += stripped_line + "\n"
                reading_file.close()

                writing_file = open("temp.txt", "w")
                writing_file.write(new_file_content)
                writing_file.close()
            else:
                file = open('temp.txt','a')
                str=f'\n\nid:{self.id}\ntitle:{self.title}\npublisher:{self.publisher}\nauthorname:{self.authorname}\ncopies:{self.copies}'
                file.write(str)
                file.close()
        else:
            file = open('temp.txt', 'w')
            str = f'\n\nid:{self.id}\ntitle:{self.title}\npublisher:{self.publisher}\nauthorname:{self.authorname}\ncopies:{self.copies}'
            file.write(str)
            file.close()
        print('Book added successfully')
    def searchByTitle(self,title):
        line_no=0
        flag=0
        file = open('temp.txt','r')
        for line in file:
            line_no=line_no+1
            toSearch=f'title:{title}'.lower()
            if toSearch in line.lower():
                flag=1
        file.close()
        return flag
    def searchByAuthor(self,authorname):
        line_no=0
        flag=0
        file = open('temp.txt','r')
        for line in file:
            line_no=line_no+1
            toSearch=f'authorname:{authorname}'.lower()
            if toSearch in line.lower():
                flag=1
        file.close()
        return flag

    def searchByPublisher(self, publisher):
        line_no = 0
        flag = 0
        file = open('temp.txt', 'r')
        for line in file:
            line_no = line_no + 1
            toSearch = f'publisher:{publisher}'.lower()
            if toSearch in line.lower():
                flag = 1
        file.close()
        return flag

    def printBook(self,line_number):
        file=open('temp.txt','r')
        temp_line_number=0
        for line in file:
            temp_line_number = temp_line_number+1
            if(temp_line_number<line_number-1):
                continue
            else:
                print(file.readline(),end='')
                print(file.readline(),end='')
                print(file.readline(),end='')
                print(file.readline(),end='')
                print(file.readline(),end='')
                file.close()
                break
    def searchBook(self,book_title):
        line_no = 0
        flag=0
        if(os.path.exists('temp.txt')):
            file = open('temp.txt', 'r')
        else:
            print('Library do not exist!')
            print('try adding new books first..')
            return flag

        for line in file:
            line_no = line_no + 1
            toSearch = f'title:{book_title.strip().lower()}'
            if toSearch in line.lower():
                flag=1
                print()
                self.printBook(line_no-1)
        if(flag==0):
            print('Not found!')
            return flag
        file.close()
    def issueBook(self):
        book_title = input("Enter the title of the book to be issued: ")
        flag=self.searchBook(book_title)
        if(flag==0):
            return ''
        print()
        book_id = input("Copy and Paste the id of the book here: ")


        reading_file = open("temp.txt", "r")
        chek = 0
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            toSearch = f'id:{book_id}'.lower()
            if chek != 0:
                chek += 1
            if toSearch in stripped_line:
                chek = 1
            if chek == 5:
                existing_copies = int((line.split(":")[1].strip()))
                if(existing_copies<1):
                    return "Book is unavailable"
                new_file_content += f'copies:{existing_copies-1}' + '\n'
                chek = 0
            else:
                new_file_content += stripped_line + "\n"
        reading_file.close()

        writing_file = open("temp.txt", "w")
        writing_file.write(new_file_content)
        writing_file.close()
        return f'{book_title} has been issued, Thanks for your time'

    def returnBook(self):
        book_title = input("Enter the title of the book you want to return: ")
        flag = self.searchBook(book_title)
        if (flag == 0):
            return ''
        book_id = input("Copy and Paste the id of the book here: ")
        reading_file = open("temp.txt", "r")
        chek = 0
        new_file_content = ""
        mybook=''
        for line in reading_file:
            stripped_line = line.strip()
            toSearch = f'id:{book_id}'.lower()
            if chek != 0:
                chek += 1
                if(chek!=5):
                    mybook+=stripped_line+'\n'
            if toSearch in stripped_line:
                mybook+=stripped_line+'\n'
                chek = 1
            if chek == 5:
                existing_copies = int((line.split(":")[1].strip()))
                new_file_content += f'copies:{existing_copies + 1}' + '\n'
                mybook+=f'copies:{existing_copies + 1}' + '\n'
                chek = 0
            else:
                new_file_content += stripped_line + "\n"
        reading_file.close()

        writing_file = open("temp.txt", "w")
        writing_file.write(new_file_content)
        writing_file.close()
        print('\nUpdated information of the book you have returned is: ')
        print(mybook)







obj = Book()
print("...........Welcome to our Library..........")
print('\nChose the following options: ')
print("Press 1 to add Books in the library"),
print("Press 2 to search Books in the library"),
print("Press 3 to issue a Book from the library"),
print("Press 4 to return a Book to the library"),

option = input('Your Response here: ')
book_title=''

if(int(option)==1):
    obj.addBook()
elif (int(option)==2):
    book_title=input('Enter the title of the book to be searched: ')
    obj.searchBook(book_title)
elif (int(option)==3):
    print(obj.issueBook())
elif (int(option)==4):
    obj.returnBook()

# print(obj.id)
# obj.addBook()
# book_title = input('Enter the title of the book to be searched: ')
# obj.searchBook(book_title)
# print(obj.issueBook())
# obj.returnBook()