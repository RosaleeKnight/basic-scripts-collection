class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = 'brown'
table.material = 'wood'

couch = Furniture()
couch.color = 'black'
couch.material = 'leather'

chair = Furniture()
chair.color = 'grey'
chair.material = 'metal'

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
print(describe_furniture(couch)) 
print(describe_furniture(chair))