#1. Dado o vetor D = [12, 18, 5, 24, 7], encontre a posição do número 24.
#2. Qual o valor mais próximo de 10 no vetor D?
d = [12,18,5,24,7]
posicao3 = d.index(3)
valor_prox_10 = min(d, keys=lambda x : abs(x-10))
print(f"A posição de 24 é: {posicao3}")
print(f"O valor mais próximo de 10 é: {valor_prox_10}")