class Tomato:
    states = {1: 'всход', 2: 'лист', 3: 'корень',
              4: 'бутон', 5: 'цветение', 6: 'плод'}
    n = 1  # начальное значение ключа словаря

    def __init__(self, index):  # иницилизируем объекты класса  Tomato

        self._index = index
        self._state = self.states[self.n]  # значение словаря соответствующее ключу стадии созревания 1

    def grow(self):
        self.n += 1  # переход на следующую стадию созревания
        self._state = self.states[self.n]  # значение словаря соответствующее ключу стадии созревания n

    def is_ripe(self):
        if self._state == self.states[6]:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, count_):
        self.tomatoes = []
        self.count_ = count_
        for tom in range(self.count_ + 1):  # для формирования списка из количества переданных томатов
            self.tomatoes.append(Tomato(tom))  # формируем список из объектов класса Tomato

    def grow_all(self):  # перевод всех томатов в списке на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        are_ripe = []
        for tomato in self.tomatoes:
            are_ripe.append(tomato.is_ripe())  # определяем стадию созревания для всех томатов
        for ripe in are_ripe:
            if ripe == True:
                return True
            else:
                return False

    def give_away_all(self):
        self.tomatoes.clear()  # очистка списка после сбора урожая


class Gardener:
    def __init__(self, name, plant):  # инициализация объектов класса
        self.name = name
        self._plant = plant  # принимает объект класса TomatoBush

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Можно собирать урожай")
        else:
            print("Предупреждение, плоды в стадии созревания")

    @staticmethod
    def knowledge_base():
        print(" не переселяйте горшки семенами;\n позаботьтесь о достаточном количестве "
              "света;\n заройте стебли саженцев поглубже;\n поливайте регулярно.")


Gardener.knowledge_base()
tom = TomatoBush(3)
gard = Gardener("Sasha", tom)
gard.work()
gard.work()
gard.work()
gard.work()
gard.work()
gard.harvest()


