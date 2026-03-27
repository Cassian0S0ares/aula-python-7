dicionario = {'gato':'chat', "dog" : "chien", "cavalo": "cheval"}
dicionario['gato'] = 'gato mia'
print(dicionario)

for chave in sorted(dicionario.keys()):
    print(chave, '->', dicionario[chave])

print("="*50)
for valor in dicionario.values():
    print(valor)