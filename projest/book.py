import uuid

class Book:
    def __init__(self, author_name: str, title: str):
        self.author_name = author_name
        self.title = title
        self.id = str(uuid.uuid4()) 

    def __str__(self):
        return f"{self.title} — {self.author_name} (ID: {self.id})"
