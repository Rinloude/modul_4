from dataclasses import dataclass

@dataclass
class Book:
    author: str
    title: str
    rating: int
    read_date: str  # Формат: "YYYY-MM-DD"
    
    def to_dict(self):
        return {
            'author': self.author,
            'title': self.title,
            'rating': self.rating,
            'read_date': self.read_date
        }

    def from_dict(data):
        return Book(
            author=data['author'],
            title=data['title'],
            rating=data['rating'],
            read_date=data['read_date']
        )
