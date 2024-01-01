class Card():
    def __init__(self, name, value, family):
        self.name = name
        self.value = value
        self.family = family
        self.title = f"{self.name} of {self.family}"
    
    def __str__(self):
        return self.title