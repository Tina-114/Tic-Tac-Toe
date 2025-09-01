import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()
    
    def test_initial_board(self):
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')
    
    def test_make_move(self):
        self.assertTrue(self.game.make_move(0, 0, 'X'))
        self.assertEqual(self.game.board[0][0], 'X')
        
        self.assertFalse(self.game.make_move(0, 0, 'O'))
        self.assertEqual(self.game.board[0][0], 'X')
    
    def test_is_winner(self):
        self.assertFalse(self.game.is_winner('X'))
        self.assertFalse(self.game.is_winner('O'))
        
        self.game.board[0] = ['X', 'X', 'X']
        self.assertTrue(self.game.is_winner('X'))
        self.assertFalse(self.game.is_winner('O'))
        
        self.game = TicTacToe()
        for i in range(3):
            self.game.board[i][1] = 'O'
        self.assertTrue(self.game.is_winner('O'))
        self.assertFalse(self.game.is_winner('X'))
        
        self.game = TicTacToe()
        for i in range(3):
            self.game.board[i][i] = 'X'
        self.assertTrue(self.game.is_winner('X'))
        
        self.game = TicTacToe()
        for i in range(3):
            self.game.board[i][2-i] = 'O'
        self.assertTrue(self.game.is_winner('O'))
    
    def test_is_board_full(self):
        self.assertFalse(self.game.is_board_full())
        
        for i in range(3):
            for j in range(3):
                self.game.board[i][j] = 'X' if (i+j) % 2 == 0 else 'O'
        
        self.assertTrue(self.game.is_board_full())
    
    def test_get_empty_cells(self):
        empty_cells = self.game.get_empty_cells()
        self.assertEqual(len(empty_cells), 9)
        
        self.game.make_move(0, 0, 'X')
        self.game.make_move(1, 1, 'O')
        
        empty_cells = self.game.get_empty_cells()
        self.assertEqual(len(empty_cells), 7)
        self.assertNotIn((0, 0), empty_cells)
        self.assertNotIn((1, 1), empty_cells)
    
    def test_minimax_ai_win(self):
        self.game.board = [
            ['O', 'X', ' '],
            ['X', 'O', 'X'],
            [' ', ' ', ' ']
        ]
        
        best_move = self.game.get_best_move()
        
        self.assertEqual(best_move, (2, 2))
    
    def test_minimax_block_human(self):
        self.game.board = [
            ['X', 'X', ' '],
            [' ', 'O', ' '],
            ['O', ' ', ' ']
        ]
        
        best_move = self.game.get_best_move()
        
        self.assertEqual(best_move, (0, 2))

if __name__ == '__main__':
    unittest.main()