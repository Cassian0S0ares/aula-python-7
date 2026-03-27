telefone = {
    "chefe" : 3114143435,
    "drake" : 43466636,
    "Só o basico pra elas" : 41432546753,
}
dicionario = {
    'gato':'chat', "dog" : "chien", "cavalo": "cheval"
}
palavras = ['gato', "dog", "cavalo", "lion"]

for palavra in palavras:
    if palavra in dicionario:
        print(palavra, '=>', dicionario[palavra])
    else:
        print(palavra,"não está no dicionario")