"""
Iterando strings com while
"""
#       012345678910
nome = 'keplin sousa'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)