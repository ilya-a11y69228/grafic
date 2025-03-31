import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графика
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]

# Создаем данные для функции y = (x²/2) - 2
x_func = np.linspace(-2, 5, 100)  # Генерируем 100 точек от -2 до 5
y_func = (x_func**2) / 2 - 2

# Создаем график
plt.plot(x_func, y_func, label='y = (x²/2) - 2', color='orange')  # График функции

# Добавляем заголовок и метки осей
plt.title('Пример графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Отображаем сетку
plt.grid()

# Добавляем линии осей
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')

# Устанавливаем пределы осей
plt.xlim(-1, 6)
plt.ylim(-5, 6)

# Добавляем легенду
plt.legend()

# Показываем график
plt.show()