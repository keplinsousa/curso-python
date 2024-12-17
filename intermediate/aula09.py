"""
Exercicios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parametro
"""
'''
def duplica(numero):
    return 2 * numero

def triplica(numero):
    return 3 * numero

def quadruplica(numero):
    return 4 * numero

print(duplica(5))
print(triplica(5))
print(quadruplica(5))
'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
print(duplicar(2))