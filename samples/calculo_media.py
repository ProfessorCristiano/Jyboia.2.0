# ==========================================
# Exemplo 2: Cálculo de Média Escolar (.jy)
# ==========================================

aluno = "Maria Silva"
nota1 = 8.5
nota2 = 7.0
nota3 = 9.0

media = (nota1 + nota2 + nota3) / 3

print("Aluno:", aluno)
print("Média final:", media)

if media >= 7.0:
    situacao = "Aprovado(a)!"
elif media >= 5.0:
    situacao = "Em Recuperacao!"
else:
    situacao = "Reprovado(a)!"

print("Situação:", situacao)
