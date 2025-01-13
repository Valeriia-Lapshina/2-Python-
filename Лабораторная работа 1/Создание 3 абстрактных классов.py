import doctest


class Tree:
    def __init__(self, type_of_wood: str, tree_count: int, height: float, trunk_diameter: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param type_of_wood: Порода древесины
        :param tree_count: Количество деревьев данной породы
        :param height: Высота дерева (в метрах)
        :param trunk_diameter: Диаметр ствола (в метрах)

        Примеры:
        >>> tree = Tree("Вяз", 10, 6.4, 0.55)  # инициализация экземпляра класса
        """

        self.type_of_wood = type_of_wood

        if not isinstance(tree_count, int):
            raise TypeError("Количество деревьев данной породы должно быть типа int")
        self.tree_count = tree_count

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(trunk_diameter, (int, float)):
            raise TypeError("Диаметр ствола должен быть типа int или float")
        if trunk_diameter <= 0:
            raise ValueError("Диаметр ствола должен быть положительным числом")
        self.trunk_diameter = trunk_diameter

    def availability_of_wood(self) -> bool:
        """
        Функция, которая проверяет наличие данной породы древесины на участке

        :return: Есть ли данная порода древесины на участке

        Примеры:
        >>> tree = Tree("Вяз", 10, 6.4, 0.55)
        >>> tree.availability_of_wood()
        """
        ...

    def tree_age(self, thickness_of_the_annual_ring: float):
        """
        Расчет возраста дерева

        :param thickness_of_the_annual_ring: Толщина годового кольца (в метрах)

        :return: Возраст дерева

        Примеры:
        >>> tree = Tree("Вяз", 10, 6.4, 0.55)
        >>> tree.tree_age(0.02)
        """

        if not isinstance(thickness_of_the_annual_ring, float):
            raise TypeError("Толщина годового кольца должна быть типа float")
        if thickness_of_the_annual_ring <= 0:
            raise ValueError("Толщина годового кольца должна быть положительным числом")
        ...

    def percent_of_wood_on_site(self, total_number_of_trees: int):
        """
        Расчет процента данной породы древесины на участке

        :param total_number_of_trees: Общее количество деревьев на участке

        :return: Процент данной породы на участке

        Примеры:
        >>> tree = Tree("Вяз", 10, 6.4, 0.55)
        >>> tree.percent_of_wood_on_site(120)
        """

        if not isinstance(total_number_of_trees, int):
            raise TypeError("Общее количество деревьев на участке должно быть типа int")
        if total_number_of_trees <= 0:
            raise ValueError("Общее количество деревьев на участке должно быть положительным числом")
        if total_number_of_trees < self.tree_count:
            raise ValueError("Общее количество деревьев должно быть больше количества деревьев данной породы")
        ...


class Diploma:
    def __init__(self, student: str, title: str, required_page_count: int, last_written_page: int):
        """
        Создание и подготовка к работе объекта "Диплом"

        :param student: Имя студента
        :param title: Название дипломной работы
        :param required_page_count: Требуемое количество страниц в дипломной работе
        :param last_written_page: Последняя написанная страница

        Примеры:
        >>> diploma = Diploma("Лапшина В.И.", "Автоматизация проектирования СГП", 70, 55)  # инициализация экземпляра класса
        """

        self.student = student

        self.title = title

        if not isinstance(required_page_count, int):
            raise TypeError("Требуемое количество страниц в дипломной работе должно быть типа int")
        self.required_page_count = required_page_count

        if not isinstance(last_written_page, int):
            raise TypeError("Высота дерева должна быть типа int")
        if last_written_page < 0:
            raise ValueError("Последняя написанная страница не может быть отрицательным числом")
        self.last_written_page = last_written_page

    def add_last_written_page(self, written_pages: int):
        """
        Функция, добавляющая количество написанных страниц

        :param written_pages: Количество написанных страниц

        Примеры:
        >>> diploma = Diploma("Лапшина В.И.", "Автоматизация проектирования СГП", 70, 55)
        >>> diploma.add_last_written_page(4)
        """

        if not isinstance(written_pages, int):
            raise TypeError("Количество написанных страниц должно быть типа int")
        if written_pages < 0:
            raise ValueError("Количество написанных страниц не должно быть отрицательным числом")

        self.last_written_page += written_pages

    def percent_of_completion(self):
        """
        Расчет процента выполнения дипломной работы

        :return: Процент выполнения дипломной работы

        Примеры:
        >>> diploma = Diploma("Лапшина В.И.", "Автоматизация проектирования СГП", 70, 55)
        >>> diploma.percent_of_completion()
        """
        ...


class WoodenFence:
    def __init__(self, place: str, transparency: float, height: float, length: float):
        """
        Создание и подготовка к работе объекта "Деревянный забор"

        :param place: Месторасположение
        :param transparency: Прозрачность полотна забора (то, насколько скрыт внутренний двор)
        :param height: Высота забора (в метрах)
        :param length: Ширина забора (в метрах)

        Примеры:
        >>> woodenfence = WoodenFence ("Деревня Ступино", 0.7, 2.0, 25.5)  # инициализация экземпляра класса
        """

        self.place = place

        if not isinstance(transparency, (int, float)):
            raise TypeError("Прозрачность должна быть типа int или float")
        if transparency < 0:
            raise ValueError("Прозрачность полотна забора не может быть отрицательным числом")
        self.transparency = transparency

        if not isinstance(height, (int, float)):
            raise TypeError("Высота забора должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота забора должна быть положительным числом")
        self.height = height

        if not isinstance(length, (int, float)):
            raise TypeError("Высота забора должна быть типа int или float")
        if length <= 0:
            raise ValueError("Высота забора должна быть положительным числом")
        self.length = length

    def fence_square(self):
        """
        Расчет площади полотна забора (в квадратных метрах)

        :return: Площадь полотна забора

        Примеры:
        >>> woodenfence = WoodenFence ("Деревня Ступино", 0.7, 2.0, 25.5)
        >>> woodenfence.fence_square()
        """
        ...

    def fence_price(self, cost_of_1_meter_square: float):
        """
        Расчет стоимости деревянного забора

        :param cost_of_1_meter_square: Стоимость 1 квадратного метра полотна забора (в тыс. руб.)

        :return: Стоимость деревянного забора

        Примеры:
        >>> woodenfence = WoodenFence ("Деревня Ступино", 0.7, 2.0, 25.5)
        >>> woodenfence.fence_price(2.57)
        """

        if not isinstance(cost_of_1_meter_square, (int, float)):
            raise TypeError("Стоимость 1 квадратного метра полотна забора должна быть типа int или float")
        if cost_of_1_meter_square <= 0:
            raise ValueError("Стоимость 1 квадратного метра полотна забора должна быть положительным числом")
        ...

    def plank_width(self):
        """
        Расчет требуемой ширины доски

        :return: Требуемая ширина доски (в миллиметрах)

        Примеры:
        >>> woodenfence = WoodenFence ("Деревня Ступино", 0.7, 2.0, 25.5)
        >>> woodenfence.plank_width()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
