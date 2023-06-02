class Carro:
    def acelerar(self):
        pass


class CarroEsportivo(Carro):
    def acelerar(self):
        return 


class CarroFamiliar(Carro):
    def acelerar(self):
        return 



carro1 = CarroEsportivo()
carro2 = CarroFamiliar()


print(carro1.acelerar())
print(carro2.acelerar())
