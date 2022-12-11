class Box:
    def __init__(self, height: int, width: int, length: int, material: str):
        """
        :param width: Ширина коробки
        :param height: Высота коробки
        :param length: Длина коробки
        :param material: Материал коробки

        Примеры:
        >>> table = Box(1, 1, 2, "pine")
        """
        if not isinstance(width, int):
            raise TypeError
        if not width > 0:
            raise ValueError
        if not isinstance(height, int):
            raise TypeError
        if not height > 0:
            raise ValueError
        if not isinstance(length, int):
            raise TypeError
        if not length > 0:
            raise ValueError
        if not isinstance(material, str):
            raise TypeError

        self.width = width
        self.height = height
        self.length = length
        self.material = material

    def rotate(self, axis: str, side: str):
        """
        Меняет местами значения length, width и height
        :param axis: Ось поворота (x, y, z)
        :param side: Направление поворота (left, right)
        :raise ValueError: Строка не является названием оси. Допустимые значения: x, y, z
        :raise ValueError: Строка не является стороной поворота. Допустимые значения: left, right

        :return: None

        Примеры:
        >>> table = Box(1, 1, 2, "pine")
        >>> table.rotate("x", "left")
        """
        ...

    def changeMaterial(self, newMaterial: str):
        """
        Меняет материал коробки
        :param newMaterial: Новый материал
        :raise ValueError: Строка не является материалом.

        :return: None

        Примеры:
        >>> table = Box(1, 1, 2, "pine")
        >>> table.changeMaterial("oak")
        """
        ...


class Cat:
    def __init__(self, nickname: str, age: int):
        """
            :param nickname: Кличка собаки
            :param age: Возраст собаки

            Примеры:
            >>> dog = Cat("Jack", 5)
        """
        if not isinstance(nickname, str):
            raise TypeError
        if not isinstance(age, int):
            raise TypeError
        if not age > 0:
            raise ValueError

        self.nickname = nickname
        self.age = age

    def pet(self):
        """
        Погладить кота

        :return: None

        Примеры:
        >>> dog = Cat("Jack", 5)
        >>> dog.pet()
        """
        ...

    def rename(self, newName: str):
        """
        Изменить кличку
        :param newName: Новая кличка

        :return: None

        Примеры:
        >>> dog = Cat("Jack", 5)
        >>> dog.rename("John")
        """
        ...

class Window:
    def __init__(self, width: int, height: int, isOpened: bool):
        """
        :param width: Ширина окна
        :param height: Высота окна
        :param isOpened: Открыто ли окно

        Примеры:
        >>> window = Window(1, 2, False)
        """
        if not isinstance(width, int):
            raise TypeError
        if not width > 0:
            raise ValueError
        if not isinstance(height, int):
            raise TypeError
        if not height > 0:
            raise ValueError
        if not isinstance(isOpened, bool):
            raise TypeError

        self.width = width
        self.height = height
        self.isOpened = isOpened

    def open(self):
        """
        Меняет состояние атрибута isOpened на True
        :return: True

        Примеры:
        >>> window = Window(1, 2, False)
        >>> window.open()
        True
        """
        self.isOpened = True
        return self.isOpened

    def close(self):
        """
        Меняет состояние атрибута isOpened на False
        :return: False

        Примеры:
        >>> window = Window(1, 2, True)
        >>> window.close()
        False
        """
        self.isOpened = False
        return self.isOpened


if __name__ == "__main__":
    import doctest

    doctest.testmod()
