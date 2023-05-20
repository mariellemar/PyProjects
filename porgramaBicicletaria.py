#Problema: registrar as vendas de biciclietas

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    #self-> referencia explicita ao objeto, a instancia do objeto que foi passado
    #nomear a instanci do objeto como self é uma convenção de python
    #sef.(atributo)
    
    def buzinar(self): #metodos são como funções dentro de uma classe
        print("Plim plim...") #o aegumento a ser passado deve ser o self
         
    def parar(self):
        print("Parando bicicleta...\nBicileta parada!")
        
    def correr(self):
        print("Vrummm...")
            
    def __str__(self):
        #return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

cor_b = input("Cor da bicicleta: ")
modelo_b = input("Modelo da bicicleta: ")
ano_b = int(input("Ano da bicicleta: "))
valor_b = float(input("Valor da bicicleta: "))

bike = Bicicleta(cor_b, modelo_b, ano_b, valor_b)
bike.buzinar() #bike.buzinar() = Bicicleta.buzinar(bike)
bike.correr()
bike.parar()

print(bike)