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

def print_board(board, moves_count):
    """Красивый вывод игрового поля"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("🎮 ИГРА 'ПЯТНАШКИ' (15 Puzzle)")
    print("=" * 40)
    print(f"Ходов сделано: {moves_count}")
    print("Управление: W - вверх, A - влево, S - вниз, D - вправо")
    print("Цель: расположить числа по порядку")
    print("=" * 40)
    print()
    
    for i in range(SIZE):
        print(" " + "─" * 25)
        print("│", end="")
        for j in range(SIZE):
            num = board[i][j]
            if num == 0:
                print("     │", end="")
            else:
                print(f" {num:2d}  │", end="")
        print()
    print(" " + "─" * 25)
    print()

def show_help():
    """Показать справку"""
    print("\n" + "=" * 50)
    print("🎯 СПРАВКА ПО УПРАВЛЕНИЮ")
    print("=" * 50)
    print("W - переместить плитку ВВЕРХ")
    print("S - переместить плитку ВНИЗ")
    print("A - переместить плитку ВЛЕВО")
    print("D - переместить плитку ВПРАВО")
    print("H - показать эту справку")
    print("R - перезапустить игру")
    print("Q - выйти из игры")
    print("=" * 50)
    input("\nНажмите Enter для продолжения...")

