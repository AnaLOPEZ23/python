def sum_naturales(n):
    if n==0:
        return 0
    elif n==1:
        
        return 1
    else:
        return n + sum_naturales(n-1)
    print(sum_naturales(n = int(input("ingrese un numero"))))
    