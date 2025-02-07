class Cell:
    def __init__(self):
        self.is_mine = False
        self.revealed = False
        self.adjacent_mines = 0

   def __init__(self, rows, cols, mines):
        self.size = rows * cols
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [-1] * (self.size)  # Инициализация значениями -1
        self.first_step = True
    def play(self):
      pass
    
    def place_mines(self, safe_row, safe_col):
      pass
    
    def print_board(self, reveal_mines=False):
      pass
    
    def get_neighbors(self, idx):
      pass
    
    def reveal(self, idx):
      pass       

index = row * cols + col

col = index % cols

row = index // cols

def get_neighbors(self, index):
    # Вычисляем строку и столбец из индекса
    row = index // self.cols
    column = index % self.cols
    # Инициализируем список для хранения индексов соседних клеток
    neighbors = []
    
    # Проходим по всем возможным соседям
    for i in range(row - 1, row + 2):  # r - 1, r, r + 1
        for j in range(column - 1, column + 2):  # c - 1, c, c + 1
            # Проверяем, чтобы не выйти за пределы поля
            if 0 <= i < self.rows and 0 <= j < self.cols:
                # Проверяем, чтобы не добавить саму клетку
                if i != row or j != column:
                    # Вычисляем индекс соседа и добавляем его в список
                    neighbor_index = i * self.cols + j
                    neighbors.append(neighbor_index)
    
    return neighbors

def get_neighbors(self, idx):
    r, c = divmod(idx, self.cols)
    return [i * self.cols + j for i in range(r - 1, r + 2) for j in range(c - 1, c + 2)
            if 0 <= i < self.rows and 0 <= j < self.cols and (i != r or j != c)]

def place_mines(self, safe_row, safe_col):
    def count_mines(idx):
        return sum(1 for ni in self.get_neighbors(idx) if self.board[ni] == 0)
    safe = set(self.get_neighbors(safe_row * self.cols + safe_col) + [safe_row * self.cols + safe_col])
    possible = [(i, j) for i in range(self.rows) for j in range(self.cols) if (i * self.cols + j) not in safe]
    list(map(lambda pos: self.board.__setitem__(pos[0] * self.cols + pos[1], 0), sample(possible, self.mines)))
    self.board = [-1 * (count_mines(idx) + 1) if cell != 0 else cell for idx, cell in enumerate(self.board)]

    def play(self):
    while True:
        print("\033[H\033[J", end="")  # очищаем терминал
        self.print_board()
        try:
            row, col = map(int, input("Enter row and column (0-9): ").split())
            assert 0 <= row < self.rows and 0 <= col < self.cols
        except (ValueError, AssertionError):
            print("Invalid input. Please enter numbers between 0 and 9.")
            continue
        idx = row * self.cols + col
        if self.first_step:
            self.place_mines(row, col)
            self.first_step = False

        if self.board[idx] == 0:
            print("You hit a mine! Game Over.")
            self.print_board(reveal_mines=True)
            break

        self.reveal(idx)

        if all(cell >= 0 for cell in self.board):
            print("Congratulations! You've cleared the minefield.")
            self.print_board(reveal_mines=True)
            break

        def reveal(self, idx):
    stack = [idx]
    while stack:
        current_idx = stack.pop()
        self.board[current_idx] = abs(self.board[current_idx])
        if self.board[current_idx] - 1 == 0:
            stack.extend(ni for ni in self.get_neighbors(current_idx) if self.board[ni] < 0)

   def print_board(self, reveal_mines=False):
    max_col_digits = len(str(self.cols - 1))
    max_row_digits = len(str(self.rows - 1))

    print(" " * (max_row_digits + 2) + " ".join(f"{i:>{max_col_digits}}" for i in range(self.cols)))

    for i in range(self.rows):
        row = ['X' if reveal_mines and value == 0 else
               str(abs(value) - 1) if reveal_mines and value < 0 else
               '*' if value <= 0 else str(value - 1)
               for value in (self.board[i * self.cols + j] for j in range(self.cols))]
        print(f"{i:>{max_row_digits}}: " + " ".join(f"{cell:>{max_col_digits}}" for cell in row))

if __name__ == "__main__":
    rows, cols, mines = (int(arg) for arg in sys.argv[1:]) if len(sys.argv) > 1 else (10, 10, 10)
    game = Minesweeper(rows, cols, mines)
    game.play()

import sys
from random import sample


