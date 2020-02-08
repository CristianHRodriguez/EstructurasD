def fib(y):
x = int(input('Ingrese cuantos numeros desea ver'))
    
    if y<2:
        return y
    return fib(y-1)+fib(y-2)
for i in range(x):
    print(fib(i))
