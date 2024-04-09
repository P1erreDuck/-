'''15.9. Генераторы: для наглядности в списках этого раздела используется длинная форма
цикла for. Если вы уверенно работаете с генераторами списков, попробуйте написать генератор для одного или обоих циклов в каждой из этих программ.'''
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Произведение'}
y_axis_config = {'title': 'Кол-во'}
my_layout = Layout(title='Бросаем 2d6 100к раз и переумножаем',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6xd6.html')