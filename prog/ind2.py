#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    def __init__(self, amount):
        # Проверка, что сумма представлена корректно
        if not isinstance(amount, list) or len(amount) > 100:
            raise ValueError("Сумма должна быть списком из не более чем 100 цифр.")
        
        self.amount = amount

    def __str__(self):
        # Преобразование суммы в строку для удобного отображения
        return ''.join(map(str, self.amount))

    def get_rubles(self):
        # Получение суммы в рублях и копейках
        if len(self.amount) < 3:
            return "0.00"  # Если сумма меньше 3 цифр, то это 0.00
        else:
            rubles = ''.join(map(str, self.amount[:-2])) or '0'
            kopecks = ''.join(map(str, self.amount[-2:]))
            return f"{rubles}.{kopecks}"


if __name__ == '__main__':
    money = Money([4, 5, 2, 5, 1, 2, 4, 6])
    print(f"Сумма: {money}")
    print(f"Сумма в рублях и копейках: {money.get_rubles()}")
