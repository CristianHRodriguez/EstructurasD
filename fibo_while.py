x = int(input('ingrese el numero de datos a visualizar'))
a = 0
b = 1
print (a)
print (b)

temp = 0
i = 1

while i < (x-1):
	temp = a + b
	a = b
	b = temp
	print (temp)
	i = i + 1
