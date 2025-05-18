class TarjetaCredito:
    #Incluye en este método valores por default
    def __init__(self, saldo_pagar, limite_credito, intereses):
        #TU CODIGO (Aquí va los atributos de instancia y sus asignaciones de valor)
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        #TU CODIGO
        if (self.limite_credito - self.saldo_pagar) >= monto:
                self.saldo_pagar += monto + monto*self.intereses  #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        else:
            print("Ha sobrepasado limite de credito de :",self.limite_credito)
            self.mostrar_info_tarjeta()
        return self
    
    def pago(self, monto):
        #TU CODIGO
        self.saldo_pagar -= monto
        return self


    def mostrar_info_tarjeta(self):
        #TU CODIGO
       print("Saldo de tarjeta habiente es de :",self.limite_credito-self.saldo_pagar)
       return self


    def cobrar_interes(self):
        #TU CODIGO
        self.saldo_pagar += self.intereses
        return self
"""    
tarjeta1 = TarjetaCredito(0,30000,0.02)
tarjeta2 = TarjetaCredito(0,25000,0.02)
tarjeta3 = TarjetaCredito(0,40000,0.02)
**************
tarjeta1.compra(1000).compra(5000).pago(2000)
**************
tarjeta2.compra(1000).compra(5000).pago(2000).compra(5000).pago(2000)
**************
tarjeta3.compra(1000).compra(5000).compra(2000).compra(5000).compra(28000)
"""

