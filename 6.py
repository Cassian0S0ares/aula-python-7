cadastro = {}
while True:
    nome = input("Digite um nome para cadastro: ")
    if nome == "":
        break
    if nome == "Neymar":
        print("volta vida 😍")
        continue
    idade = int(input("Digite a sua idade: "))
    cidade = input("Digite cidade: ")
    cadastro[nome] = {"idade" : idade, "cidade" : cidade}
print("Itens cadastrados: ")
for nome, dados in cadastro.items():
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")