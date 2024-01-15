import doctest
from typing import Any, Union

# TODO Написать 3 класса с документацией и аннотацией типов

class SocialNetwork:
    def __init__(self, name: str, age: int, text_message: Any):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Имя пользователя
        :param age: Возраст
        :param text_message: Текст сообщения
        """
        self.name = name
        self.age = age
        self.text_message = text_message

    def writes_greeting(self, name: str) -> str:
        """
        Приветствие пользователя

        :param name: Имя пользователя

        :return: Печатает приветствие с указанием имени пользователя

        Пример:
        >>> account = SocialNetwork('Любовь', 26, 'Всем привет!')
        >>> account.writes_greeting('Любовь')
        """
        ...

    def counts_the_year_of_birth(self, current_year: int, age: int) -> Any:
        """
        Метод считает год рождения пользователя

        :param current_year: Текущий год
        :param age: Возраст

        :return: Указывает год рождения

        Пример:
        >>> account = SocialNetwork('Любовь', 26, 'Всем привет!')
        >>> account.counts_the_year_of_birth(2024, 26)
        """
        if not isinstance(current_year, int):
            raise TypeError('Текущий год должен быть int')
        if not isinstance(age, int):
            raise TypeError('Возраст должен быть int')
        ...

    def makes_upper_letters(self, text_message: Any) -> Any:
        """
        Метод приводит все буквы текста к верхнему регистру. Все остальные символы остаются неизмененными.

        :param text_message: Текст сообщения

        :return: Возвращает копию текста заглавными буквами

        Пример:
        >>> account = SocialNetwork('Любовь', 26, 'Всем привет!')
        >>> account.makes_upper_letters('Всем привет!')
        """
        ...


class Worker:
    def __init__(self, work_days: int, payment: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Сотрудник"

        :param work_days: Количество рабочих дней
        :param payment: Стоимость одной рабочей смены
        """
        self.work_days = work_days
        self.payment = payment

    def counts_the_salary(self, work_days: int, payment: Union[int, float]) -> Any:
        """
        Метод считает зарплату

        :param work_days: Количество рабочих дней
        :param payment: Стоимость одной рабочей смены

        :return: Выводит результат умножения количества смен на стоимость одной смены

        Пример:
        >>> worker = Worker(15, 350.65)
        >>> worker.counts_the_salary(15, 350.65)
        """
        if not isinstance(work_days, int):
            raise TypeError('Количество рабочих дней должно быть int')
        if work_days < 0:
            raise ValueError('Количество рабочих дней не может быть отрицательным')
        if not isinstance(payment, Union[int, float]):
            raise TypeError('Значение должно быть int или float')
        if payment < 0:
            raise ValueError('Значение не может быть отрицательным')
        ...

    def counts_the_weekend(self, work_days: int, days_in_month: int) -> int:
        """
        Метод считает количество выходных дней в месяце

        :param work_days: Количество рабочих дней
        :param days_in_month: Количество дней в расчетном месяце

        :return: Выводит результат вычитания количества рабочих дней из общего количества дней в месяце

        Пример:
        >>> worker = Worker(15, 350.65)
        >>> worker.counts_the_weekend(15, 31)
        """
        ...


class Bus:
    def __init__(self, total_seats: int, occupied_seats: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param total_seats: Всего мест в автобусе
        :param occupied_seats: Количество занятых мест
        """
        self.total_seats = total_seats
        self.occupied_seats = occupied_seats

    def capacity_bus(self, total_seats: int, occupied_seats: int) -> Union[int, str]:
        """
        Метод считает на сколько процентов заполнен автобус

        :param total_seats: Всего мест в автобусе
        :param occupied_seats: Количество занятых мест

        :return: Выводит на сколько процентов заполнен автобус, округляет значение до целого числа

        Пример:
        >>> bus = Bus(60, 26)
        >>> bus.capacity_bus(60, 26)
        """
        if total_seats == occupied_seats:
            return "Все места заняты, дождитесь следующий автобус"
        ...

    def counts_travel_time(self, distance: Union[int, float], speed: int) -> int:
        """
        Метод вычисляет время, за которое автобус проедет определенное расстояние

        :param distance: Расстояние в км
        :param speed: Скорость в км/ч

        :return: Выводит количество минут

        Пример:
        >>> bus = Bus(60, 26)
        >>> bus.counts_travel_time(7, 60)
        """
        if speed == 0:
            raise ValueError('Автобус стоит на месте')
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
