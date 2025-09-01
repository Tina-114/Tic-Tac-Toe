import random
import time
import os

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.human = 'X'
        self.ai = 'O'
        self.current_player = self.human
        self.difficulty = 'hard'
        
    def print_board(self):
        print('\n')
        print('    1   2   3')
        print('  -------------')
        for i in range(3):
            print(f'{i+1} | {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} |')
            print('  -------------')
        print('\n')
    
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def is_winner(self, player):
        for row in self.board:
            if row.count(player) == 3:
                return True
        
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count(player) == 3:
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        
        return False
    
    def get_empty_cells(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    empty_cells.append((i, j))
        return empty_cells
    
    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    
    def undo_move(self, row, col):
        self.board[row][col] = ' '
    
    def minimax(self, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        if self.is_winner(self.ai):
            return 10 - depth
        if self.is_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for row, col in self.get_empty_cells():
                self.board[row][col] = self.ai
                score = self.minimax(depth + 1, False, alpha, beta)
                self.board[row][col] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        
        else:
            best_score = float('inf')
            for row, col in self.get_empty_cells():
                self.board[row][col] = self.human
                score = self.minimax(depth + 1, True, alpha, beta)
                self.board[row][col] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
    
    def get_best_move(self):
        if self.difficulty == 'easy':
            if random.random() < 0.7:
                empty_cells = self.get_empty_cells()
                if empty_cells:
                    return random.choice(empty_cells)
        
        elif self.difficulty == 'medium':
            if random.random() < 0.3:
                empty_cells = self.get_empty_cells()
                if empty_cells:
                    return random.choice(empty_cells)
        
        best_score = float('-inf')
        best_move = None
        
        for row, col in self.get_empty_cells():
            self.board[row][col] = self.ai
            score = self.minimax(0, False)
            self.board[row][col] = ' '
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move
    
    def ai_move(self):
        print("AI is thinking...")
        time.sleep(0.5)
        
        move = self.get_best_move()
        if move:
            row, col = move
            self.make_move(row, col, self.ai)
            return True
        return False
    
    def check_game_over(self):
        if self.is_winner(self.human):
            return "You win!"
        elif self.is_winner(self.ai):
            return "AI wins!"
        elif self.is_board_full():
            return "It's a tie!"
        return None
    
    def set_difficulty(self, difficulty):
        if difficulty.lower() in ['easy', 'medium', 'hard']:
            self.difficulty = difficulty.lower()
            print(f"Difficulty set to {self.difficulty}")
        else:
            print("Invalid difficulty level. Using 'hard' as default.")
            self.difficulty = 'hard'
    
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("You are 'X' and the AI is 'O'")
        
        print("\nSelect difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard (default)")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            self.set_difficulty('easy')
        elif choice == '2':
            self.set_difficulty('medium')
        else:
            self.set_difficulty('hard')
        
        game_over = False
        result = None
        
        while not game_over:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            self.print_board()
            
            if self.current_player == self.human:
                valid_move = False
                while not valid_move:
                    try:
                        print("Your turn (row, col): ")
                        row = int(input("Enter row (1-3): ")) - 1
                        col = int(input("Enter column (1-3): ")) - 1
                        
                        if 0 <= row < 3 and 0 <= col < 3:
                            valid_move = self.make_move(row, col, self.human)
                            if not valid_move:
                                print("That cell is already occupied! Try again.")
                        else:
                            print("Invalid input! Row and column must be between 1 and 3.")
                    except ValueError:
                        print("Please enter numbers only!")
                
                result = self.check_game_over()
                if result:
                    game_over = True
                else:
                    self.current_player = self.ai
            else:
                self.ai_move()
                
                result = self.check_game_over()
                if result:
                    game_over = True
                else:
                    self.current_player = self.human
        
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board()
        print(result)
        
        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            self.__init__()
            self.play_game()
        else:
            print("Thanks for playing!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()