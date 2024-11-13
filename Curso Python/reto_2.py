def sumatoria(ini, n):
     if n == ini:
         return n
     else:
         return n + sumatoria(ini, n-1)