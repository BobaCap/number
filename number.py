number = input("введите число: ") #ввод числа
lst = list(number) #переводим в формат list

lst_int = [int(item) for item in lst] # перевод в формат int

amount = len(number)# узнаём количество цифр 

#effect = input("Введите номер действия: ") !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def space (lst): # выведение через пробел №1
	lst.reverse() # реверс 
	for x in lst: # цикл для выведения через пробел 
		print(x, end=' ')
#space(lst)


def column (lst, amount): # выведение в столбик №2
	for x in range(amount): # цикл для выведения через в столбик 
		print(lst[x])
#column(lst, amount)


def addition (lst_int): # умма всех цифр №3
	answer = 0
	for x in lst_int:
		answer += x
	print (answer)
#addition(lst_int)


def multiplication (lst_int): # произведение всех цифр №4
	answer = 1
	for x in lst_int:
		answer *= x
	print (answer)
#multiplication(lst_int)


def Addition_of_even (lst_int): # сумма чётных №5
	answer = 0
	for x in lst_int:
		if x % 2 == 0:
			answer += x
	print (answer)
#Addition_of_even(lst_int)


def Even_rank (number): # сумма цифр в чётных разрядах №6
	n = int(number)
	k = 0 
	z = 0
	while n>0:
		x = n % 10 
		if k % 2 == 0:
			z += x
		n = n // 10 
		k += 1 
	print(z)
#Even_rank(number)


def multiplication_of_odd (lst_int): # произведение нечётных цифр №7 
	answer = 1
	for x in lst_int:
		if x % 2 != 0:
			answer *= x
	print (answer)
#multiplication_of_odd(lst_int)


def Number_of_odd (lst_int): # количество нечётных цифр №8
	answer = 0
	for x in lst_int:
		if x % 2 != 0:
			answer += 1
	print (answer)
#Number_of_odd(lst_int)


def max_min (lst_int, amount): # аксимальнная и минимальная цифра №9
	for run in range(amount-1):
		for x in range(amount-1):
			if lst_int[x] > lst_int[x+1]: # сравнение 
				lst_int[x], lst_int[x+1] = lst_int[x+1], lst_int[x] # перестановка 
	print("минимальная цифра: ", lst_int[0] )# вывод 
	print("максимальная цифра: ", lst_int[-1])
#max_min(lst_int, amount)


def Max_discharge(number): # номер разряда с максимальной цифрой №10
	n = int(number)
	maxi = 0 
	raz_max = 0
	raz = 0
	while n>0:
		x = n % 10 
		if x > maxi:
			maxi = x
			raz_max = raz
		n = n // 10 
		raz += 1
	print(raz_max)
#Max_discharge(number)


def Min_discharge(number): # номер разряда с минимальной цифрой №11
	n = int(number)
	mini = 9 
	raz_min = 0
	raz = 0
	while n>0:
		x = n % 10 
		if x < mini:
			mini = x
			raz_min = raz
		n = n // 10 
		raz += 1
	print(raz_min)
#Min_discharge(number)


def Average (lst_int, amount): #среднее арифметическое №14
	answer = 0
	for x in lst_int:
		answer += x
	z = answer / amount
	print (z)
#Average(lst_int, amount)


# варианты ответов и запуск функций
if effect == "1":
	space(lst)
elif effect == "2":
	column(lst, amount)
elif effect == "3":
	addition(lst_int)
elif effect == "4":
	multiplication(lst_int)
elif effect == "5":
	Addition_of_even(lst_int)
elif effect == "6":
	Even_rank(number)
elif effect == "7":
	multiplication_of_odd(lst_int)
elif effect == "8":
	Number_of_odd(lst_int)
elif effect == "9":
	max_min(lst_int, amount)
elif effect == "10":
	Max_discharge(number)
elif effect == "11":
	Min_discharge(number)
elif effect == "12":
	print("Этого я пока не умею")
elif effect == "13":
	print("Этого я пока не умею")
elif effect == "14":
	Average(lst_int, amount)
else:
	print("Этого я пока не умею")