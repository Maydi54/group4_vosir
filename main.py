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

def get_direction(move):
    """Преобразование ввода в направление"""
    move = move.upper()
    
    directions = {
        'W': (-1, 0),    # вверх
        'S': (1, 0),     # вниз
        'A': (0, -1),    # влево
        'D': (0, 1),     # вправо
    }
    
    return directions.get(move)

def move_tile(board, empty_pos, direction):
    """Перемещение плитки"""
    empty_row, empty_col = empty_pos
    target_row = empty_row + direction[0]
    target_col = empty_col + direction[1]
    
    if not is_valid_move(target_row, target_col):
        return board, empty_pos, False
    
    # Меняем местами пустую клетку и целевую плитку
    board[empty_row][empty_col] = board[target_row][target_col]
    board[target_row][target_col] = 0
    empty_pos = (target_row, target_col)
    
    return board, empty_pos, True

def is_solved(board):
    """Проверка решения"""
    expected = 1
    for i in range(SIZE):
        for j in range(SIZE):
            if i == SIZE - 1 and j == SIZE - 1:
                if board[i][j] != 0:
                    return False
            else:
                if board[i][j] != expected:
                    return False
                expected += 1
    return True

def get_available_moves(empty_pos):
    """Получение доступных ходов"""
    available = []
    empty_row, empty_col = empty_pos
    
    moves = {
        'W': (-1, 0), 'S': (1, 0), 
        'A': (0, -1), 'D': (0, 1)
    }
    
    for move, direction in moves.items():
        target_row = empty_row + direction[0]
        target_col = empty_col + direction[1]
        if is_valid_move(target_row, target_col):
            available.append(move)
    
    return available

def main():
    """Основная функция игры"""
    print("🎮 Добро пожаловать в игру 'Пятнашки'!")
    print("Перемещайте плитки, чтобы расположить числа от 1 до 15 по порядку.")
    
    board, empty_pos, moves_count = initialize_game()
    show_help()
    
    while True:
        print_board(board, moves_count)
        
        if is_solved(board):
            print("🎉 ПОЗДРАВЛЯЮ! Вы решили головоломку!")
            print(f"📊 Количество ходов: {moves_count}")
            break
        
        available_moves = get_available_moves(empty_pos)
        print(f"Доступные ходы: {', '.join(available_moves)}")
        
        try:
            user_input = input("\nВведите ход (WASD/H/R/Q): ").strip().upper()
            
            if user_input in ['Q', 'QUIT', 'EXIT']:
                print("👋 До свидания!")
                break
            elif user_input in ['H', 'HELP']:
                show_help()
                continue
            elif user_input in ['R', 'RESTART']:
                board, empty_pos, moves_count = initialize_game()
                print("🔄 Игра перезапущена!")
                continue
            
            direction = get_direction(user_input)
            
            if direction:
                board, empty_pos, moved = move_tile(board, empty_pos, direction)
                if moved:
                    moves_count += 1
                    print("✅ Ход выполнен!")
                else:
                    print("❌ Невозможно выполнить этот ход!")
            else:
                print("❌ Неверная команда! Используйте W, A, S, D, H, R или Q")
            
            input("Нажмите Enter для продолжения...")
            
        except (KeyboardInterrupt, EOFError):
            print("\n👋 До свидания!")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
