
class Produto:
    __preco = float
    __categoria = str
    __codigo = int

    __lista = []

    def __init__(self, codigo=int):
        self.__codigo = codigo

    def getCodigo(self)-> int:
        return self.__codigo
    
    def setPreco(self,novo_preco=int)->None:
        self.__preco = novo_preco

    def getPreco(self)->int:
        return self.__preco
    
    def setCategoria(self,nova_categoria=str)->None:
        self.__categoria = nova_categoria

    def getCategoria(self)->str:
        return self.__categoria
    
    def adicionar(self):
        self.__lista.append(self.getCodigo())

    def getLista(self):
        return self.__lista

    def __str__(self):
        saida = "Resumo\n"
        saida += 'Código:'+str(self.getCodigo())+'\n'
        saida += 'Categoria:'+str(self.getCategoria())+'\n'
        saida += 'Preço:'+str(self.getPreco())
        return saida