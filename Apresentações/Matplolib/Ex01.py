import numpy as np
from matplotlib import pyplot as plt
# x = np.array(["Janeiro", "Fevereiro", "Março", "Abril"])
# y = np.array([10, 20, 30, 40])
# plt.plot(x,y)
# plt.title("Lucros por mês", color="g")
# plt.xlabel("Meses", color="red")
# plt.ylabel("Lucros", color="red")
# plt.show()


# labels = np.array(["TI","Administração", "Engenharia civil", "Inglês"])
# y = np.array([50, 30, 10, 10])
# plt.pie(y, labels=labels)
# plt.show()


# x = np.array(["Janeiro", "Fevereiro", "Março"])
# y = np.array([3, 8, 1])
# plt.bar(x,y, color='r')
# plt.title("JonasExProfessor", color="blue")
# plt.xlabel("Meses", color="yellow")
# plt.ylabel("Pessoas", color="yellow")
# plt.show()


# x = np.array(["Janeiro", "Fevereiro", "Março"])
# y = np.array([3, 8, 1])
# plt.grid(linestyle='--')
# plt.barh(x,y, color='r')
# plt.title("JonasExProfessor", color="blue")
# plt.xlabel("Meses", color="yellow")
# plt.ylabel("Pessoas", color="yellow")
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# fig, ax = plt.subplots(figsize=(5, 3))
# ax.set(xlim=(-3, 3), ylim=(-1, 1))
# x = np.linspace(-3, 3, 91)
# t = np.linspace(1, 25, 30)
# X2, T2 = np.meshgrid(x, t)
# sinT2 = np.sin(2*np.pi*T2/T2.max())
# F = 0.9*sinT2*np.sinc(X2*(1 + sinT2))
# line = ax.plot(x, F[0, :], color='k', lw=2)[0]
#
# def animate(i):
#     line.set_ydata(F[i, :])
# anim = FuncAnimation(
# fig, animate, interval=100, frames=len(t)-1)
# plt.draw()
# plt.show()