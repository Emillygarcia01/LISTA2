codigo_aluno = int(input("Digite o código do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# determina qual é a maior nota
maior_nota = max(nota1, nota2, nota3)

# calcula a média ponderada
media = (4 * maior_nota + 3 * (nota1 + nota2 + nota3 - maior_nota)) / 6

# exibe as informações
print("Código do aluno:", codigo_aluno)
print("Notas: {}, {}, {}".format(nota1, nota2, nota3))
print("Média: {:.2f}".format(media))

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")