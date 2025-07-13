# restaurant case revisted
from queue import Queue
from collections import namedtuple
import json
cola_ordenes_fifo = Queue(maxsize = 7) #el restaurante puede manejar hasta 7 órdenes a la vez
orden_json = "ordenes.json"
class MenuItem:
    def __init__(self, name:str, price:float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate(self):
        total_price = self.price*self.quantity
        return total_price
            
class Rice(MenuItem): #ya sets y gets
   def __init__(self, name, price, quantity, meat: bool, vegetables: bool, 
                 seafood: bool ):
         super().__init__(name, price, quantity)
         self.__meat = meat
         self.__vegetables = vegetables
         self.__seafood = seafood
         if self.__meat == True :
            self.price += 2
         if self.__seafood == True :
            self.price += 3
         if self.__vegetables == True:
            self.price += 2
   def get_meat(self):
      if self.__meat == True :
         self.price += 2
      return self.__meat
   def set_meat(self, new_meat: bool):
         self.__meat = new_meat
         if self.__meat == True :
            self.price += 2
         else:
            self.price -= 2
   def get_vegetables(self):
         return self.__vegetables
   def set_vegetables(self, new_vegetables: bool):
         self.__vegetables = new_vegetables
         if self.__vegetables == True :
            self.price += 2
         else:
            self.price -= 2
   def get_seafood(self):
      return self.__seafood
   def set_seafood(self, new_seafood: bool):
         self.__seafood = new_seafood
         if self.__seafood == True :
               self.price += 3
         else:
            self.price -= 3

class Soup(MenuItem): #geteado y seteado
   def __init__(self, name, price, quantity, meat: bool, changua:bool, 
                 seafood: bool):
        super().__init__(name, price, quantity)
        self.__meat = meat
        self.__seafood = seafood
        self.__changua = changua
        if self.__changua == True:
            self.price -= 1
        if self.__meat == True :
            self.price += 2
        if self.__seafood == True :
            self.price += 3
   def get_meat(self):
      if self.__meat == True :
         self.price += 2
      return self.__meat
   def set_meat(self, new_meat: bool):
         self.__meat = new_meat
         if self.__meat == True :
            self.price += 2
         else:
            self.price -= 2
   def get_changua(self):
      return self.__changua
   def set_changua(self, new_changua: bool):
         self.__changua = new_changua
         if self.__changua == True :
            self.price -= 1
         else:
            self.price += 1
   def get_seafood(self):
      return self.__seafood
   def set_seafood(self, new_seafood: bool):
         self.__seafood = new_seafood
         if self.__seafood == True :
               self.price += 3
         else:
            self.price -= 3
            
class Salad(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, meat:bool, seafood:bool, 
                 fruit : bool):
        super().__init__(name,price,quantity)
        self.__meat = meat
        self.__seafood = seafood
        self.__fruit = fruit
        if self.__meat == True :
            self.price += 2
        if self.__seafood == True :
            self.price += 3
        if self.__fruit == True:
            self.price += 1
   def get_meat(self):
      if self.__meat == True :
         self.price += 2
      return self.__meat
   def set_meat(self, new_meat: bool):
         self.__meat = new_meat
         if self.__meat == True :
            self.price += 2
         else:
            self.price -= 2
   def get_fruit(self):
      return self.__fruit
   def set_fruit(self, new_fruit: bool):
         self.__fruit = new_fruit
         if self.__fruit == True :
            self.price += 1
         else:
            self.price -= 1
   def get_seafood(self):
      return self.__seafood
   def set_seafood(self, new_seafood: bool):
         self.__seafood = new_seafood
         if self.__seafood == True :
               self.price += 3
         else:
            self.price -= 3   
            
class Dessert(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, ice_cream: bool, special: bool, 
                 extra_candys: bool):
        super().__init__(name, price, quantity)
        self.__ice_cream = ice_cream
        self.__special = special
        self. __extra_candys = extra_candys
        if self.__ice_cream == True :
            self.price += 1
        if self.__special == True :
            self.price += 2
        if self.__extra_candys == True:
            self.price += 2
   def get_ice_cream(self):
        return self.__ice_cream
   def set_ice_cream(self, new_ice_cream: bool):
         self.__ice_cream = new_ice_cream
         if self.__ice_cream == True :
            self.price += 1
         else:
            self.price -= 1
   def get_special(self):
        return self.__special
   def set_special(self, new_special: bool):
         self.__special = new_special
         if self.__special == True :
            self.price += 2
         else:
            self.price -= 2
   def get_extra_candys(self):
        return self.__extra_candys
   def set_extra_candys(self, new_extra_candys: bool):
         self.__extra_candys = new_extra_candys
         if self.__extra_candys == True :
            self.price += 2
         else:
            self.price -= 2
     
class Drink(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, suggar: bool, milk :bool, 
                buffet: bool ):
        super().__init__(name, price, quantity)
        self.__suggar = suggar
        self.__milk = milk
        self.__buffet = buffet
        if self.__milk == True :
            self.price += 1
        if self.__buffet == True:
            self.price += 3
   def get_suggar(self):
      return self.__suggar
   def set_suggar(self, new_suggar: bool):
         self.__suggar = new_suggar
         if self.__suggar == True :
            self.price += 1
         else:
            self.price -= 1  
   def get_milk(self):
      return self.__milk
   def set_milk(self, new_milk: bool):
         self.__milk = new_milk
         if self.__milk == True :
            self.price += 1
         else:
            self.price -= 1
   def get_buffet(self):
      return self.__buffet
   def set_buffet(self, new_buffet: bool):
      if self.__buffet == True :
         self.price += 3
      else:
         self.price -= 3
   
class AlcoholicDrink(Drink): #seteado y geteado
   def __init__(self, name, price, quantity, suggar, milk, bottle : bool):
        super().__init__(name, price, quantity, suggar, milk, buffet = False)
        self.__bottle = bottle
        if self.__bottle == True:
            self.price = self.price*4
   def get_bottle(self):
      return self.__bottle
   def set_bottle(self, new_bottle: bool):
         self.__bottle = new_bottle
         if self.__bottle == True :
            self.price = self.price*4
         else:
            self.price = self.price/4
            
class Snacks(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, doritos: bool, chips: bool, 
                 spicy: bool):
         super().__init__(name, price, quantity)
         self.__doritos = doritos
         self.__chips = chips
         self.__spicy = spicy
         if self.__doritos == True :
            self.price += 2
         if self.__spicy == True:
            self.price += 2
         if self.__chips == True :
            self.price += 1
   def get_doritos(self):
      return self.__doritos
   def set_doritos(self, new_doritos: bool):
         self.__doritos = new_doritos
         if self.__doritos == True :
            self.price += 2
         else:
            self.price -= 2
   def get_chips(self):
      return self.__chips
   def set_chips(self, new_chips: bool):
         self.__chips = new_chips
         if self.__chips == True :
            self.price += 1
         else:
            self.price -= 1
   def get_spicy(self):
      return self.__spicy
   def set_spicy(self, new_spicy: bool):
         self.__spicy = new_spicy
         if self.__spicy == True :
            self.price += 2
         else:
            self.price -= 2
               
class Entrance(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, potatoes: bool, sausage : bool, 
                 sauce: bool):
        super().__init__(name, price, quantity)
        self.__potatoes = potatoes
        self.__sausage = sausage
        self.__sauce = sauce
        if self.__potatoes == True :
            self.price += 1
        if self.__sausage == True :
            self.price += 2
        if self.__sauce == True:
            self.price += 0.2
   def get_potatoes(self):
      return self.__potatoes
   def set_potatoes(self, new_potatoes: bool):
         self.__potatoes = new_potatoes
         if self.__potatoes == True :
            self.price += 1
         else:
            self.price -= 1
   def get_sausage(self):
      return self.__sausage
   def set_sausage(self, new_sausage: bool):
         self.__sausage = new_sausage
         if self.__sausage == True :
            self.price += 2
         else:
            self.price -= 2
            
class FastFood(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, sauce: bool, premium:bool, 
                 extra: bool):
        super().__init__(name, price, quantity)
        self.__sauce = sauce
        self.__premium = premium
        self.__extra = extra
        if self.__extra == True :
            self.price += 2
        if self.__premium == True :
            self.price += 3
        if self.__sauce == True:
            self.price += 0.2
   def get_sauce(self):
      return self.__sauce
   def set_sauce(self, new_sauce: bool):
         self.__sauce = new_sauce
         if self.__sauce == True :
            self.price += 0.2
         else:
            self.price -= 0.2
   def get_premium(self):
      return self.__premium
   def set_premium(self, new_premium: bool):
         self.__premium = new_premium
         if self.__premium == True :
            self.price += 3
         else:
            self.price -= 3
   def get_extra(self):
      return self.__extra
   def set_extra(self, new_extra: bool):
         self.__extra = new_extra
         if self.__extra == True :
            self.price += 2
         else:
            self.price -= 2

class ForeignFood(MenuItem): #seteado y geteado
   def __init__(self, name, price, quantity, japanese: bool, italian: bool,
                 arabic: bool):
        super().__init__(name, price, quantity)
        self.__japanese = japanese
        self.__italian = italian
        self.__arabic = arabic
        if self.__japanese == True :
            self.price += 3
        if self.__italian == True :
            self.price += 2
        if self.__arabic == True:
            self.price += 1.5
   def get_japanese(self):
      return self.__japanese
   def set_japanese(self, new_japanese: bool):
         self.__japanese = new_japanese
         if self.__japanese == True :
            self.price += 3
         else:
            self.price -= 3
   def get_italian(self):
      return self.__italian
   def set_italian(self, new_italian: bool):
         self.__italian = new_italian
         if self.__italian == True :
            self.price += 2
         else:
            self.price -= 2
   def get_arabic(self):
      return self.__arabic
   def set_arabic(self, new_arabic: bool):
         self.__arabic = new_arabic
         if self.__arabic == True :
            self.price += 1.5
         else:
            self.price -= 1.5

class Payment:
   def __init__(self):
       pass
   def pagar(self, monto):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Card(Payment):
   def __init__(self,number: int, cvv: int):
      super().__init__()
      self.__number = number
      self.__cvv = cvv
   def get_number(self):
      return self.__number
   def set_number(self, new_number: int):
      self.__number = new_number
   def get_cvv(self):
      return self.__cvv
   def set_cvv(self, new_cvv: int):
      self.__cvv = new_cvv
   def pagar(self, monto):
      pagado = True
      print(monto)
      return pagado
   
class Cash(Payment):
   def __init__(self,monto: float, ingreso: float):
      self._ingreso = ingreso
      self.monto = monto
      super().__init__()
   def get_ingreso(self):
      return self._ingreso
   def set_ingreso(self, new_ingreso: float):
      self._ingreso = new_ingreso
   def calculate_cambio(self):
      if self._ingreso < self.monto:
         return "El ingreso es menor que el monto a pagar, por favor de más dinero"
      elif self._ingreso == self.monto:
         return "No hay cambio, gracias por su compra"
      else: return self._ingreso - self.monto
   def pagar(self, monto):
      pagado = True
      print(monto)
      return pagado

class Order: 
   def __init__(self,client,order = []):
      self.order = order
      self.client = client
   def additem(self,item:"MenuItem"):
      self.order.append(item)
   def delete_item(self,item:"MenuItem"):
      if item in self.order:
         self.order.remove(item)
      else: 
         print("el elemento no se puede remover porque no existe en el menú")
   def calculate(self):
      amount = 0
      for item in range(0,len(self.order),1):
         amount += self.order[item].calculate()
      for item in self.order:
        if isinstance(item, ForeignFood):
            amount -= item.calculate() * 0.10
        if isinstance(item, AlcoholicDrink) and item.get_bottle():
            amount -= item.calculate() * 0.05
        if isinstance(item, Soup) and item.get_changua():
            amount += amount * 0.15
      return amount
   def order_list(self):
        list = []
        for i in range(0,len(self.order),1):
            pre_list = []
            pre_list.append(self.order[i].name)
            pre_list.append(self.order[i].quantity)
            pre_list.append(self.order[i].price)
            pre_list.append(self.order[i].calculate())
            list.append(pre_list)
        return list
   def add_menu(self,order_list):
      with open(orden_json,"r") as ord:
         menu_actual = json.load(ord)
         nuevo_menu = {}
      for i in range(0,len(order_list),1):
         nuevo_menu[str(order_list[i][0])] = order_list[i][2]
         menu_actual.update(nuevo_menu)
      with open(orden_json,"w") as ord:
         json.dump(menu_actual,ord)
         
"""
arroz_con_pollo = Rice("pollito",15,2, True, True, False)
piña_colada = AlcoholicDrink("piñita",10,3, False, True, True)
arroz_con_pollo.calculate()
piña_colada.calculate()
picada = Entrance("picadita",5, 1, True, True, True)
orden = Order()
orden.additem(arroz_con_pollo)
orden.additem(picada)
print(orden.order[0].name)
print(picada.calculate())
print(arroz_con_pollo.calculate())
orden.calculate()
orden.order_list()
""" #parte de pruebas
def creador_de_ordenes() -> Order:
   nombre_cliente = input("por favor ingrese su nombre para tomar la orden: ")
   print("por favor elija que comida desea, tenemos:")
   print("Arroces(Rice), Sopas(Soup), Ensaladas(Salad), Postres(Dessert), Bebidas(Drink),")
   print("Bebidas Alcohólicas(AlcoholicDrink), Snacks, Entradas(Entrance), Comida Rápida(FastFood),")
   print("Comida Extranjera(ForeignFood)")
   tipo = None
   while tipo != '':
      tipo = input("ingrese el tipo(parentesís de las opciones)")
      nombre = str(input("ingrese el nombre del plato:"))
      cantidad = int(input("ingrese la cantidad de platos que se van a consumir:"))
      precio = float(input("ingrese el precio individual de cada plato:"))
      primera_adicion = bool(input("ingrese True o False si desea o no agregar la primera adición(costo extra):"))
      segunda_adicion = bool(input("ingrese True o False si desea o no agregar la segunda adición(costo extra):"))
      tercera_adicion = bool(input("ingrese True o False si desea o no agregar la tercera adición(costo extra):"))
      match tipo:
         case "Rice":
               item = Rice(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "Soup":
               item = Soup(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "Salad":
               item = Salad(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "Dessert":
               item = Dessert(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "Drink":
               item = Drink(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "AlcoholicDrink":
               item = AlcoholicDrink(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "Snacks":
               item = Snacks(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "Entrance":
               item = Entrance(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "FastFood":
               item = FastFood(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
         case "ForeignFood":
               item = ForeignFood(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
      orden_1 = Order(nombre_cliente)
      orden_1.additem(item)
      print("¿Desea agregar otro plato? (si/no)")
      respuesta = input()
      if respuesta == "si":
         continue
      else:
         lista_orden = orden_1.order_list()
         orden_1.add_menu(lista_orden)
         precio_orden = orden_1.calculate()
         print("hay dos opciones de medio de pago Tarjeta(Card) o efectivo(Cash)")
         medio_pago = str(input("ingrese su medio de pago (parentésis): "))
         if medio_pago == "Card":
            número = int(input("ingrese su número de tarjeta"))
            cvv = int(input("ingrese su código de autenticidad"))
            tarjeta = Card(número,cvv)
            tarjeta.pagar(precio_orden)
            precio_orden -= precio_orden * 0.025 #decuento por pagar con tarjeta
            print("Su orden es la siguiente:")
            for i in range(0,len(orden_1.order),1):
               print(orden_1.order[i].name)
            print("El total de su orden es: ", precio_orden)
            print("pagado con tarjeta", tarjeta.get_number())
            print("con cvv", '*'*len(str(tarjeta.get_cvv()))) #esto es para trolear al que quería ver el cvv
            break
         if medio_pago == "Cash":
            ingreso = float(input("ingrese el monto que va a pagar: "))
            efectivo = Cash(precio_orden, ingreso)
            cambio = efectivo.calculate_cambio()
            print("Su orden es la siguiente:")
            for i in range(0,len(orden_1.order),1):
               print(orden_1.order[i].name)
            #print(orden_1.order)
            print("El total de su orden es: ", precio_orden)
            print("pagado con una cantidad de efectivo", efectivo.get_ingreso(),"moneda corriente")
            break
      return orden_1
if __name__ == "__main__":
   print("bienvenido al restaurante XYZ")
   menu_del_día = namedtuple("menu_del_día",["entrada", "plato_fuerte", "bebida", "postre"])
   menu_de_hoy = menu_del_día(Soup("sopa de arroz",5,1,False,False,False), Rice("arroz blanco",6,1,True,False,False),
                              Drink("agua",2,1,False,False,False),Dessert("flan",2,1,False,False,False))
   primera_orden = creador_de_ordenes()
   segunda_orden = creador_de_ordenes()
   tercera_orden = creador_de_ordenes()
   cuarta_orden = creador_de_ordenes()
   quinta_orden = creador_de_ordenes()
   sexta_orden = creador_de_ordenes()
   septimma_orden = creador_de_ordenes()
   cola_ordenes_fifo.put(primera_orden)
   cola_ordenes_fifo.put(segunda_orden)
   cola_ordenes_fifo.put(tercera_orden)
   cola_ordenes_fifo.put(cuarta_orden)
   cola_ordenes_fifo.put(quinta_orden)
   cola_ordenes_fifo.put(sexta_orden)
   cola_ordenes_fifo.put(septimma_orden)
   while not cola_ordenes_fifo.empty():
      orden_actual = cola_ordenes_fifo.get()
      print(f"Procesando la orden de {orden_actual.order[0].name} pedida por {orden_actual.order[0].client}.")
      print("orden procesada exitosamente")