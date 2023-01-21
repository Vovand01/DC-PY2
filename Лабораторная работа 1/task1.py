from typing import Union
import doctest


class Wheel:
    def __init__(self, radius: Union[int, float], protector_thickness: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Колесо"

        :param radius: Радиус колеса
        :param protector_thickness: Толщина протектора шины колеса

        Примеры:
        >>> wheel = Wheel(50, 4)
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус колеса должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус колеса должен быть положительным числом")
        self.radius = radius

        if not isinstance(protector_thickness, (int, float)):
            raise TypeError("Толщина протектора должна быть типа int или float")
        if protector_thickness < 0:
            raise ValueError("Толщина протектора должна быть неотрицательным числом")
        self.protector_thickness = protector_thickness

    def circumference_length(self) -> float:
        """
        Функция, которая считает длину окружности колеса

        :return: Длина окружности колеса

        Примеры:
        >>> wheel = Wheel(20, 3)
        >>> wheel.circumference_length()
        """
        ...

    def comparison_of_protector_thickness(self, minimal_thickness: Union[int, float]) -> bool:
        """
        Функция, сравнивающая толщину протектора шины колеса с минимально допустимой для безопасной езды толщиной, значение которой вводится пользователем

        :param minimal_thickness: Минимально допустимая толщина протектора

        :return: Превышает ли толщина протектора минимально допустимую толщину

        Примеры:
        >>> wheel = Wheel(20, 3)
        >>> wheel.comparison_of_protector_thickness(2.5)
        """
        if not isinstance(minimal_thickness, (int, float)):
            raise TypeError("Значение минимально допустимой толщины должно быть типа int или float")
        if minimal_thickness <= 0:
            raise ValueError("Значение минимально допустимой толщины должно быть положительным числом")
        ...

    def conversion_to_inches(self) -> float:
        """
        Функция, переводящая значение радиуса колеса из миллиметров в дюймы

        :return: Радиус колеса в дюймах

        Примеры:
        >>> wheel = Wheel(20, 3)
        >>> wheel.conversion_to_inches()
        """
        ...


class Flat:
    def __init__(self, area: Union[int, float], number_of_tenants: int):
        """
        Создание и подготовка к работе объекта "Квартира"

        :param area: Площадь квартиры
        :param number_of_tenants: Количество людей, живущих в квартире

        Примеры:
        >>> flat = Flat(33.98, 2)
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь квартиры должна быть типа int или float")
        if not area > 0:
            raise ValueError("Площадь квартиры должна быть положительным числом")
        self.area = area

        if not isinstance(number_of_tenants, int):
            raise TypeError("Число жильцов должно быть целым числом")
        if not number_of_tenants > 0:
            raise ValueError("Число жильцов должно быть положительным числом")
        self.number_of_tenants = number_of_tenants

    def room_for_every_tenant(self, number_of_rooms: int) -> bool:
        """
        Функция, проверяющая, приходится ли на каждого жильца отдельная комната в квартире

        :param number_of_rooms: Количество комнат в квартире

        :return: Может ли каждый жилец жить в отдельной комнате

        Примеры:
        >>> flat = Flat(47.8, 3)
        >>> flat.room_for_every_tenant(2)
        """
        if not isinstance(number_of_rooms, int):
            raise TypeError("Число комнат должно быть целым числом")
        if not number_of_rooms > 0:
            raise ValueError("Число комнат должно быть положительным числом")
        ...

    def average_area(self) -> float:
        """
        Функция, вычисляющая среднюю площадь, приходящуюся на одного жильца квартиры

        :return: Средняя площадь на одного жильца квартиры

        Примеры:
        >>> flat = Flat(47.8, 3)
        >>> flat.average_area()
        """
        ...

    def volume_of_flat(self, floor_height: Union[int, float]) -> float:
        """
        Функция, которая считает объем квартиры

        :param floor_height: Высота квартиры

        :return: Строительный объем квартиры

        Примеры:
        >>> flat = Flat(47.8, 3)
        >>> flat.volume_of_flat(2.8)
        """
        if not isinstance(floor_height, (int, float)):
            raise TypeError("Высота квартиры должна быть типа int или float")
        if not floor_height > 0:
            raise ValueError("Высота квартиры должна быть положительным числом")
        ...

class CreditCard:
    def __init__(self, credit_limit: int, percent: Union[int, float], average_month_wastes: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Кредитная карта"

        :param credit_limit: Лимит средств кредитной карты
        :param percent: Процент, который нужно доплачивать банку за оборот средств с кредитной карты
        :param average_month_wastes: Средние ежемесячные траты

        Примеры:
        >>> credit_card = CreditCard(200000, 5, 45000)
        """
        if not isinstance(credit_limit, int):
            raise TypeError("Кредитный лимит должен быть целым числом")
        if not credit_limit > 0:
            raise ValueError("Кредитный лимит должен быть положительным числом")
        self.credit_limit = credit_limit

        if not isinstance(percent, (int, float)):
            raise TypeError("Процент должен быть типа int или float")
        if not percent > 0:
            raise ValueError("Процент должен быть положительным числом")
        if percent > 100:
            raise ValueError("Процент не может быть больше 100")
        self.percent = percent

        if not isinstance(average_month_wastes, (int, float)):
            raise TypeError("Средние траты за месяц должны быть типа int или float")
        if not average_month_wastes > 0:
            raise ValueError("Средние траты за месяц должны быть положительным числом")
        if average_month_wastes > credit_limit:
            raise ValueError("Средние траты за месяц не могут быть больше лимита кредитной карты")
        self.average_month_wastes = average_month_wastes

    def increase_of_wastes(self, addition: int) -> None:
        """
        Функция, которая увеличивает траты за месяц

        :param addition: Значение, на которое увеличиваются ежемесячные траты

        :raise ValueError: Если средние траты за месяц больше лимита кредитной карты, то вызывается ошибка

        Примеры:
        >>> credit_card = CreditCard(200000, 5, 45000)
        >>> credit_card.increase_of_wastes(5000)
        """
        if not isinstance(addition, int):
            raise TypeError("Добавочное значение к ежемесячным тратам должно быть целым числом")
        if not addition > 0:
            raise ValueError("Добавочное значение к ежемесячным тратам должно быть положительным числом")
        ...

    def amount_with_percent(self, amount: Union[int, float]) -> float:
        """
        Функция, которая считает сумму с процентами, которую надо будет положить на карту, в случае снятия средств с нее

        :param amount: Сумма средств, взятых с кредитной карты

        :raise ValueError: Если сумма средств, снятых с кредитной карты, больше лимита карты, то вызывается ошибка

        :return: Сумма, которую нужно вернуть на карту, с процентами

        Примеры:
        >>> credit_card = CreditCard(200000, 5, 45000)
        >>> credit_card.amount_with_percent(10000)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if not amount > 0:
            raise ValueError("Сумма должна быть положительным числом")
        ...

    def number_of_months(self) -> int:
        """
        Функция, которая считает, на сколько месяцев хватит средств на кредитной карте при заданных ежемесячных тратах (в предположении, что баланс карты не пополняется)

        :return: Количество месяцев

        Примеры:
        >>> credit_card = CreditCard(200000, 5, 45000)
        >>> credit_card.number_of_months()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
