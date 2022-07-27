from ast import match_case

match_case

def bebida_suco (caracteristicas):
	match caracteristicas:
		case 1:
			return "Suco"
		case 2:
			return "Sabor: Uva"
		case 3:
			return "Sabor: Laranja"
		case 4:
			return "Material do copo: plástico"
		case 5:
			return "Tamanho: 300ml"
		case 6:
			return "Tamanho: 500ml"
		case _:
			return "Bebida {} indisponível".format(caracteristicas)

print(bebida_suco(1))
print(bebida_suco(2))
print(bebida_suco(4))
print(bebida_suco(6))

gelo = True
delivery = True

if gelo == True:
	print ("Com gelo: colocar 6 pedras de gelo")
else:
	print ("Sem gelo")

if delivery == True:
	print ("Copo sem furo")
	print ("Delivery")
else:
	print ("Copo com furo")
	print ("Consumir no local")