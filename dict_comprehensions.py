lista = ['maçã', 'banana', 'abacaxi', 'goiaba']

# Solução com For
frutas = {}

for item in range(len(lista)):
    frutas[f'fruta{item}'] = lista[item]
print(frutas)

# Solução em dict comprehensions
frutas2 = {f'fruta{item}': lista[item] for item in range(len(lista))}
print(frutas2)

