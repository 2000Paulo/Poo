class Comida:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        self.__preco = novo_preco



pizza = Comida("Pizza", 25.99)


print(pizza.get_preco())


pizza.set_preco(29.99)


print(pizza.get_preco())
