import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Game state
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.game_over = False
        
        # Create buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    root, 
                    text=" ", 
                    font=('Arial Black', 10), 
                    width=20, 
                    height=10,
                    bg="lightblue",
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)
        
        # Reset button
        reset_button = tk.Button(
            root, 
            text="Reset Game", 
            font=('Arial', 14), 
            command=self.reset_game
        )
        reset_button.grid(row=3, column=0, columnspan=3, sticky="we")
    
    def on_click(self, row, col):
        index = row * 3 + col
        
        if self.board[index] == " " and not self.game_over:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.game_over = False
        
        for button in self.buttons:
            button.config(text=" ")

# Create and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()