from matplotlib import pyplot as plt
import numpy as np
# plt.plot([1,5,6,10], [1,4,10, 0])
# plt.show()

# eixox = np.array([1,5, 8])
# eixoy = np.array([3,100, 10])
# plt.plot(eixox, eixoy)
# plt.show()
#
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# plt.subplot


# x = np.array(["A","B", "C", "D"])
# y = np.array([3,8,1,10])
# plt.bar(x,y)
# plt.show()


# x = np.array(["A","B", "C", "D"])
# y = np.array([3,8,1,10])
# plt.scatter(x,y)
# plt.show()


# x = np.random.normal(110, 10, 255)
# plt.hist(x)
# plt.show()


# y = [10, 10]
# label = ["Amarelo", "Azul"]
# explode = [0.4, 0]
# plt.pie(y, labels=label, explode=explode, shadow=True)
# plt.show()


# x = np.array(["A","B", "C", "D"])
# y = np.array([0,8,1,10])
# plt.plot(x, y)
# plt.xlabel("EIXO X")
# plt.ylabel("EIXO Y")
# plt.title("TITULO")
# plt.show()



# x = np.array(["A","B", "C", "D"])
# y = np.array([0,8,1,10])
# plt.subplot(1,2,1)
# plt.plot(x, y)
# plt.subplot(1,2,2)
# plt.pie(y, labels=x)
# plt.xlabel("EIXO X")
# plt.ylabel("EIXO Y")
# plt.suptitle("TITULO")
# plt.show()


# x = np.array(["A","B", "C", "D"])
# y = np.array([0,8,1,10])
# y2 = np.array([0,2,3,10])
# plt.plot(y)
# plt.plot(y2)
#
# plt.xlabel("EIXO X")
# plt.ylabel("EIXO Y")
# plt.title("TITULO")
# plt.legend(["Laranja", "Azul"], loc="lower right" )
# plt.show()


# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# plt.figure(figsize=)
# plt.subplot(1,2,2)


# x = np.array(["A","B", "C", "D"])
# y = np.array([0,8,1,10])
# plt.subplot(1,2,1)
# plt.plot(x, y)
# plt.subplot(1,2,2)
# plt.plot(x, y)
# plt.xlabel("EIXO X", size=15, color="blue")
# plt.ylabel("EIXO Y")
# plt.suptitle("TITULO")
# plt.grid(color='green', linestyle='solid', linewidth=0.5, axis='x')
# plt.show()
# plt.box(False)
# plt.box(False)



#PROVA
# y = np.array([5, 20, 10])
# x = np.array(["Aprendizado Mínimo", "Aprendizado Médio", "Aprendizado Completo"])
# plt.bar(x,y, color="gray")
# plt.title("Educação para menores", size=15, color='r')
# plt.ylabel("Alunos", color='g')
# plt.xlabel("Aprendizado", color='g')
# plt.grid()
# plt.show()


# y1 = np.array([10000, 20000, 30000, 2000, 12000])
# y2 = np.array([20000, 10000, 40000, 5, 8.5])
# x = np.array(["Janeiro", "Fevereiro", "Março", "Abril", "Maio"])
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.title("Gráfico de Lucro por Mês das empresas jonas e Reiter", color='r')
# plt.ylabel("Lucro", color='r')
# plt.xlabel("Meses", color='r')
# plt.grid(axis='y')
# plt.legend(["Empresa jonas", "Empresa Reiter"], loc='upper right')
# plt.show()


# labels = np.array(["Pão", "Bebidas", "Balas e doces", "Salgados", "Bolos e cucas", "Café"])
# explode = np.array([0.2, 0, 0, 0, 0, 0])
# val = np.array([30, 20, 10, 20, 15, 5])
# plt.pie(val, labels=labels, shadow=True, explode=explode)
# plt.title("Padaria do Seu jonas", color='r')
# plt.show()