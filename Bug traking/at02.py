#analisa dados de vendas
def vendas(mensal,valor):
    valor = [600,400,100,300,700,450,850,950,1200,4000,2330,7000]
    for x,valor in range(0,len(valor),1):
        if mensal.lower() == x:
            return mensal
        print(valor)
    mensal = input("Digite um mês")
    valor = input("Digite o valor")

vendas(1,1)