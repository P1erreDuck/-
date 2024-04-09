'''15.1. Кубы: число, возведенное в третью степень, называется «кубом». Нанесите на диаграмму первые пять кубов, а затем первые 5000 кубов.
15.2. Цветные кубы: примените цветовую карту к диаграмме с кубами'''
import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, s=100)
plt.show()