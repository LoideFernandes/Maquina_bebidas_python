from ast import match_case
match_case

def bebida_refrigerante (caracteristicas):
	match caracteristicas:
		case 1:
			return "Refrigerante"
		case 2:
			return "Sabor: Coca-cola"
		case 3:
			return "Sabor: Guaraná"
		case 4:
			return "Material do copo: papel"
		case 5:
			return "Tamanho: 300ml"
		case 6:
			return "Tamanho: 500ml"
		case 7:
			return "Tamanho: 700ml"
		case _:
			return "Bebida {} indisponível".format(caracteristicas)

print(bebida_refrigerante(30))
print(bebida_refrigerante(1))
print(bebida_refrigerante(2))
print(bebida_refrigerante(3))

gelo = True
delivery = True

if gelo == True:
	print ("Com gelo: colocar 12 pedras de gelo")
else:
	print ("Sem gelo")

if delivery == True:
	print ("Copo sem furo")
	print ("Delivery")
else:
	print ("Copo com furo")
	print ("Consumir no local")
