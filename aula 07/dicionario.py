lista = [1,6,3]
tupla = (3,7,8)
dicionario = {
    "Professor":"Gustavo",
    "Diciplina":"Vericionamento",
    "Aluno":"Felipe",
    "Ano":2024
}
    
print(lista[1])
print(tupla[2])
print(dicionario.values())
print(type(dicionario))
for x in dicionario.values():
    print("{:>10}{:>16}".format("valor: ",x))