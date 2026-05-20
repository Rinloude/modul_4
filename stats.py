from models import Book
from storage import load_books
from collections import defaultdict

def average_rating():
    books = load_books()
    if not books:
        return 0
    total = sum(book.rating for book in books)
    return total / len(books)

def stats_by_author():
    books = load_books()
    author_counts = defaultdict(list)
    for b in books:
        author_counts[b.author].append(b.rating)
    stats = {}
    for author, ratings in author_counts.items():
        stats[author] = {
            'count': len(ratings),
            'average_rating': sum(ratings) / len(ratings)
        }
    return stats
