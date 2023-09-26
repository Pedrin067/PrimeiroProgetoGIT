par=0
impar=0
for i in range(1,2001):
    if(i/2==0):
        par=par+1
    else:
        impar=impar+1
print(f'a quantidade de numeros pares é {par}')
print(f'a quantidade de numeros ímpares é {impar}')
