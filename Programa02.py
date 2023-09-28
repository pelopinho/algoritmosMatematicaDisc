# PROGRAMA 02 - Criar um código para que o usuário informe dois conjuntos e que seja informado se há relação de contenção e/ou pertinência.

# Nas primeiras linhas, os "sets" possuem a função de receber os conjuntos A e B informados pelo usuário:

A = set(input("Digite os elementos do conjunto A separados por espaços: ").split())
B = set(input("Digite os elementos do conjunto B separados por espaços: ").split())

# A estrutura "if-else" verifica se A está contido em B (se A é subconjunto de B):

if A.issubset(B):
    print("A está contido em B (A é subconjunto de B).")
else:
    print("A não está contido em B (A não é subconjunto de B).")

# Este "if-else" verifica se B está contido em A (B é subconjunto de A)
if B.issubset(A):
    print("B está contido em A (B é subconjunto de A).")
else:
    print("B não está contido em A (B não é subconjunto de A).")

# Este outro "if-else" verifica a pertinência de um elemento x aos conjuntos A e B
x = input("Digite um elemento para verificar sua pertinência a A e B: ")

if x in A:
    print(f"{x} pertence a A.")
else:
    print(f"{x} não pertence a A.")

if x in B:
    print(f"{x} pertence a B.")
else:
    print(f"{x} não pertence a B.")