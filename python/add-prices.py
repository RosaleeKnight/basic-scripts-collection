def add_prices(cart):
	total = 0
	for item in cart:
		total += cart[item]
	return round(total, 2)  

groceries = {"bananas": 1.99, "grapes": 2.99, "orange": 0.99, "energy drink": 3.99, 
	"coffee": 4.99, "oat milk": 4.99, "chips": 2.99, "cookies": 4.50}

print(add_prices(groceries))