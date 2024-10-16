#Matris de temperatura em cada mês de 3 cidades
matris = [[22,25,28,32],[20,23,26,30],[18,22,25,29]]
for l in range (0,3):
    for c in range (0,3):
        matris[l][c]
print('-=' * 30)
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matris[l][c]}]', end='')
    print()

