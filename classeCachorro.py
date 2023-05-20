class Cachorro:
    def __init__(self, nome, cor, acordado):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def latir(self):
        print("auau")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave,valor in self.__dict__.items()])}"
    
    def __del__(slef):
        print("Deletando a instancia da classe")
        
name = input("Digite o nome: ")
coulor = input("Digete a cor: ")
woke = int(input("""para acordado digite 1
para dormindo digite 0: """))
if (woke == 1):
    woke = True
else:
    woke = False
dog = Cachorro(name, coulor, woke)
print(dog)
dog.latir() 