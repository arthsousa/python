dic = {}  # Começamos com um dicionário vazio

while True:
    nome = input("Digite o nome do usuário : ").title()
    idade = int(input(f"Digite a idade de {nome}: "))
    nota = []
    for i in range(4):
        num = float(input(f"Digite a sua nota no {i+1} bim:  "))
        nota.append(num)

    somas = sum(nota)
    media_notas = somas / 4

    dic[nome] = {
        "idade": idade,
        "nota": nota,
        "media_notas": media_notas
    }
    dnv = input("Quer adicionar mais um aluno S/N: ").title()
    if dnv == "S":
        continue
    else:
        break

print(dic)
maior_media = 0

for nome_aluno, dados_aluno in dic.items():
    if dados_aluno["media_notas"] > maior_media:
        maior_media = dados_aluno["media_notas"]
        aluno_maior_media = nome_aluno

print(f"\n--- Aluno com a Maior Média ---")
print(f"O aluno com a maior média é: {aluno_maior_media}")
print(f"Com média: {maior_media:.2f}")  # Formata para 2 casas decimais

for nome_aluno, dados_aluno in dic.items():
    if dados_aluno["media_notas"] > 7:
        print(f"{nome_aluno} foi aprovado")
        print()
for nome_aluno, dados_aluno in dic.items():
    if dados_aluno["media_notas"] <= 7:
        print(f"{nome_aluno} foi Reprovado")
        print()
