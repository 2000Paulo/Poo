class Comida:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        self.__preco = novo_preco


# Criando uma instância da classe Comida
pizza = Comida("Pizza", 25.99)

# Acessando o atributo preço usando o método get_preco()
print(pizza.get_preco())

# Modificando o preço usando o método set_preco()
pizza.set_preco(29.99)

# Acessando o atributo preço novamente
print(pizza.get_preco())
