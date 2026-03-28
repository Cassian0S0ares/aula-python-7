votos = {}
while True:
    candidato = input("Nome do candidato: ")
    if candidato == "":
        break
    if candidato in votos:
        votos[candidato] =+ 1
    else:
        votos[candidato] = 1
print("resultado da votação:")
for candidato, quantiedade in votos.items():
    print(f"{candidato}, - {quantiedade} votos")