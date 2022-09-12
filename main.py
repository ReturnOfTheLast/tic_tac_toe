field = [i for i in range(1, 10)]
players = ['O', 'X']

def print_field() -> None:
    for i in range(3):
        print_horizontal_line()
        for c in field[i*3:i*3+3]: print(f"| {c} ", end="")
        print("|")
    print_horizontal_line()

def print_horizontal_line() -> None: print("-" * 13)

def ask_for_move(player: int) -> None:
    global field
    while True:
        try: answer = int(input(f"Spiller {players[player]} hvad er dit træk? "))
        except ValueError: print("Input skal være et tal"); continue
        if 9 >= answer >= 1 and isinstance(field[answer-1], int):
            field[answer-1] = players[player]
            break
        else: print("Det er ikke et lovligt træk")

def print_winner(winner: str):
    print_field()
    print(f"Spiller {winner} har vundet")

def check_if_won() -> bool:
    for i in range(3):
        if field[i] == field[i+3] == field[i+6]:
            print_winner(field[i])
            return True
        elif field[i*3] == field[i*3+1] == field[i*3+2]:
            print_winner(field[i*3])
            return True
    if field[0] == field[4] == field[8] or field[2] == field[4] == field[6]:
        print_winner(field[4])
        return True
    return False

def main():
    for i in range(9):
        print_field()
        ask_for_move(i%2)
        if check_if_won(): exit(1)
    print("Uafgjort")

if __name__ == "__main__": main()