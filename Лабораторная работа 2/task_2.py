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
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('Значение id_ должно быть типа int')
        if id_ < 1:
            raise ValueError('Значение id_ должно быть положительным числом')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError('Значение name должно быть строковым типом')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Значение pages должно быть типа int')
        if pages < 1:
            raise ValueError('Значение pages должно быть положительным числом')
        self.pages = pages


# TODO написать класс Library
class Library:
    def __init__(self, books: list = None):
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return max(self.books, key=lambda book: book.id_).id_ + 1


    def get_index_by_book_id(self, id_: int):
        if not isinstance(id_, int):
            raise TypeError('Значение id_ должно быть типа int')
        if id_ <= 0:
            raise ValueError('Значение id_ должно быть больше 1')

        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i

        raise ValueError('Книги с запрашиваемым id не существует')



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
