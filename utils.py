from player import Player

def choose_name() -> str:
    """
    Prompt user to input name
    - prompt will continue until valid name is input
    - valid name must be at least 3 characters long
    """
    while True:
        name = input("Please select player name: ")
        if len(name) < 3:
            print("Name should have at least 3 characters")
            continue
        else:
            print(f"{name} is ready to play")
            return name
        
def log_winner(winner: Player) -> None:
        """
        Logs the winner name.
        """
        print("\n" + "*" * 20)
        print(f"{winner.name} is the WINNER!")
        print("*" * 20)