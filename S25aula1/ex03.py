#Calcular o total de vendas no ano.
#Calcular a média mensal de vendas.
#Determinar o mês com a máxima venda.

def somar(Vendas_mensais):
    soma = 0
    for i in Vendas_mensais:
        soma = soma + i
    return soma
Vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]
soma = somar(Vendas_mensais)
print(Vendas_mensais)
print("Soma das Vendas mensais = {0:.2f}".format(soma)) 

def metade(Vendas_mensais):
    media = 0
    for i in Vendas_mensais:
        media = media + i/2
    return media
Vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]
media = metade(Vendas_mensais)
print(Vendas_mensais)
print("Média das vendas mensais = {0:.2f}".format(media)) 

def max_Vendas_mensais(Vendas_mensais):
    maior = Vendas_mensais[0]
    for xi in Vendas_mensais:
        if(xi > maior):
            maior = xi
    return maior

Vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]
maxl = max_Vendas_mensais(Vendas_mensais)
print("O valor máximo é {0:.2f}".format(maxl))