class Carro:
    def acelerar(self):
        pass


class CarroEsportivo(Carro):
    def acelerar(self):
        return "O carro esportivo está acelerando rapidamente!"


class CarroFamiliar(Carro):
    def acelerar(self):
        return "O carro familiar está acelerando suavemente."


# Criando instâncias das classes derivadas
carro1 = CarroEsportivo()
carro2 = CarroFamiliar()

# Chamando o método acelerar() de cada instância
print(carro1.acelerar())  
# Saída: "O carro esportivo está acelerando rapidamente!"
print(carro2.acelerar())  
# Saída: "O carro familiar está acelerando suavemente."
