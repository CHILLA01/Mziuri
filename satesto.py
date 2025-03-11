class Book(LibraryItem):
    def __init__(self, title, subject, ISBN, authors, status="available"):
        super().__init__(title, status)
        self.subject = subject
        self.ISBN = ISBN
        self.authors = authors

    def __str__(self):
        return f"წიგნი: {self.title}, თემატიკა: {self.subject}, ავტორი: {(self.authors)}, სტატუსი: {self.status}"


