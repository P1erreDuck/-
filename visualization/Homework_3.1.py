'''15.6. Два кубика D8: создайте модель, которая показывает, что происходит при 1000-кратном бросании двух восьмигранных кубиков. Попробуйте заранее представить, как будет
выглядеть визуализация, перед моделированием; проверьте правильность своих интуитивных представлений. Постепенно наращивайте количество бросков, пока не начнете замечать ограничения, связанные с ресурсами вашей системы.'''
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die(8)
die_2 = Die(8)
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Сумма'}
y_axis_config = {'title': 'Кол-во'}
my_layout = Layout(title='Бросаем 2д8 1к раз',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2d8.html')
