'''15.3. Молекулярное движение: измените программу rw_visual.py и замените plt.scatter()
вызовом plt.plot(). Чтобы смоделировать путь пыльцевого зерна на поверхности водяной капли, передайте значения rw.x_values и rw.y_values и включите аргумент linewidth.
Используйте 5000 точек вместо 50 000.
15.4. Измененные случайные блуждания: в классе RandomWalk значения x_step и y_step генерируются по единому набору условий. Направление выбирается случайно из списка [1,
-1], а расстояние — из списка [0, 1, 2, 3, 4]. Измените значения в этих списках и посмотрите, что произойдет с общей формой диаграммы. Попробуйте применить расширенный
список вариантов расстояния (например, от 0 до 8) или удалите –1 из списка направлений
по оси x или y.
15.5. Рефакторинг: метод fill_walk() получился слишком длинным. Создайте новый метод с именем get_step(), который определяет расстояние и направление для каждого шага,
после чего вычисляет этот шаг. В результате метод fill_walk() должен содержать два вызова get_step():'''

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9))
    point_numbers = range(rw.num_points)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    plt.show()
    keep_running = input("Еще хочешь? (y/n): ")
    if keep_running == 'n':
        break


"""15.5 в random_walk"""