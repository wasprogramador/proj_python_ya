#atualizar estoque vendendo 3 produtos 1 e 2 do produto 4;
#adicione 10 unidades ao produto 5;
vetor = ["produto1","produto2","produto3","estoque4","estoque5"]
print("{:<14}{:<14}{:<14}{:<14}{:<10}".format("estoque1","estoque2","estoque3","estoque4","estoque5"))

for x in range(0,len(vetor),1):
    while (x<2):
        print(vetor)
        x=x+1

"estoque4".remove(2)
"estoque5".append(10)
print(vetor)
x=x+1