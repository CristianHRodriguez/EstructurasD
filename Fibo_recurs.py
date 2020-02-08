def fib(x,y,z):
	if z!=0:
		c = z - 1
		f3 = x + y
		print(f3)	
		return fib(y,f3,c)
m = int(input('Ingrese cuantos numeros desea ver'))

a = 0
b = 1
print(a)
print(b)
cont = m
fib(a,b,cont-2)
