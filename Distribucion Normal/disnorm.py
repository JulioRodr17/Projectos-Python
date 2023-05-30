import math
from scipy import integrate

# sigma es igual a x
# mi es igual a m
def integral(y,x,m):
    return (1 / (x * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((y - m) / x) ** 2)

def calcula_integral(a,b,x,m):
    resultado = integrate.quad(integral, a, b, args=(x, m))[0]
    return resultado

# Solicitar valores al usuario
a = float(input("Ingrese el valor de 'a': "))
b = float(input("Ingrese el valor de 'b': "))
x = float(input("Ingrese el valor de 'sigma': "))
m = float(input("Ingrese el valor de 'miu': "))

# Calcular la integral definida
if x>0:
    integral = calcula_integral(a, b, x, m)
else:
    print("El valor de sigma debe ser positivo")
    integral = 0
print(f"El valor de la integral definida de {int(a)} a {int(b)} es: {integral}")



