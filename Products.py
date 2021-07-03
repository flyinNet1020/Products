import os
# function呼叫需要參數、回傳值
# function儘量只做一件事

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f: # 寫入/讀取檔案都會有編碼的問題，要特別注意
		for line in f:
			if '商品,價格' in line:
				continue # 不處理後面再繼續一次迴圈;break會直接跳出當下迴圈
			name, price = line.strip().split(',') # 把換行符號(\n)去除後，遇到逗點就分割，而split處理後，資料會變成清單
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
	while True: # for偏向已知的次數，while為未知會使用幾次
		name = input('請輸入商品品項：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open('filename', 'w', encoding = 'utf-8') as f: # with的做用是讓程式離開with後，檔案自動關閉。
		f.write('商品,價格\n') # 若不加入26行的encoding = 'utf-8'編碼會出問題
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # 4個字串的相加。避免在同一儲存格，故用逗點做區隔。

def main(): # main function 為程式進入點
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案是否存在，檔案在才繼續讀取
		print('此檔案存在...')
		products = read_file(filename)
	else:
		print('檔案不存在...')

	products = user_input(products) # 把上一個函式導入，並回傳存回products
	print_products(products)
	write_file('product.csv', products)

main()