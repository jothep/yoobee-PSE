class Color:
    def __init__(self, name):
        self.name = name

    def is_transparent(self):
        return  False
    
    def describe(self):
        return f"{self.name}."

class TransparentColor(Color):
    def is_transparent(self):
        return  True
    
    def describe(self):
        return f"transparent."

class Animal:
    def __init__(self, name, color):
        self.name   = name
        self.color  = color

class Zoo:
    def __init__(self, name, animals=None):
        self.name = name
        self.animals = list(animals) if animals else []       

    def add_animal(self, animal):
        self.animals.append(animal)
        
    def show_animals(self):
        return [
            f"Animal(name='{a.name}', color={a.color.describe()})"
            for a in self.animals
        ]

def main():
    yellow = Color("yellow")
    transparent = TransparentColor("transparent")

    Lion = Animal("Lion", yellow)
    Jellyfish = Animal("Jellyfish", transparent)

    zoo = Zoo("The Zoo", [Lion, Jellyfish])
    print("== Animal list ==")
    for line in zoo.show_animals():
        print(line)

if __name__ == "__main__":
    main()