products = []
while True: # for偏向已知的次數，while為未知會使用幾次
	name = input('請輸入商品品項：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
#	p = []
#	p.append(name)
#	p.append(price)
#	products.append(p)

#	p = [name, price] 
#	products.append(p) # 可取代7-10行

	products.append([name, price]) # 可取代12-13行

print(products)