#projeto que separa funcionários para cada área
matriz = [[1,5,9],[1,7,10],[3,3,10]]
print("nível de cada funcionário em 3 áreas")
print(' fun1   fun2   fun3')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    

