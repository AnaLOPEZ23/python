import csv

# Leer un archivo
"""with open("products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)    
    for row in csv_reader:        
        print(row)"""
        
#Mostrar la informacionpor columnas
with open("products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)    
    for row in csv_reader:        
        print(f"El producto:{row["name"]}, precio:{row["price"]}")
