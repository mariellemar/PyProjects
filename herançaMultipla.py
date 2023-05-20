class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}'for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo
         
class Ave(Animal,):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
    
class Gato(Mamifero):
    pass

class Ornitorrinco(Ave, Mamifero):
    def __init__(self, cor_bico, cor_pelo, num_patas):
        super().__init__(cor_bico = cor_bico, cor_pelo = cor_pelo, num_patas = num_patas)
        print(Ornitorrinco.__mro__)

gato = Gato(num_patas = 4, cor_pelo = "Branco")
print(gato)
ornitorrinco = Ornitorrinco(num_patas = 4, cor_pelo = "verde", cor_bico = "laranja")
print(ornitorrinco)