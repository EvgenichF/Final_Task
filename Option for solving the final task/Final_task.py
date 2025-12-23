import numpy as np

def game_core_v3(number: int=1) -> int:
    """
    Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его на случайное число в диапазоне, в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    
    count = 0
    predict = np.random.randint(1,101)
    
    
    while number != predict:
        count +=1
        if number > predict:
            predict += np.random.randint(1,10)
        elif number < predict:
            predict -= np.random.randint(1,10)
    return count


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v3)