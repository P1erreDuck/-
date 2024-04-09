'''15.9. Генераторы: для наглядности в списках этого раздела используется длинная форма
цикла for. Если вы уверенно работаете с генераторами списков, попробуйте написать генератор для одного или обоих циклов в каждой из этих программ.'''
from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline



class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)



def generate_results(die1, die2, num_rolls):
    results = [die1.roll() + die2.roll() for _ in range(num_rolls)]
    frequencies = [results.count(value) for value in range(2, die1.num_sides + die2.num_sides + 1)]
    return frequencies


def generate_plot(die1, die2, num_rolls):
    frequencies = generate_results(die1, die2, num_rolls)

    x_values = list(range(2, die1.num_sides + die2.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Сумма'}
    y_axis_config = {'title': 'Количество'}
    my_layout = Layout(title=f'Бросаем d{die1.num_sides} и d{die2.num_sides} {num_rolls} раз', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename=f'2d{die1.num_sides}.html')


die_1 = Die(6)
die_2 = Die(8)
generate_plot(die_1, die_2, 1000)