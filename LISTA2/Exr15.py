# solicita que o usuário insira a idade do nadador
idade = int(input("Insira a idade do nadador: "))

# verifica em qual categoria o nadador se enquadra
if idade >= 5 and idade <= 7:
    categoria = "infantil A"
elif idade >= 8 and idade <= 10:
    categoria = "infantil B"
elif idade >= 11 and idade <= 13:
    categoria = "juvenil A"
elif idade >= 14 and idade <= 17:
    categoria = "juvenil B"
else:
    categoria = "sênior"

# imprime a categoria do nadador
print("O nadador se enquadra na categoria", categoria)