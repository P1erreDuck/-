'''15.10. Эксперименты с библиотеками: попробуйте использовать Matplotlib для создания
визуализации бросков кубиков, а Plotly — для создания визуализации случайного блуждания. (Для выполнения этого упражнения вам придется обратиться к документациям обеих
библиотек.)'''

import matplotlib.pyplot as plt
from die import Die
from random import randint


def roll_dice(num_dice=1, num_sides=6):
    return sum(randint(1, num_sides) for _ in range(num_dice))


while True:
    die_1 = Die(6)
    die_2 = Die(6)
    results = [die_1.roll() + die_2.roll() for _ in range(1000)]
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.hist(results, bins=range(2, die_1.num_sides + die_2.num_sides + 2), align='left')
    plt.show()
    keep_running = input("Вырубай на n: ")
    if keep_running == 'n':
        break