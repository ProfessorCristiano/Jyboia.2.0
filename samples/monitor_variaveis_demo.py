# =======================================================
# Exemplo 4: Demonstração do Monitor de Variáveis (.jy)
# Observe como a tabela de Variáveis é atualizada!
# =======================================================

contador = 0
soma_acumulada = 0
lista_pares = []

while contador < 10:
    contador = contador + 1
    soma_acumulada = soma_acumulada + contador
    
    if contador % 2 == 0:
        lista_pares.append(contador)

print("Total de repeticoes:", contador)
print("Soma acumulada:", soma_acumulada)
print("Numeros pares encontrados:", lista_pares)
