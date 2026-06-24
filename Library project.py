import json
class Library:
    def __init__(self,):

        self.books_list = []

    def add_book(self):
        
        self.books_dict = {}
        
        title = input("Enter book Title: =>> ")
        author = input("Enter book Author: =>> ")
        isbn = input("Enter book ISBN: =>> ")
        
        self.books_dict["Title"] = (title)
        self.books_dict["Author"] = (author)
        self.books_dict["ISBN"] = (isbn)
        self.books_list.append(self.books_dict)
        library.save_books()

    def save_books(self):
        
        with open("Books.json", "w") as file:
            json.dump(self.books_list, file,indent=4)
        
    def load_books(self):
        try:
            with open("Books.json", "r") as file:
                content = json.load(file)
            for i in content:
                self.books_list.append(i)
        except json.decoder.JSONDecodeError:
            pass
        except FileNotFoundError:
            pass

    def display_books(self):
        if not self.books_list:
            print("Library is empty")
        else:
            for each_book in self.books_list:
                for x,y in each_book.items():
                    print(f"{x}: {y}")
                print("----------------")

    def search_book(self):
            user_input = input("Enter book Title to search => ")
            for book in self.books_list:
                if book.get("Title") == user_input:
                    for x,y in book.items():
                        print(f"{x}: {y}")
                    print("----------------")
                    break
            else:
                print('Book is not in Library')

    def delete_book(self):
        user_input = input("Enter Book Title to delete => ")
        for book in self.books_list:
            if book.get("Title") == user_input:
                self.books_list.remove(book)
                print("Book has been removed")
                break
        else:
            print(f"No such Book with that name")
        library.save_books()

library = Library()
library.load_books()

def main():
    while True:
        choice = input("""Select option to perform
1 = Add a book
2 = Display all books
3 = Search for a book
4 = Delete a book
5 = exit
=>> """)
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.delete_book()
        elif choice == "5":
            break
        else:
            print("Invaild input")

if __name__ == "__main__":
    main()

library.save_books()
