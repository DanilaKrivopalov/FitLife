# Проект FitLife - MVP версия 1.0


WATER_CONST = 30  # Константа для подсчёта воды
RATIO_LITERS = 1000  # Константа для перевода в литры
# Подсказки для запроса данных от пользователя
USER_WEIGHT_PROMT = (
    "Введите ваш вес в кг (для отделения целой части " "используйте точку): "
)
USER_HEIGHT_PROMT = (
    "Введите ваш рост в кг (для отделения целой части " "используйте точку): "
)


# Поместим все рассчеты в функцию name
def main():
    """Основная функция прогрраммы: сбор информации и расчет показателей"""
    # Сбор данных
    user_name = input("Введите ваше имя: ")

    try:
        user_age = int(input("Введите ваш возраст: "))
        user_weight_float = float(input(USER_WEIGHT_PROMT).replace(",", "."))
        user_height_float = float(input(USER_HEIGHT_PROMT).replace(",", "."))

    except ValueError:
        print(
            "Чилсо введено неверно. Используйте цифры, а для разделения"
            " числа точку (например 79.8)",
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
