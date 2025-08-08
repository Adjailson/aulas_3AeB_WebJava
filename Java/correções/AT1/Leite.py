from Produto import Produto
import random as r

class Leite(Produto):
    __volume = float
    __descricao = str

    def __init__(self):
        __codigo = r.randint(1000001,9999999)
        super().__init__(__codigo)

    def setVolume(self,volume_ml=float)->float:
        self.__volume = volume_ml
        return volume_ml
    
    def setDescricao(self,descricao=str)->None:
        self.__descricao = descricao

    def getVolume(self)->float:
        return self.__volume
    
    def getDescricao(self)->str:
        return self.__descricao
    
    def extrato(self):
        return [Produto().getCodigo(),Leite()]
    
    def __str__(self):
        return "\nDescrição para leite"
    