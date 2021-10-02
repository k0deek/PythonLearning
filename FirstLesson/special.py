class Cat:
    name = ''
    color = ''
    weight = 0

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self, n):
        print("meow\n"*n)


cat = Cat('Mihail', 'black', 18)
cat.meow(10)