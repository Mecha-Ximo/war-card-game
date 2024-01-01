class Card():
    def __init__(self, name: str, value: int, suit: str):
        self.name = name
        self.value = value
        self.family = suit
        self.title = f"{self.name} of {self.family}"
    
    def __str__(self) -> str:
        return self.title