def choose_name():
    while True:
        name = input("Please select player name: ")
        if len(name) < 3:
            print("Name should have at least 3 characters")
            continue
        else:
            print(f"{name} is ready to play")
            return name