import Tanque
import time
import matplotlib.pyplot as plt

V1 = Tanque.Valvula("Entrada", 15.0) #1
V2 = Tanque.Valvula("Entrada", 25.0) #2
V3 = Tanque.Valvula("Salida", 50.0)  #3

valvulas = [V1,V2,V3]
#tiempo = 0.001
litros = []

TQ1 = Tanque.TanqueConValvulas(2.0,3.0,100.0,valvulas)

TQ1.abrir_valvula(1)
while TQ1.litrosActual < 200:
    TQ1.update()
    litros.append(TQ1.litrosActual)

TQ1.cerrar_valvula(1)

TQ1.abrir_valvula(2)

while TQ1.litrosActual < 350:
    TQ1.update()
    litros.append(TQ1.litrosActual)

TQ1.cerrar_valvula(2)

TQ1.abrir_valvula(3)

while TQ1.litrosActual > 0:
    TQ1.update()
    litros.append(TQ1.litrosActual)

TQ1.cerrar_valvula(3)



plt.plot(litros)
plt.show()