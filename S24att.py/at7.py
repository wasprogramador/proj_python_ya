#1. Crie um vetor com 5 nomes de colegas da sala. Escreva o vetor na forma de
#tabela.
#2. Troque o nome da segunda posição por outro nome e reescreva o vetor.
vetor = [
    "Gabriel",
    "thomas",
    "Henrrique",
    "Jeferson",
    "David"

]
    
for i in range (4):
    i += 1 
    print(F"posição {i}: {vetor}")
    vetor.remove("thomas")
    vetor.append("lurdes")
    

    
    
    
