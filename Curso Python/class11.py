squares = [x**3 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
#print("Temperatura en F:", fahrenheit)

#Numeros pares
events = [x for x in range(1,21) if x%2 ==0]
#print(events)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i]for row in matrix] for i in range(len(matrix[0]))]

#print(matrix)
#print(transposed)


transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
        
#print(transposed)


x = 5
if x > 5:
    print("x es mayor que 5")
elif x ==5:
    print("x es igual que 5")
else:
    print("x es menor que 5")
print("afuera")
    
    
    
    
    