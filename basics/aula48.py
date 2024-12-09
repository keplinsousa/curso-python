""" 
Listas em Python 
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutiliz´zveis - índices e fatiamento
Métodos úteis:
     append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
""" 
#       +01234
#       -54321
string = 'ABCDE' # caracteres (len)
lista = [123, True, 'keplin', 1.2, []]
#print(lista, type(lista))
lista[-3] = 'João'
print(lista)
print(lista[2], type(lista[2]))

#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista[2] = 300

# deletar
del lista[2]
print(lista)
print(lista[2])

# adicionar no final
lista.append(50)
lista.append(60)
lista.append(470)
print(lista)

# deletar o ultimo 
lista.pop()
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)


"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)