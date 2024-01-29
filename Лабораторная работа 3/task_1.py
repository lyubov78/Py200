from typing import Union


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: '{self.name}'. Автор: '{self.author}'."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError('Значение должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц должно быть положительным числом!')
        self._pages = pages

    # Методы __str__ и __repr__ перегружены, потому что у дочернего класса PaperBook появился аргумент pages
    def __str__(self):
        return f"Книга: '{self.name}'. Автор: '{self.author}'. Кол-во страниц: {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: Union[int, float]):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: Union[int, float]):
        if not isinstance(duration, (int, float)):
            raise TypeError('Значение должно быть типа int или float')
        if duration <= 0:
            raise ValueError('Длительность должна быть больше нуля!')
        self._duration = duration

    # Методы __str__ и __repr__ перегружены, потому что у дочернего класса AudioBook появился аргумент duration
    def __str__(self):
        return f"Книга: '{self.name}'. Автор: '{self.author}', Длительность: {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    a = Book('Азбука', 'Иванов И.И.')
    print(a.__str__())
    print(a.__repr__())
    print('-' * 60)
    b = PaperBook('Азбука', 'Иванов И.И.', 50)
    print(b.__str__())
    print(b.__repr__())
    print('-' * 60)
    c = AudioBook('Азбука', 'Иванов И.И.', 100)
    print(c.__str__())
    print(c.__repr__())
