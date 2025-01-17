BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):  # метод, возвращающий идентификатор для добавления новой книги в библиотеку
        if not self.books:  # если книг в библиотеке нет
            return 1  # возвращается 1
        else:
            return self.books[-1].id + 1  # если книги есть, то возвращается идентификатор последней книги, увеличенной на 1

    def get_index_by_book_id(self, book_id):  # метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса
        for index, book in enumerate(self.books):
            if book_id == book.id:  # если книга найдена
                return index  # возвращается ее индекс
            raise ValueError(f'Книги с запрашиваемым id={book_id} не существует')  # вызов ошибки


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
