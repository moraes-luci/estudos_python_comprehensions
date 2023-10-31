# Números divisivel por 7 em uma lista de 1 a 1000
divisor_7 = [numero for numero in range(1, 1000) if numero % 7 == 0]
print(divisor_7)

print('\n')
# Números de 1 a 1000 que contém 3
contem_3 = [numero for numero in range(1, 1000) if '3' in str(numero)]
print(contem_3)

print('\n')
# Número de espaços em uma string
var = 'Eu estudo python  '
espaco = [s for s in var if s == ' ']
print(espaco.count(' '))

print('\n')
# Crie uma lista de todas as consoantes na string
frase = 'Iaques amarelos gostam de gritar e bocejar e ontem eles cantavam enquanto comiam inhame nojento'
consoantes = [c for c in frase.upper() if c not in 'a,e,i,o,u," "'.upper()]
print(consoantes)

print('\n')
# Obtenha o índice e o valor como uma tupla para os itens da lista “hi”, 4, 8,99, 'apple', ('t,b','n').
# O resultado seria semelhante a (índice, valor), (índice, valor)
lista = ['hi', 4, 8.99, 'apple', ('t,b', 'n')]
indice_valor = [(t, p) for t, p in enumerate(lista)]
print(indice_valor)

print('\n')
# Encontre os números comuns em duas listas (sem usar tupla ou conjunto)
# list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
item_comum = [i for i in list_a if i in list_b]
print(item_comum)

print('\n')
# Obtenha apenas os números em uma frase como
# 'Em 1984, houve 13 casos de protesto com mais de 1.000 pessoas presentes'
frase_num = 'Em 1984, houve 13 casos de protesto com mais de 1.000 pessoas presentes'
numeros_frase = [n for n in frase_num if n.isnumeric()]
print(numeros_frase)

print('\n')
# Dados números = intervalo (20), produza uma lista contendo a palavra 'par'
# se um número nos números for par, e a palavra 'ímpar' se o número for ímpar.
# O resultado seria parecido com 'ímpar','ímpar', 'par'
intervalo = ['PAR' if i % 2 == 0 else 'IMPAR' for i in range(20)]
print(intervalo)

print('\n')
# Produza uma lista de tuplas consistindo apenas dos números correspondentes
# O resultado seria semelhante a (4 ,4), (12,12)
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_d = [2, 7, 1, 12]
result = [(a, b) for a in list_c for b in list_d if a == b]
print(result)

print('\n')
frutas = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Lista de frutas em maiusculo
frutas_maiusculo = [fruta.upper() for fruta in frutas]
print(frutas_maiusculo)

print('\n')
# Lista de frutas primeira letra de cada palavra maiusculo
frutas_pmaiusculo = [fruta.capitalize() for fruta in frutas]
print(frutas_pmaiusculo)



