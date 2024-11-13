class vehicle:
    def __init__(self, model, brand,  price):
        self.model = model
        self.brand = brand
        self.price = price
        self.available = True # Indica si el vehiculo esta disponible para la venta
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehiculo{self.model} ha sido vendido")
        else:
            print(f"El vehiculo{self.model} no esta disponible para la venta")
            
    def return_vehicle(self):
        self.available = True
        print(f"El vehiculo{self.model} ha sido devuelto y esta disponible para la venta")
        
class customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.purchased_vehicles = []
        
    def buy_vehicle(self, vehicle):
        if vehicle.available:
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
            print(f"{self.name} ha comprado el vehiculo{vehicle.model}")
        else:
            print(f"El vehiculo{vehicle.model} no esta disponible para la venta")
            
    def return_vehicle(self, vehicle):
        if vehicle in self.purchased_vehicles:
            vehicle.return_vehicle()
            self.purchased_vehicles.remove(vehicle)
        else:
            print(f"{self.name} no ha comprado el vehiculo{vehicle.model}")
            
class Dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"El vehiculo{vehicle.model}ha sido agregado a la consesionaria")
        
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la consesionaria")
            
    def show_available_vehicles(self):
        print("Vehiculos disponibles:")
        for vehicle in self.vehicles:
            if vehicle.available:
                print(f"{vehicle.model} - ${vehicle.price}")
                
#Ejemplo de uso
vehicle1 = vehicle(" Model S ", "Tesla", 79999)
vehicle2 = vehicle("Mustang", "Ford" , 55999)

#crear cliente
customer1 = customer("Ana Judy", "001")

#Crear concesionaria
dealership = Dealership()
dealership.add_vehicle(vehicle1)
dealership.add_vehicle(vehicle2)
dealership.register_customer(customer1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicles()

#Realizar compra
customer1.buy_vehicle(vehicle1)

#Mostrar vehiculos disponibles despues de la compra
dealership.show_available_vehicles()

#Devolver vehiculo
customer1.return_vehicle(vehicle1)

#Mostrar vehiculos disponibles despues de la devolucion
dealership.show_available_vehicles()
                
