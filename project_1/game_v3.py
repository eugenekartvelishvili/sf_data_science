import numpy as np

random_n = np.random.randint(1, 101)  # Случайное число

def random_predict_v2(number: int = 1) -> int:
    """Угадываем наше число методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток, потребовавшихся для угадывания числа.
    """

    low_bound = 1
    high_bound = 100
    count = 0

    while True:
        count += 1
        guess_n = (low_bound + high_bound) // 2  # Предполагаем, что число в середине интервала

        if guess_n == number:
            return count  # Если угадали, возвращаем количество попыток
            break # Выходим из цикла в случае успеха
        elif guess_n < number:
            low_bound = guess_n + 1  # Сужаем интервал снизу
        else:
            high_bound = guess_n - 1  # Сужаем интервал сверху

    return count  # Если не угадали, возвращаем количество попыток

# Тестирование функции
attempts = random_predict_v2(random_n)  # Алгоритм пытается угадать число
print(f"Загаданное число: {random_n}")
print(f"Количество попыток: {attempts}")



def score_game(random_predict_v2) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм.

    Args:
        random_predict_v2 (callable): Функция угадывания числа.

    Returns:
        int: Среднее количество попыток.
    """

    count_ls = []  # Список для сохранения количества попыток
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_v2(number))

    score = int(np.mean(count_ls))  # Находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# Тестирование функции
score_game(random_predict_v2)
