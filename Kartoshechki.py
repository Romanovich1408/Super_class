class Human:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def get_voice(self):
        pass

    def __str__(self):
        return'age = {}, weight = {}, '.format(self.age, self.weight)

class We(Human):

    def __init__(self, age, weight, name, kartoshechka):
        super().__init__(age, weight)
        self.name = name
        self.kartoshechka = kartoshechka

    def get_voice(self):
        print('Hello')

    def __str__(self):
        return 'We:' + super().__str__() + 'name = {}, kartoshechka = {}'.format(self.name, self.kartoshechka)

kartoshechka_one = We(33, 95, 'Maxim', 'Husband')
kartoshechka_two = We(30, 65, 'Inna', 'Wife')
print(kartoshechka_one)
print(kartoshechka_two)
kartoshechka_two.get_voice()