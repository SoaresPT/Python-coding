# 11.1
class Book:
    def __init__(self, name, author, page_count) -> None:
        self.name = name
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"{self.name} (author {self.author}, {self.page_count} pages)")

class Magazine:
    def __init__(self, name, chief_editor) -> None:
        self.name = name
        self.chief_editor = chief_editor
    
    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor})")

class Publication(Book, Magazine):
    def __init__(self, name, author, page_count) -> None:
        super().__init__(name, author, page_count)

if __name__ == "__main__":
    book = Book("Compartment No. 6", "Rosa Liksom", 192)
    book.print_information()
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    magazine.print_information()
    pub = Publication("WTF", "MAS?", 1)
    print(type(pub))