class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.size = rows * cols
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [-1] * self.size
        self.first_step = True

    def play(self):
        while True:
            print("\033[H\033[J", end="")  # очищаем терминал
            self.print_board()
            try:
                row, col = map(int, input("Enter row and column (0-9): ").split())
                assert 0 <= row < self.rows and 0 <= col < self.cols
            except (ValueError, AssertionError):
                print("Invalid input. Please enter numbers between 0 and 9.")
                continue
            idx = row * self.cols + col
            if self.first_step:
                self.place_mines(row, col)
                self.first_step = False

            if self.board[idx] == 0:
                print("You hit a mine! Game Over.")
                self.print_board(reveal_mines=True)
                break

            self.reveal(idx)

            if all(cell >= 0 for cell in self.board):
                print("Congratulations! You've cleared the minefield.")
                self.print_board(reveal_mines=True)
                break

    def print_board(self, reveal_mines=False):
        max_col_digits = len(str(self.cols - 1))
        max_row_digits = len(str(self.rows - 1))

        print(" " * (max_row_digits + 2) + " ".join(f"{i:>{max_col_digits}}" for i in range(self.cols)))

        for i in range(self.rows):
            row = ['X' if reveal_mines and value == 0 else
                   str(abs(value) - 1) if reveal_mines and value < 0 else
                   '*' if value <= 0 else str(value - 1)
                   for value in (self.board[i * self.cols + j] for j in range(self.cols))]
            print(f"{i:>{max_row_digits}}: " + " ".join(f"{cell:>{max_col_digits}}" for cell in row))

    def place_mines(self, safe_row, safe_col):
        def count_mines(idx):
            return sum(1 for ni in self.get_neighbors(idx) if self.board[ni] == 0)

        safe = set(self.get_neighbors(safe_row * self.cols + safe_col) + [safe_row * self.cols + safe_col])
        possible = [(i, j) for i in range(self.rows) for j in range(self.cols) if (i * self.cols + j) not in safe]
        list(map(lambda pos: self.board.__setitem__(pos[0] * self.cols + pos[1], 0), sample(possible, self.mines)))
        self.board = [-1 * (count_mines(idx) + 1) if cell != 0 else cell for idx, cell in enumerate(self.board)]

    def get_neighbors(self, idx):
        r, c = divmod(idx, self.cols)
        return [i * self.cols + j for i in range(r - 1, r + 2)
                for j in range(c - 1, c + 2)
                if 0 <= i < self.rows and 0 <= j < self.cols and (i != r or j != c)]

    def reveal(self, idx):
        stack = [idx]
        while stack:
            current_idx = stack.pop()
            self.board[current_idx] = abs(self.board[current_idx])
            if self.board[current_idx] - 1 == 0:
                stack.extend(ni for ni in self.get_neighbors(current_idx) if self.board[ni] < 0)


if __name__ == "__main__":
    rows, cols, mines = (int(arg) for arg in sys.argv[1:]) if len(sys.argv) > 1 else (10, 10, 10)
    game = Minesweeper(rows, cols, mines)
    game.play()

class MinesweeperSolver(Minesweeper):
    def __init__(self, rows, cols, mines):
        super().__init__(rows, cols, mines)
        self.probabilities = [0] * self.size
        self.flagged = [False] * self.size

        self.place_mines(int(rows / 2), int(cols / 2))
        self.reveal(int(rows / 2 * cols + cols / 2))

def analyze_and_reveal(self):
    to_reveal = []
    self.probabilities = [0] * self.size
    flag_placed = False

    for idx, cell in enumerate(self.board):
        if cell <= 1:  # клетка не раскрыта или по соседству 0 мин
            continue

        unrevealed_neighbors = [n for n in self.get_neighbors(idx) if self.board[n] <= 0]
        flag_neighbors_count = sum(self.flagged[n] for n in self.get_neighbors(idx))

        #  если количество мин вокруг равно значению клетки то помечаем соседей флагом
        if cell - 1 == len(unrevealed_neighbors):
            for un_idx in unrevealed_neighbors:
                if not self.flagged[un_idx]:
                    self.flagged[un_idx] = True
                    flag_placed = True

        for un_idx in unrevealed_neighbors:
            # если соседняя клетка не помечена флагом
            if not self.flagged[un_idx]:
                if cell - 1 == flag_neighbors_count and un_idx not in to_reveal:
                    # если количество помеченных флагом клеток вокруг равно значению клетки
                    # добавляем ее в список для раскрытия
                    to_reveal.append(un_idx)
                # подсчитываем вероятность клетки быть заминированной на основании ее значения
                # и количества нераскрытых и не помеченных флагом клеток вокруг
                self.probabilities[un_idx] += (cell - 1) / (len(unrevealed_neighbors))

    if to_reveal:
        # открываем гарантированно безопасные клетки
        print("Reveal safe cells:", [divmod(safe_idx, self.cols) for safe_idx in to_reveal])
        list(map(self.reveal, to_reveal))
    elif flag_placed:
        # если безопасных клеток нет, но какая-то клетка была помечена флагом, следует проанализировать доску снова
        return True
    else:
        # находим клетку с минимальной вероятностью быть заминированной и пытаемся открыть
        probably_safe = (i for i, p in enumerate(self.probabilities) if p > 0 and not self.flagged[i])
        idx = min(probably_safe, key=lambda i: self.probabilities[i], default=None)
        if idx is not None:
            print("Try reveal:", divmod(idx, self.cols), self.board[idx])
            if self.board[idx] == 0:
                return False
            self.reveal(idx)
        else:
            return False
    return True

def solve(self):
    while (not_failed := self.analyze_and_reveal()) and not all(cell >= 0 for cell in self.board):
        self.print_board()

    if not_failed:
        print("Congratulations! You've cleared the minefield.")
    else:
        print("Auto-solver hit a mine! Game Over.")        

if __name__ == "__main__":
  tries = 5000
  success_rates = []
  mine_counts = range(10, 36)

  for m in mine_counts:
      rows, cols, mines = (int(arg) for arg in sys.argv[1:]) if len(sys.argv) > 1 else (10, 10, m)
      stat = 0
      for i in range(tries):
          solver = MinesweeperSolver(rows, cols, mines)
          stat += solver.solve()
      success_rate = stat / tries * 100
      success_rates.append(success_rate)
      print(m, success_rate)

  # Построение графика
  plt.figure(figsize=(8, 4))
  plt.plot(mine_counts, success_rates, marker='o')
  plt.title('Success Rate of Minesweeper Solver')
  plt.xlabel('Number of Mines')
  plt.ylabel('Success Rate (%)')
  plt.ylim(0, 100)
  plt.grid(True)
  plt.show()