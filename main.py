import os

board = [i for i in range(1, 10)] # Make a board as a list with the numbers 1-9
players = ['X', 'O'] # Players and their symbol

def print_board() -> None: # Method to print the board
    os.system("cls" if os.name == "nt" else "clear") # Clear the terminal before the board is printed
    for i in range(3): # Repeat three times one for each row
        print_horizontal_line() # Print the line at the top and in between the rows
        for c in board[i*3:i*3+3]: print(f"| {c} ", end="") # Print the value for each of the three columns in the row (with a divider to the left)
        print("|") # Print the final divider (rightmost) at the end of the row
    print_horizontal_line() # Print the bottom line

def print_horizontal_line() -> None: print("-" * 13) # Method to print the horizontal lines

def ask_for_move(player: int) -> None: # Method to get user input
    global board # Make the board list editable in the method
    while True: # Try to get valid input till we succeed
        try: answer = int(input(f"Player {players[player]} what's your move? ")) # Get user input and try to convert it to an integer
        except ValueError: print("Input must be a number"); continue # If the input cannot be converted we show an error and continue at the start of the loop
        if 9 >= answer >= 1 and isinstance(board[answer-1], int): board[answer-1] = players[player]; break # If the user input is 1-9 and the board position haven't been taken yet we change the board position to the players symbol and break the loop
        else: print("Illegal move") # If not, show error and repeat the loop

def print_winner(winner: str) -> None: print_board(); print(f"Player {winner} has won!") # Method to print the winning player

def check_if_won() -> bool: # Method to check if a player has won
    for i in range(3): # Check rows and columns at the same time (three rows and three columns)
        if board[i] == board[i+3] == board[i+6]: # Check if the columns have the same symbol
            print_winner(board[i]) # Print the winning player/symbol
            return True
        elif board[i*3] == board[i*3+1] == board[i*3+2]: # Check if the rows have the same symbol
            print_winner(board[i*3]) # Print the winning player/symbol
            return True
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]: # Check the diagonals
        print_winner(board[4]) # Print the winning player/symbols
        return True
    return False

def main(): # Main method
    for i in range(9): # Play for nine moves (number of total position in the board)
        print_board() # Print the board
        ask_for_move(i%2) # Ask for the players move (alternates as the 'i' goes from 0 to 8 since the modulo 2 will make it swing back and forth between 0 and 1)
        if check_if_won(): exit(0) # Exit the program if a player has won
    print("Game ends in a tie") # If all 9 moves go by and the game haven't been won, it will end in a tie

if __name__ == "__main__": main() # Check that the file is run as the primary program and not imported