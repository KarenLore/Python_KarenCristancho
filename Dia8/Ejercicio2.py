# Definición de la lista de frutas
frutas = [('banana', 0.45, 6), ('jackfruit', 4.55, 2), ('kiwi', 0.15, 23)]

#a
resultado_a = [fruta[0].upper() for fruta in frutas]
print(resultado_a)

#b
resultado_b = [fruta[0] for fruta in frutas if fruta[1] < 0.50]
print(resultado_b)

#c
resultado_c = max(frutas, key=lambda x: x[1] * x[2])
print(resultado_c)

#d
resultado_d = sorted(frutas, key=lambda x: x[1] * x[2], reverse=True)
print(resultado_d)
