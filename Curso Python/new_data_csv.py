import csv

new_product = {
    "name": "Wireles Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargerMaster",
    "category": "Accesories",
    "enty_date": "2024-07-01"
}

with open("product.csv", mode="a", newline="") as file:
    file.write("\n")
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)