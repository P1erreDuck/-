import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("Название", fontsize=24)
ax.set_xlabel("Значение 1", fontsize=14)
ax.set_ylabel("Значение 2", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
plt.show()