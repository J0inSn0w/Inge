import math
import matplotlib.pyplot as plt

def exponencial(input):
    return math.exp(input/10)
def exponencial_inversa(inicial,input):
    return inicial - math.exp(-input/10)
def cuadratica(valor):
    return (valor*valor)
def division(valor):
    if valor != 0:
        return (1/valor)
    else:
        return 1/0.1
    
valores = [exponencial(valor) for valor in range(50)]

plt.plot(valores)
print (plt.show())

# ax = plt.axes()
# ax.set_facecolor("slategray")
# plt.grid(True)
# plt.plot(valores, color="red", label="Ecuación Exponencial")
# plt.plot(valores2, linestyle="--", label = "Ecuación
# cuadrática")
# plt.xlabel("Muestras")
# plt.ylabel("Valores")
# plt.title("Comparativa entre funciones")
# plt.legend()
# plt.savefig("imagen.png")
# plt.show()