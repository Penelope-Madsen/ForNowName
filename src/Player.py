import random


class Player:
    def __init__(self, crew, fuel, cargo, law, name):
        self.crew = crew
        self.fuel = fuel
        self.cargo = cargo
        self.law = law
        self.name = name


# controls neg space of stats - inverse
crew = 20
fuel = 20
cargo = 20
law = 20
ships = ["Andromeda", "Argo", "Starbuster 5000", "Galaxy Devourer 4000"]
name = ships[random.randint(0, len(ships)-1)]
p1 = Player(crew, fuel, cargo, law, name)
