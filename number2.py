#n = int(input())

mini = int(input())
maxi = int(input())

def function_l(n): #количество делителей числа №1
	a = 0
	b = 1

	while n >= b:
		if n % b == 0:
			a += 1
		b += 1
	print(a)
#function_l(n)


def function_ll(n): # делители числа в массиве №2
	a = []
	b = 1

	while n >= b:
		if n % b == 0:
			x = n/b
			a.append(int(x))
		b += 1
	print(a)
#function_ll(n)


def function_lll(n): # проверка чила на простоту №3 
	a = 0
	b = 1

	while n >= b:
		if n % b == 0:
			a += 1
		b += 1
	if a == 2:
		print("число простое")
	elif a != 2:
		print("число не простое")
#function_lll(n)


def function_lv(n): # сумма чётных делителей №4
	a = 0
	b = 1

	while n >= b:
		if n % b == 0:
			x = n/b
			if x % 2 == 0:
				a += x
		b += 1
	print(int(a))
#function_lv(n)


def function_v(n): # количество не чётных делителей №5
	a = 0
	b = 1

	while n >= b:
		if n % b == 0:
			x = n/b
			if x % 2 != 0:
				a += 1
		b += 1
	print(int(a))
#function_v(n)


def function_vll(mini,maxi): # простые числа в диапазоне  №7
	mini = mini
	a = 1
	b = 1
	col = 0

	while mini >= maxi:
		if mini % b == 0:
			print("+")
		mini += 1 
function_vll(mini,maxi)

	#a = 0
	#b = 1

	#while n >= b:
		#if n % b == 0:
		#	a += 1
		#b += 1
	#if a == 2:
	#	print("число простое")
	#elif a != 2:
		#print("число не простое")