class Wall:
    def __init__(self, id_: (str, int, float), length: int, width: int, height: int):
        """
        Создание базового класса - "Стена"

        :param id_: Идентификационный номер стены
        :param length: Длина стены (в миллиметрах)
        :param width: Ширина стены (в миллиметрах)
        :param height: Высота стены (в миллиметрах)
        """
        if not isinstance(id_, (str, int, float)):
            raise TypeError("Идентификатор стены может передаваться только в виде строки или числа")
        self._id = id_

        if not isinstance(length, (int, float)):
            raise TypeError("Длина стены должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина стены должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стены должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина стены должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота стены должна быть типа int или float")
        if height == 0:  # Высота стены может быть отрицательным числом в зависимости от расположения нулевого уровня
            raise ValueError("Высота стены не может быть равна 0")
        self.height = height

    @property  # Инкапсуляция для атрибута id (данный атрибут не должен изменяться)
    def id(self):
        """Возвращает идентификационный номер стены."""
        return self._id

    def volume(self):
        """
        Функция для подсчета объема стены.

        :return: Объем стены в метрах кубических.
        """
        return (self.length * self.width * self.height)/(10**9)

    def lateral_surface_area(self):
        """
        Функция для подсчета площади боковой поверхности.

        :return: Площадь боковой поверхности в метрах квадратных.
        """
        return (self.length * self.height * 2)/(10**6)

    def __str__(self) -> str:
        """
        Магический метод для представления информации о стене в человекочитаемой текстовой форме.

        :return: Строка о стене.
        """
        return f"Стена с идентификационным №: '{self.id}'. " \
               f"Длина = {self.length} (мм). " \
               f"Ширина = {self.width} (мм). " \
               f"Высота = {self.height} (мм). " \
               f"Объем = {self.volume()} (м^3). " \
               f"Площадь боковой поверхности = {self.lateral_surface_area()} (м^2)."

    def __repr__(self) -> str:
        """
        Магический метод для внутреннего представления объекта.

        :return: Строка о стене.
        """
        return f"{self.__class__.__name__} " \
               f"(id={self.id!r}, " \
               f"length={self.length!r}, " \
               f"width={self.width!r}, " \
               f"height={self.height!r})"


class BrickWall(Wall):
    def __init__(self, id_: (str, int, float), length: int, width: int, height: int, material: str, brick_mark: str, mortar_mark: str):
        """
        Создание дочернего класса - "Кирпичная стена"

        :param id_: Идентификационный номер стены
        :param length: Длина стены (в миллиметрах)
        :param width: Ширина стены (в миллиметрах)
        :param height: Высота стены (в миллиметрах)
        :param material: Материал стены (прилагательное)
        :param brick_mark: Марка кирпича
        :param mortar_mark: Марка раствора
        """
        super().__init__(id_, length, width, height)

        if not isinstance(material, str):
            raise TypeError("Материал стены может передаваться только в виде строки")
        self._material = material

        if not isinstance(brick_mark, str):
            raise TypeError("Марка кирпича может передаваться только в виде строки")
        self.brick_mark = brick_mark

        if not isinstance(mortar_mark, str):
            raise TypeError("Марка раствора может передаваться только в виде строки")
        self.mortar_mark = mortar_mark

    @property  # Инкапсуляция для атрибута material (данный атрибут не должен изменяться)
    def material(self):
        """Возвращает материал стены."""
        return self._material

    def brick_count(self, volume_brick: (int, float) = 0.00195, mortar_percent: float = 0.25):
        """
        Функция для подсчета целого количества кирпичей в стене.

        :param: volume_brick: Объем 1 кирпича в метрах кубических (по умолчанию = 0.00195 м3)
        :param: mortar_percent: Доля расвора в объеме стены (по умолчанию = 0.25, то есть 25 %)

        :return: Строка с целым количеством кирпичей в стене.
        """
        return f"Целое количество кирпичей в стене = {int((self.volume() * (1-mortar_percent)) / volume_brick)} штук."  # для формулы используем метод из базового класса self.volume()

    def cost(self, cost_1m3: (int, float)):
        """
        Функция для подсчета стоимости кирпичной стены.

        :param: cost_1m3: Стоимость 1 метра кубического кирпичной стены (по умолчанию = 0 тыс.руб.)

        :return: Строка со стоимостью кирпичной стены (тыс.руб.)
        """
        if not isinstance(cost_1m3, (int, float)):
            raise TypeError("Стоимость должна быть числом")

        return f"Стоимость киричной стены {(self.volume() * cost_1m3)} тыс.рублей."  # для формулы используем метод из базового класса self.volume()

    def __str__(self) -> str:
        """
        Перегрузка магического метода для представления информации о кирпичной стене в человекочитаемой текстовой форме.

        :return: Строка о кирпичной стене.
        """
        return f"{self._material} {super().__str__()} " \
               f"Марка кирпича: {self.brick_mark}. " \
               f"Марка раствора: {self.mortar_mark}. "

    def __repr__(self) -> str:
        """
        Перегрузка магического метода для внутреннего представления объекта.

        :return: Строка о кирпичной стене.
        """
        return f"{super().__repr__()}; " \
               f"(brick_mark={self.brick_mark!r}, " \
               f"mortar_mark={self.mortar_mark!r})"


if __name__ == "__main__":
    # Пример использования дочернего класса "Кирпичная стена"
    brickwall = BrickWall("13tyn", 4600, 250, 2700, "Кирпичная", "М75", "М25")  # Инициализируем кирпичную стену
    print(brickwall.volume())  # Метод базового класса по подсчету объема стены. Вывод: 3.105
    print(brickwall.lateral_surface_area())  # Метод базового класса по подсчету площади боковой поверхности стены. Вывод: 24.84
    print(brickwall)  # Вывод: Кирпичная Стена с идентификационным №: '13tyn'. Длина = 4600 (мм). Ширина = 250 (мм). Высота = 2700 (мм). Объем = 3.105 (м^3). Площадь боковой поверхности = 24.84 (м^2). Марка кирпича: М75. Марка раствора: М25.
    print(brickwall.__repr__())  # Вывод: BrickWall (id='13tyn', length=4600, width=250, height=2700); (brick_mark='М75', mortar_mark='М25')
    print(brickwall.brick_count())  # Метод дочернего класса (со значениями по умолчанию). Вывод: Целое количество кирпичей в стене = 1194 штук.
    print(brickwall.brick_count(0.00205, 0.3))  # Метод дочернего класса (с заданными значениями). Вывод: Целое количество кирпичей в стене = 1060 штук.
    print(brickwall.cost(5))  # Метод дочернего класса. Вывод: Стоимость киричной стены 15.525 тыс.рублей.
    pass
