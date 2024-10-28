from random import randint

class Die():
    """Игральные кости (кубик)"""
     
    def __init__(self, num_sides = 6):
        '''Используеться кубик с шестью гранями'''
        self.num_sides = num_sides

    def roll(self):
        '''Показывает число выпавшее на кубике'''
        return randint(1, self.num_sides)