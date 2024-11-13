import csv

file_path = "product.csv"
updated_file_path = "products_updated.csv"

with open("products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    #obtener los nombrees de las columnas existentes
    fieldnames = csv_reader.fieldnames + ["total_value"]
    
    with open(updated_file_path, mode="w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()#Escribir los encabezados
        
        for row in csv_reader:
            row["total_value"] = float(row["price"]) * int(row["quantity"])
            csv_writer.writerow(row)
        
        