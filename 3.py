import numpy as np
import matplotlib.pyplot as plt

# Параметрическое задание сердечка
def heart(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x + 1j * y

# Дискретизация
N = 10  # Количество точек
t_discrete = np.linspace(0, 2 * np.pi, N)
z_discrete = heart(t_discrete)

# Параметрический график (непрерывный)
t_continuous = np.linspace(0, 2 * np.pi, 1000)
z_continuous = heart(t_continuous)

# Визуализация
plt.figure(figsize=(8, 6))
plt.plot(np.real(z_continuous), np.imag(z_continuous), label="Параметрический график (непрерывный)", color="blue", alpha=0.7)
plt.plot(np.real(z_discrete), np.imag(z_discrete), label="Дискретные точки (соединены)", color="red", linestyle="-", marker="o", markersize=4, linewidth=1)
plt.scatter(np.real(z_discrete), np.imag(z_discrete), color="red", s=20)  # Точки для акцента
plt.title("Сердечко на комплексной плоскости")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.axis("equal")
plt.legend()
plt.grid(True)
plt.show()

# Вычисление коэффициентов Фурье
c = np.fft.fft(z_discrete) / N  # Дискретное преобразование Фурье

# Визуализация амплитуд коэффициентов Фурье
plt.figure()
plt.stem(np.arange(-N//2, N//2), np.fft.fftshift(np.abs(c)))
plt.title("Амплитуды коэффициентов Фурье")
plt.xlabel("n")
plt.ylabel("|c_n|")
plt.show()

# Вывод коэффициентов Фурье в текстовом виде
print("Коэффициенты Фурье:")
print("n\tRe(c_n)\t\tIm(c_n)\t\t|c_n|")
for n in range(-N//2, N//2):
    idx = n + N//2  # Индекс для массива коэффициентов
    cn = c[idx]
    print(f"{n}\t{cn.real:.6f}\t{cn.imag:.6f}\t{np.abs(cn):.6f}")