'''15.7. Три кубика: при броске трех кубиков D6 наименьший возможный результат равен
3, а наибольший — 18. Создайте визуализацию, которая показывает, что происходит при
броске трех кубиков D6.'''
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Сумма'}
y_axis_config = {'title': 'Кол-во'}
my_layout = Layout(title='Бросаем 3д6 1к раз',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')