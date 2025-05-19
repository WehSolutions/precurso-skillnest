from myclass.TarjetaCredito import TarjetaCredito
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = TarjetaCredito(0,20000,0.015)
    """
    / Este bloque ya no tiene sentido ya que estas operaciones se pueden hacer directo con la clase TarjetaCredito
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        if (self.limite_credito - self.saldo_pagar) >= monto:
            self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        else:
            print("Ha sobrepasado limite de credito de :",self.limite_credito)
            self.mostrar_saldo_usuario()
        return self

    def pagar_tarjeta(self,monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_saldo_usuario(self):
        print("Saldo de tarjeta habiente :",self.nombre,self.apellido,"es de :",self.limite_credito-self.saldo_pagar)
        return self

    def transferir_deuda(self,otro_usurio,monto):
        pass
    /
    """
   
""""
usuario1 = Usuario("Miyagui","Soto","")
usuario2 = Usuario("Patmorita","Peréz","")
usuario1.hacer_compra(1000)
usuario1.hacer_compra(1500)
usuario1.pagar_tarjeta(2000)
print(usuario1.mostrar_saldo_usuario())
print("*"*10)
usuario2.hacer_compra(5000)
usuario2.hacer_compra(10000)
usuario2.hacer_compra(5000)
usuario2.pagar_tarjeta(5000)
usuario2.pagar_tarjeta(5000)
usuario2.pagar_tarjeta(5000)
usuario2.pagar_tarjeta(5000)
print(usuario2.mostrar_saldo_usuario())
print("*"*10)
usuario1.hacer_compra(30000)
usuario1.pagar_tarjeta(500)
usuario1.hacer_compra(30000)
print(usuario1.mostrar_saldo_usuario())
"""
usuario1 = Usuario("Miyagui","Soto","")
usuario1.tarjeta.compra(100)
print(usuario1.tarjeta.saldo_pagar)
