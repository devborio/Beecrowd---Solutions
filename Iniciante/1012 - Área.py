a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

trianguloArea = (a * c) / 2
circuloArea = 3.14159 * (c**2)
trapezioArea = ((a + b) * c)/2
quadradoArea = b**2
retanguloArea = a * b

print("TRIANGULO: %.3f" %trianguloArea)
print("CIRCULO: %.3f" %circuloArea)
print("TRAPEZIO: %.3f" %trapezioArea)
print("QUADRADO: %.3f" %quadradoArea)
print("RETANGULO: %.3f" %retanguloArea)
