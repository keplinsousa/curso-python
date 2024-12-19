# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a

print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa.values()
# print(a, b)

# args e kwargs 
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa, dados_pessoa)
print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

mostro_argumentos_nomeados(nome='Joana', qlq=123)