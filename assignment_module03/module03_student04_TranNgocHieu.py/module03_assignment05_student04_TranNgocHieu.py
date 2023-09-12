def a():
    while True:
        a = input("Please enter a number: ")
        try:
            a = int(a)
            if 0 <= a <= 9: 
                print("Congrats. You escaped.")
                break
            else:
                print("You are on the right track, but not there yet. Try again...")
        except ValueError:
            print("Invalid input type. Input must be an integer. Try again...")

def rock_paper_scissors():
    import sys 
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print("A's turn")
    a = input("Enter your move (Choose one of [rock, paper, scissors]): ")
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    print("B's turn")
    b = input("Enter your move (Choose one of [rock, paper, scissors]): ")
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    plays = ["rock", "paper", "scissors"]
    a_num = plays.index(a)
    b_num = plays.index(b)
    if b_num == (a_num + 1) % 3:
        print(f"Plays: A - {a}, B - {b}\nB wins.")
    elif b_num == a_num:
        print(f"Plays: A - {a}, B - {b}\nDraw.")
    else:
        print(f"Plays: A - {a}, B - {b}\nA wins.")
key = ""
while key != "no":
    rock_paper_scissors()
    key = input("Continue ? (yes/no)\n")
