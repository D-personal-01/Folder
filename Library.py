class Library:
    library_books = []
    number_of_books = 0
    def add(self,book):
        self.library_books.append(book)
        self.number_of_books+=1
    def show(self):
        for book in self.library_books:
            print(book,end="\n")
lib1=Library()
lib1.add("Herry Potter, J.K. Rowling, 1997")
lib1.add("The name of the Rose, Umberto Eco, 1980")
lib1.show()
print(lib1.number_of_books)
open("Library.txt","w").write("\n".join(lib1.library_books))