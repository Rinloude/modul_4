import sys
from storage import add_book, list_books, delete_book
from models import Book
from stats import average_rating, stats_by_author

def main_menu():
    while True:
        print("\nТрекер прочитанных книг")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            add_book_ui()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_stats_by_author()
        elif choice == '5':
            delete_book_ui()
        elif choice == '6':
            print("До свидания!")
            sys.exit()
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

def add_book_ui():
    author = input("Автор: ")
    title = input("Название: ")
    try:
        rating = int(input("Оценка (1-5): "))
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        print("Некорректная оценка.")
        return
    read_date = input("Дата прочтения (ГГГГ-MM-ДД): ")
    new_book = Book(author, title, rating, read_date)
    if add_book(new_book):
        print("Книга добавлена.")
    else:
        print("Добавление книги не удалось.")

def show_all_books():
    books = list_books()
    if not books:
        print("Нет книг.")
        return
    for b in books:
        print(f"{b.author} - {b.title} | Оценка: {b.rating} | Дата: {b.read_date}")

def show_average_rating():
    avg = average_rating()
    print(f"Средняя оценка: {avg:.2f}")

def show_stats_by_author():
    stats = stats_by_author()
    for author, data in stats.items():
        print(f"{author}: {data['count']} книг, средняя оценка: {data['average_rating']:.2f}")

def delete_book_ui():
    author = input("Автор книги для удаления: ")
    title = input("Название книги для удаления: ")
    if delete_book(author, title):
        print("Книга удалена.")
    else:
        print("Не удалось удалить книгу.")

if __name__ == "__main__":
    main_menu()
