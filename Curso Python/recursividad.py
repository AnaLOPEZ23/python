def sumatoria(n):
    if n ==0:
        return 0
    
    else:
        return n + sumatoria(n-1)
num=3
print(sumatoria(num))
        