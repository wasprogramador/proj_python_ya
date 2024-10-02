#1. Dado o vetor E = [21, 10, 15, 3, 8], reordene os números de forma
#crescente.
#2. Agora, ordene o vetor E de forma decrescente.
E = [21,10,15,3,8]
print(E)
E_crescente = sorted(E)
E_decrescente = sorted(E,reverse=True)
print(f"vetor ordenado de forma crescente: {E_crescente}")
print(f"vetor ordenado de forma decrescente: {E_decrescente}")
