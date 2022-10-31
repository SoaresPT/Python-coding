# 11.1

class Publication():
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"{self.name} (author {self.author}, {self.page_count} pages)")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    
    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor})")

if __name__ == "__main__":
    book = Book("Compartment No. 6", "Rosa Liksom", 192)
    book.print_information()
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    magazine.print_information()