# Проект FitLife - MVP версия 1.0


WATER_CONST = 30  # Константа для подсчёта воды
RATIO_LITERS = 1000  # Константа для перевода в литры
# Подсказки для ввода данных
USER_WEIGHT = (
    "Введите ваш вес в кг (для отделения целой части " "используйте точку): "
)
USER_HEIGHT = (
    "Введите ваш рост в кг (для отделения целой части " "используйте точку): "
)


# Поместим все рассчеты в функцию name
def main():
    """Основная функция прогрраммы: сбор информации и расчет показателей"""
    # Сбор данных

    try:
        user_name = input("Введите ваше имя: ")
        user_age = input("Введите ваш возраст: ")
        user_weight_float = float(input(USER_WEIGHT).replace(",", "."))
        user_height_float = float(input(USER_HEIGHT).replace(",", "."))

    except ValueError:
        print(
            "Чилсо введено невнрно. Используйте цифры, а для разделения"
            " числа точку (например 79.8)"
        )
        return

    # Вычисления
    bmi = user_weight_float / (user_height_float**2)
    water_needed = (user_weight_float * WATER_CONST) / RATIO_LITERS

    print(
        f"\n Привет, {user_name}!\n",
        f"Ваш возраст: {user_age} лет\n",
        f"Ваш ИМТ составляет: {round(bmi, 1)} кг/м^2\n",
        f"Ваша норма воды составляет: {round(water_needed, 2)} л",
    )
    print("Расчёт окончен. Будьте здоровы!")


if __name__ == "__main__":
    main()
