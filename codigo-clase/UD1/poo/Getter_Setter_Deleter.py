'''

@property → define un getter (para leer saldo).

@radio.setter → controla cuándo se asigna (c1.saldo = x).

@radio.deleter → permite borrar (del c1.radio).
'''

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    @property
    def saldo(self):
        """Getter: devuelve el saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, cantidad):
        """Setter: impide saldos negativos"""
        if cantidad >= 0:
            self._saldo = cantidad
        else:
            raise ValueError("El saldo no puede ser negativo")





cb = CuentaBancaria(100)
print(cb.saldo)
#cb.saldo = -100
cb.saldo(0)

'''
¿Por qué usamos _saldo en lugar de saldo?

Dentro de la clase defines una propiedad llamada saldo (con @property).

Si en el setter usáramos self.saldo = cantidad, estarías llamando de nuevo al setter, creando un bucle infinito (recursión).

Para evitar eso, se crea un atributo interno con otro nombre (por convención, con guion bajo: _saldo), y ahí se guarda el valor real.
'''