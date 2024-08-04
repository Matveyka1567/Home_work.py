import matplotlib.pyplot as plt

fig = plt.figure()

x = [4.0, 4.7, 4.1, 4.4, 5.0, 4.3, 4.6, 4.9, 4.5]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.title('Мой средний бал в школе с 1 по 9 классы')

plt.plot(x, y)

plt.xlabel('Средний балл')
plt.ylim(1, 9)
plt.xlim(4, 5)
plt.ylabel('Классы')

plt.grid()
plt.legend()

plt.show()
