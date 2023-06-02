class Planeta:
    def __init__(self, nome, diametro, populacao):
        self.nome = nome
        self.diametro = diametro
        self.populacao = populacao
    
    def apresentar(self):
        print(f"Planeta: {self.nome}")
        print(f"Diametro: {self.diametro}")
        print(f"População: {self.populacao}")


class PlanetaTerra(Planeta):
    def __init__(self, nome, diametro, populacao, continentes):
        super().__init__(nome, diametro, populacao)
        self.continentes = continentes
    
    def apresentar(self):
        super().apresentar()
        print(f"Continentes: {self.continentes}")


class PlanetaMarte(Planeta):
    def __init__(self, nome, diametro, populacao, exploracoes):
        super().__init__(nome, diametro, populacao)
        self.exploracoes = exploracoes
    
    def apresentar(self):
        super().apresentar()
        print(f"Explorações: {self.exploracoes}")


# Criando instâncias das classes
planeta1 = Planeta("Júpiter", 139820, 0)
terra1 = PlanetaTerra("Terra", 12742, 7700000000, 7)
marte1 = PlanetaMarte("Marte", 6779, 0, "Curiosity, Perseverance")


# Chamando os métodos das instâncias
print("Planeta 1:")
planeta1.apresentar()
print()

print("Terra 1:")
terra1.apresentar()
print()

print("Marte 1:")
marte1.apresentar()
