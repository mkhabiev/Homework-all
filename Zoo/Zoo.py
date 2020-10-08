class Animals:
    def __init__(self, name, dangerous, prey, cages, area, zookeepers, cost):
        self.name = name
        self.dangerous = dangerous
        self.prey = prey
        self.cages = cages
        self.area = area
        if isinstance(zookeepers, int):
            self.zookeepers = zookeepers
        else:
            raise ValueError("Zookeepers is not integer")
        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError("Cost is not integer")
    def __str__(self):
        return f"{self.name, self.dangerous}" + \
               f"{self.prey, self.cages}" + \
               f"{self.area, self.zookeepers, self.cost}"
    def __add__(self, other):
        return f"${self.cost + other.cost}"


class Zoo:
    def __init__(self, animals, species, cost, food, zookeepers, cages):
        self.animals = animals
        self.species = species
        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError("Cost is not integer")
        self.food = food
        if isinstance(zookeepers, int):
            self.zookeepers = zookeepers
        else:
            raise ValueError("Zookeepers is not integer")
        if isinstance(cages, int):
            self.cages = cages
        else:
            raise ValueError("Cages is not integer")

    def __str__(self):
        return f"{self.species}, {self.animals}, {self.cages}, {self.zookeepers}, " \
               f"{self.cost}, {self.food}"

def Zoo_open():
    return "Zoo is open!"

class Zoo_Time(Zoo):
    def __init__(self, species, animals, cages, zookeepers, cost, food):
        super(Zoo_Time, self).__init__(species, animals, cages, zookeepers, cost, food)
    def __add__(self, other):
        return f"${self.cost + other.cost}"


cat = Animals('Manul', 'Like a cat, but wild', 'rodent', 'medium', 'mountains', 2, 10)
print(cat)

wild_cat = Animals('Snow Bars', 'If this animal is weak', 'Artiodactyls and small animals', 'Very big', 'Mountains',
                   10, 50)
print(wild_cat)

camel = Animals('Vicugna', "It's a domestic animal", 'Grass', 'Open air', 'Mountains', 3, 5)
print(camel)

half_horned = Animals('White tailed wildebeest', "Don't come closer", 'Grass', 'Open air', 'Big', 3, 10)
print(half_horned)

monkey = Animals('Fat Lori', 'Not dangerous', 'Fruits, eggs, flowers, insects', 'Medium', 'With trees', 3, 20)
print(monkey)

snake1 = Animals('Black Mamba', 'Tobi pizda!', 'Rodents, bats, birds', 'Small', 'With a tree', 5, 100)
print(snake1)

snake2 = Animals('Python', "Don't panic!", 'Rodents, reptiles, jackal', 'Medium', 'Open air with grass', 5, 100)
print(snake2)

turtle = Animals('Egyptian turtle', 'Not dangerous', 'Plant foods', 'Small', 'Sun place', 2, 10)
print(turtle)