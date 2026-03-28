import webbrowser
agenda = {}
while True:
    nome = input("Digite um nome para cadastrar: ")
    if nome == "":
        break
    telefone = input("Digite o seu telefone bb: ")
    agenda[nome] = telefone

while True:
    pesquisa = input("Pesquisa: ")
    if pesquisa == "":
        break
    if pesquisa in agenda:
        print(f"telefone do {pesquisa} é {agenda[pesquisa]}")
    else:
        print("Quem é esse?")
        webbrowser.open_new_tab("https://media.tenor.com/JWzIaFEJs2gAAAAe/who-is-he.png")