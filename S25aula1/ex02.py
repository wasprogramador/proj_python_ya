#Faça a reserva dos assentos (1,3), (2,5) e (4,7).
reservas = ["reserva1","reserva2","reserva3"]
print("{:<14}{:<14}{:<14}".format("reserva1","reserva2","reserva3"))
assentos = [1.3,2.5,4.7]
print("{:<14}{:<14}{:<14}".format(1.3,2.5,4.7))

#Cancele a reserva do assento (2,5).

reservas.remove("reserva2")
assentos.remove(2.5)

#Exiba o mapa de assentos atualizado.
print(reservas)
print(assentos)

