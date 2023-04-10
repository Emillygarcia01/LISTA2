# Lê os números inteiros A e B 
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Verifica se B é diferente de zero
if b == 0:
    print("Impossível dividir", a, "por zero!")
else:
    # Verifica se A é divisível por B
    if a % b == 0:
        print("A é divisível por B")
    else:
        print("A não é divisível por B")