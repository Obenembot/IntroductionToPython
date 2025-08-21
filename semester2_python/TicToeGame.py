import random

class Player:
    def __init__(self, name, symbol, is_computer=False):
        self.name = name
        self.symbol = symbol
        self.is_computer = is_computer


class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        self.rows = {"A": 0, "B": 1, "C": 2}

    def display(self):
        print("\n    1   2   3")
        print("  +---+---+---+")
        for row_label, row in zip(self.rows.keys(), self.grid):
            print(f"{row_label} | {' | '.join(row)} |")
            print("  +---+---+---+")

    def is_valid_move(self, position):
        if len(position) != 2:
            return False
        row, col = position[0].upper(), position[1]
        if row not in self.rows or not col.isdigit():
            return False
        col = int(col) - 1
        return 0 <= col <= 2 and self.grid[self.rows[row]][col] == " "

    def make_move(self, position, symbol):
        row, col = position[0].upper(), int(position[1]) - 1
        self.grid[self.rows[row]][col] = symbol

    def get_available_moves(self):
        moves = []
        for r, row in zip(self.rows.keys(), self.grid):
            for c in range(3):
                if row[c] == " ":
                    moves.append(f"{r}{c+1}")
        return moves

    def check_winner(self, symbol):
        # Check rows, columns, diagonals
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)):  # Row
                return True
            if all(self.grid[j][i] == symbol for j in range(3)):  # Column
                return True
        if all(self.grid[i][i] == symbol for i in range(3)):  # Diagonal
            return True
        if all(self.grid[i][2-i] == symbol for i in range(3)):  # Anti-diagonal
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.grid for cell in row)

    def reset(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]




class Game:
    def __init__(self):
        self.scoreboard = {"X": 0, "O": 0, "Draws": 0}
        self.board = Board()

    def choose_mode(self):
        print("=== Welcome to Tic Tac Toe ===")
        print("Select game mode:\n1. Player vs Player\n2. Player vs Computer")
        while True:
            choice = input("Enter 1 or 2: ")
            if choice in ["1", "2"]:
                return int(choice)
            print("Invalid choice! Try again.")

    def get_players(self, mode):
        name1 = input("Enter Player 1 name (X): ")
        if mode == 1:
            name2 = input("Enter Player 2 name (O): ")
            return Player(name1, "X"), Player(name2, "O")
        else:
            return Player(name1, "X"), Player("Computer", "O", is_computer=True)

    def computer_move(self):
        moves = self.board.get_available_moves()
        # 1. Try to win
        for move in moves:
            self.board.make_move(move, "O")
            if self.board.check_winner("O"):
                return move
            self.board.make_move(move, " ")
        # 2. Block player win
        for move in moves:
            self.board.make_move(move, "X")
            if self.board.check_winner("X"):
                self.board.make_move(move, " ")
                return move
            self.board.make_move(move, " ")
        # 3. Take center
        if "B2" in moves:
            return "B2"
        # 4. Take corners
        for corner in ["A1", "A3", "C1", "C3"]:
            if corner in moves:
                return corner
        # 5. Random move
        return random.choice(moves)

    def play_round(self, player1, player2):
        current_player = player1
        self.board.reset()
        self.board.display()

        while True:
            if current_player.is_computer:
                position = self.computer_move()
                print(f"Computer chooses (0): {position}")
            else:
                position = input(f"{current_player.name}'s turn ({current_player.symbol}): ").upper()
                while not self.board.is_valid_move(position):
                    position = input("Invalid move! Try again e.g A1: ").upper()

            self.board.make_move(position, current_player.symbol)
            self.board.display()

            if self.board.check_winner(current_player.symbol):
                print(f"\n🎉 {current_player.name} wins!")
                self.scoreboard[current_player.symbol] += 1
                break

            if self.board.is_draw():
                print("\nIt's a draw!")
                self.scoreboard["Draws"] += 1
                break

            current_player = player1 if current_player == player2 else player2

    def show_scoreboard(self):
        print("\n=== SCOREBOARD ===")
        print(f"Player X Wins: {self.scoreboard['X']}")
        print(f"Player O Wins: {self.scoreboard['O']}")
        print(f"Draws: {self.scoreboard['Draws']}")

    def start(self):
        mode = self.choose_mode()
        player1, player2 = self.get_players(mode)

        while True:
            self.play_round(player1, player2)
            self.show_scoreboard()

            choice = input("\nDo you want to play again? (y/n): ").lower()
            if choice != "y":
                print("Thanks for playing! Goodbye 👋")
                break


if __name__ == "__main__":
    Game().start()
