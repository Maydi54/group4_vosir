import random
import os

# Глобальные константы
SIZE = 4

def initialize_game():
    """Инициализация игрового поля"""
    numbers = list(range(1, 16)) + [0]
    
    while True:
        random.shuffle(numbers)
        if is_solvable(numbers):
            break
    
    board = []
    empty_pos = (3, 3)
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            num = numbers[i * SIZE + j]
            row.append(num)
            if num == 0:
                empty_pos = (i, j)
        board.append(row)
    
    return board, empty_pos, 0

def is_solvable(numbers):
    """Проверка решаемости конфигурации"""
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] != 0 and numbers[j] != 0 and numbers[i] > numbers[j]:
                inversions += 1
    
    empty_row = SIZE - (numbers.index(0) // SIZE)
    return (inversions % 2) == (empty_row % 2)

def is_valid_move(row, col):
    """Проверка валидности позиции"""
    return 0 <= row < SIZE and 0 <= col < SIZE
