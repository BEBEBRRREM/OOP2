#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        # Проверка корректности значений
        if not isinstance(first, int) or first <= 0 or first not in [1, 2, 5, 10, 50, 100, 500, 1000, 5000]:
            raise ValueError(
                "'first' должно быть положительным числом из набора.")
        if not isinstance(second, int) or second <= 0:
            raise ValueError("'second' должно быть положительным целым числом.")
        
        self.first = first
        self.second = second

    def __mul__(self):
        return self.first * self.second
    
    def __str__(self):
        return print(f"Всего {self.second} по {self.first}")
    

def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    # Реализация вводы данных из кода
    pair = make_pair(5000, 67)
    pair.__str__()
    print(f"Общая сумма: {pair.first * pair.second}")
