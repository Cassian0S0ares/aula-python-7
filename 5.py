dicionario = {'gato':'chat', "dog" : "chien", "cavalo": "cheval"}
dicionario['ave'] = "galo"
print(dicionario)
print("=" *50)
del dicionario['dog']
print(dicionario)
print("=" *50)
dicionario['cachorro'] = 'pit'
print(dicionario)
print("=" *50)
dicionario.popitem()
print(dicionario)