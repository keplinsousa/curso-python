# Exercicios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variavel 
def multiplica(*args):
    resultado = 0
    for numero in args:
        resultado = numero * numero
    return resultado

conta1 = multiplica(8, 9, 8, 86)
conta2 = multiplica(2, 5)

print(conta1)
print(conta2)


# Crie uma função que fala se um número é par ou impar.
# Retorne se o número é par ou impar

def impar_par(x):
    if x % 2 == 0:
        return f'O número {x} é par.'
    else:
        return f'O número {x} é ímpar.'

print(impar_par(15))