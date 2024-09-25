produto = {
    "id":2024001,
    "produto":"Maçã",
    "preço":3.50,
    "validade":"25/09/24"
}
chave = [x for x in produto.keys()]
valor = [x for x in produto.values()]
x = 0
while(x<len(chave)):
    print("{:<10}{:>10}".format(chave[x],valor[x]))
    x += 1 