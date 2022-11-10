from matplotlib import pyplot as plt


def gain_solver(frequency):
    if 0.9 <= frequency < 4:
        a = 0.94
        b = -7.6
        c = 20.5
        d = -8.3
    elif 4 <= frequency < 9:
        a = 0.055
        b = -1
        c = 5.8
        d = 1.5
    elif 9 <= frequency <= 12.4:
        a = 0
        b = -0.89
        c = 17.7
        d = -74.4
    else:
        raise 'Frequency error'
    return a * frequency ** 3 + b * frequency ** 2 + c * frequency + d

# Поверенный
f1 = [0.9, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.4]
g1 = [6.1, 4.9, 7.9, 7.8, 9.9, 11, 11, 11.2, 11.6, 11.9, 11.8, 11.8, 12.5, 11.3, 11.6, 11.6, 12.9, 13.3, 13.4, 13.6, 13.8, 13.2, 12, 11.8, 4.8]

# Заявленный
f2 = [0.9, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
g2 = [6, 6.5, 8.3, 8.4, 8.3, 10, 11.1, 12.5, 11.4, 11.1, 11.6, 11.5, 11.7, 11.6, 11.9, 12.5, 13, 12.7, 13, 13.4, 13.2, 13.4, 12.4, 11.1]

# Измеренный
f3 = [8.025, 8.097, 8.128, 8.159, 8.213, 8.226, 8.4]
g3 = [12.3, 12.2, 12.3, 12.3, 12.2, 12.2, 12]

# Аналитический
f4 = [0.9, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.4]
g4 = [gain_solver(frequency) for frequency in f4]


fig, ax = plt.subplots()
ax.plot(f1, g1, linestyle='--', label='Поверенный', linewidth=2)
ax.plot(f2, g2, linestyle=':', label='Заявленный', linewidth=2)
ax.plot(f3, g3, label='Измереный', linewidth=2)
ax.plot(f4, g4, label='Аналитический', linewidth=2)

ax.legend()
ax.set_xlabel('Frequency')
ax.set_ylabel('Gain')
ax.set_title('П6-123')
ax.grid()

plt.show()
