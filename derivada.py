# Derivada, primeira aula.
# define funcoes em python e faz o calculo de derivadas
# no ponto.
# Apresenta um primeiro loop usando for

# f1 retorna o quadrado de x
def f1(x):
    #print(x**2)
    return x**2

# calcula a derivada de f no ponto x com intervalo h
# : f'(x) = f(x + h) + f(x)
def derivada(f, h, x):
    return x, f(x), (f(x + h) - f(x))/h

# define valor do ponto p
p = input("por favor digite o valor do ponto x:")

# calcula derivada e imprime valores
print(derivada(f1, 5, p))

# for i in range(0, 10, 1):
#     print(derivada(f1, 5, i))
