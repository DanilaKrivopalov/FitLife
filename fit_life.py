# Проект FitLife - MVP версия 1.0

WATER_CONST = 30  # Константа для подсчёта воды
RATIO_LITERS = 1000  # Константа для перевода в литры


# 1. Знакомство
user_name = input('Введите ваше имя: ')
user_age = input('Введите ваш возраст: ')
user_age_int = int(user_age)  # Преобразуем в тип целое число


# 2. Сбор данных
user_weight = (
    'Введите ваш вес в кг (для отделения целой части '
    'используйте точку): '
)
user_height = (
    'Введите ваш рост в метрах (для отделения целой части '
    'используйте точку): '
)

# Преобразуем в тип число с плавающей точкой
user_weight_float = float(input(user_weight))
user_height_float = float(input(user_height))


# 3. Логика расчётов (Функции как «чёрный ящик»: используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight_float / (user_height_float ** 2)


# Подсчёт воды: вес * 30 мл
water_needed = (user_weight_float * WATER_CONST) / RATIO_LITERS


# 4. Вывод красивого результата
print(
    f'Привет, {user_name}!\n',
    f'Ваш возраст: {user_age} лет\n',
    f'Ваш ИМТ составляет: {round(bmi, 1)} кг/м^2\n',
    f'Ваша норма воды составляет: {round(water_needed, 2)} л')
print("Расчёт окончен. Будьте здоровы!")
