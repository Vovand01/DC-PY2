from typing import Union
import math


class Foundation:
    """ Базовый класс фундамента."""
    def __init__(self, load_capacity: int, area: Union[int, float], type: str):
        """
        Создание и подготовка к работе объекта "Фундамент"
        :param load_capacity: Несущая способность фундамента
        :param area: Площадь фундамента
        :param type: Тип фундамента по глубине заложения
        """
        self._load_capacity = load_capacity
        self._area = area
        self._type = type

    @property
    def load_capacity(self) -> int:
        """Возвращает несущую способность фундамента"""
        return self._load_capacity

    @load_capacity.setter  # применяем setter, чтобы проверить принимаемые значения
    def load_capacity(self, new_capacity: int) -> None:
        """Устанавливает несущую способность фундамента, предварительно сделав проверки"""
        if not isinstance(new_capacity, int):
            raise TypeError("Несущая способность должна быть типа int")
        if new_capacity < 0:
            raise ValueError("Несущая способность должна быть положительным числом")
        self._load_capacity = new_capacity

    @property
    def area(self) -> Union[int, float]:
        """Возвращает площадь фундамента"""
        return self._area

    @area.setter  # применяем setter, чтобы проверить принимаемые значения
    def area(self, new_area: Union[int, float]) -> None:
        """Устанавливает площадь фундамента, предварительно сделав проверки"""
        if not isinstance(new_area, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if new_area < 0:
            raise ValueError("Площадь должна быть положительным числом")
        self._area = new_area

    @property
    def type(self) -> str:
        """Возвращает тип фундамента"""
        return self._type

    @type.setter  # применяем setter, чтобы проверить принимаемые значения
    def type(self, new_type: str) -> None:
        """Устанавливает тип фундамента, предварительно сделав проверки"""
        if not isinstance(new_type, str):
            raise TypeError("Тип фундамента должен быть типа str")
        self._type = new_type

    def __str__(self) -> str:
        return f'Фундамент по глубине {self._type}, имеет площадь {self._area}, несущая способность - {self._load_capacity}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(load_capacity={self._load_capacity!r}, area={self._area!r}, type={self._type!r})'

    def number_of_floors(self, one_floor_weight: Union[int, float]) -> int:
        """
        Функция, считающая количество этажей здания, которое можно построить без превышения несущей способности фундамента
        :param one_floor_weight: Нагрузка от одного этажа
        :return: Количество этажей здания
        """
        if not isinstance(one_floor_weight, (int, float)):
            raise TypeError("Нагрузка от этажа должна быть типа int или float")
        if one_floor_weight < 0:
            raise ValueError("Нагрузка должна быть положительным числом")
        return self._load_capacity // one_floor_weight

    def volume_of_soil(self, foundation_thickness: float) -> float:
        """
        Функция, считающая объем грунта, который нужно вынуть для заложения фундамента
        :param foundation_thickness: Толщина фундамента
        :return: Объем грунта
        """
        if not isinstance(foundation_thickness, float):
            raise TypeError("Толщина фундамента должна быть типа float")
        if foundation_thickness < 0:
            raise ValueError("Толщина фундамента должна быть положительным числом")
        return self._area * foundation_thickness


class PileFoundation(Foundation):
    """ Дочерний класс фундамента."""
    def __init__(self, load_capacity: int, area: Union[int, float], type: str, number_of_piles: int, pile_length: int, pile_radius: float):
        """
        Создание и подготовка к работе объекта "Свайный фундамент"
        :param load_capacity: Несущая способность фундамента
        :param area: Площадь фундамента
        :param type: Тип фундамента по глубине заложения
        :param number_of_piles: Количество свай в фундаменте
        :param pile_length: Длина сваи
        :param pile_radius: Радиус сваи
        """
        super().__init__(load_capacity, area, type)
        self._number_of_piles = number_of_piles
        self._pile_length = pile_length
        self._pile_radius = pile_radius

    @property
    def number_of_piles(self) -> int:
        """Возвращает количество свай в фундаменте"""
        return self._number_of_piles

    @number_of_piles.setter  # применяем setter, чтобы проверить принимаемые значения
    def number_of_piles(self, new_number_of_piles: int) -> None:
        """Устанавливает количество свай в фундаменте, предварительно сделав проверки"""
        if not isinstance(new_number_of_piles, int):
            raise TypeError("Количество свай должно быть типа int")
        if new_number_of_piles < 0:
            raise ValueError("Количество свай должно быть положительным числом")
        self._number_of_piles = new_number_of_piles

    @property
    def pile_length(self) -> int:
        """Возвращает длину сваи"""
        return self._pile_length

    @pile_length.setter  # применяем setter, чтобы проверить принимаемые значения
    def pile_length(self, new_length: int) -> None:
        """Устанавливает длину сваи, предварительно сделав проверки"""
        if not isinstance(new_length, int):
            raise TypeError("Длина сваи должна быть типа int")
        if new_length < 0:
            raise ValueError("Длина сваи должна быть положительным числом")
        self._pile_length = new_length

    @property
    def pile_radius(self) -> float:
        """Возвращает радиус сваи"""
        return self._pile_radius

    @pile_radius.setter  # применяем setter, чтобы проверить принимаемые значения
    def pile_radius(self, new_radius: float) -> None:
        """Устанавливает длину сваи, предварительно сделав проверки"""
        if not isinstance(new_radius, float):
            raise TypeError("Радиус сваи должен быть типа float")
        if new_radius < 0:
            raise ValueError("Радиус сваи должен быть положительным числом")
        self._pile_radius = new_radius

    def __str__(self) -> str:
        return (f'Фундамент по глубине {self._type}, имеет площадь {self._area}, несущая способность - {self._load_capacity}, '
                f'количество свай равно {self._number_of_piles}, длина сваи - {self._pile_length}, радиус - {self._pile_radius}')

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(load_capacity={self._load_capacity!r}, area={self._area!r}, type={self._type!r},'
                f'number_of_piles={self._number_of_piles}, pile_length={self._pile_length}, pile_radius={self._pile_radius})')

    def volume_of_soil(self, foundation_thickness: float) -> float:
        """
        Функция, считающая объем грунта, который нужно вынуть для заложения фундамента
        Метод перегружен, т.к. объем считается по-другому из-за появления свай в грунте
        :param foundation_thickness: Толщина фундамента
        :return: Объем грунта
        """
        if not isinstance(foundation_thickness, float):
            raise TypeError("Толщина фундамента должна быть типа float")
        if foundation_thickness < 0:
            raise ValueError("Толщина фундамента должна быть положительным числом")
        return self._area * foundation_thickness + math.pi * self._pile_radius ** 2 * self._pile_length


if __name__ == "__main__":
    foundation_1 = Foundation(40000, 600, "глубокого заложения")
    foundation_2 = PileFoundation(50000, 1000, "свайный", 75, 20, 1.2)
    print(foundation_1)
    print(foundation_2)
    print(repr(foundation_1))
    print(repr(foundation_2))
    print(foundation_1.number_of_floors(7000), foundation_1.volume_of_soil(0.7))
    print(foundation_2.number_of_floors(4600), foundation_2.volume_of_soil(0.9))