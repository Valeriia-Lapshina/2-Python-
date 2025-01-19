class Book:
    """ Базовый класс - Книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        return f"книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс - Бумажные книги."""
    def __init__(self, name: str, author: str, pages: int = 0):  # По умолчанию количество страниц = 0
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        """Устанавливаем количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная {super().__str__()}. Количество страниц: {self.pages}"


class AudioBook(Book):
    """ Дочерний класс - Аудио-книги. """
    def __init__(self, name: str, author: str, duration: float = 0):  # По умолчанию продолжительность = 0
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Возвращает значение продолжительности книги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        """Устанавливаем значение продлжительности книги."""
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Аудио-{super().__str__()}. Продолжительность: {self.duration} минут"


# Проверка бумажной книги:
PaperBook = PaperBook("Источник", "Айн Рэнд")  # Инициализируем бумажную книгу
print(PaperBook.pages)  # Проверяем, сколько страниц в книге (по умолчанию = 0)
PaperBook.pages = 550  # Устанавливаем количество страниц в книге 550
print(PaperBook.pages)  # Получаем: 550
print(PaperBook)  # Бумажная книга 'Источник'. Автор Айн Рэнд. Количество страниц: 550
print(PaperBook.__repr__())  # PaperBook(name='Источник', author='Айн Рэнд')

# Проверка аудио-книги:
AudioBook = AudioBook("Источник", "Айн Рэнд")  # Инициализируем аудио-книгу
print(AudioBook.duration)  # Проверяем продолжительность аудио-книги (по умолчанию = 0)
AudioBook.duration = 1012.5  # Устанавливаем значение продолжительности книги
print(AudioBook.duration)  # Получаем: 1012.5
print(AudioBook)  # Аудио-книга 'Источник'. Автор Айн Рэнд. Продолжительность: 1012.5 минут
print(AudioBook.__repr__())  # AudioBook(name='Источник', author='Айн Рэнд')
