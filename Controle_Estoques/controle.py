class Estoque:
def __init__(self):
self__carros = [] # Inicializa a lista de carros vazia
def adicionar_carro(self, carro):
self.__carros.append(carro)
print(f"Carro {carro.get_marca()} {carro.get_modelo()} adicionado ao
estoque.")