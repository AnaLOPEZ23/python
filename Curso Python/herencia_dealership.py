class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model 
        self.proce = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo{self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo{self.brand}. No esta disponible")
            
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.get_price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implemetado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

class Car(Vehicle):
    def star_engine(self):
        if not self.is_available:
            return f"El motor del coche{self.brand} esta en marcha"
        else:
            return f"El coche{self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche{self.brand} se ha detenido"
        else:
            return f"El coche{self.brand} No esta disponible"
        
class Bike(Vehicle):
    def star_engine(self):
        if not self.is_available:
            return f"La vicicleta {self.brand} esta en marcha"
        else:
            return f"La vicicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"La vicicleta {self.brand} se ha detenido"
        else:
            return f"La vicicleta {self.brand} No esta disponible"
        
class Truck(Vehicle):
    def star_engine(self):
        if not self.is_available:
            return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} se ha detenido"
        else:
            return f"El camion {self.brand} No esta disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicle =[]
        
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicle.append(vehicle)
        else:
            print(f"Lo siento,{vehicle:brand} no esta disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} esta{availablity} y cuesta {vehicle.get_price()}")
        
class Dealership:
    
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)  
        print(f"El {vehicle.brand} ha sido anadido sl inventario")   
        
    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.nme} ha sido anadido")  
        
        
    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")
                
car1 = Car("Toyota", "Carolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Jose Luis")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibes
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()
      
        
        
        

        
        
    
    

        
    
    
    