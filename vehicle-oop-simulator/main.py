# Classe base Veiculo (marca, modelo, ano, velocidade = 0)
# Métodos: acelerar() frear() info()
# Classe Carro (Portas)
# Métodos Buzinar
# Classe moto (Cilindradas)
# Métodos empinar

class Veiculo:
    def __init__(self, marca, modelo, ano, velocidade = 0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self._combustivel = 100
        self.consumo = 10

    def acelerar(self, quantidade):
        self.velocidade += 10 * quantidade
        self._combustivel -= self.consumo * quantidade
        if self.velocidade >= 100:
            self.velocidade = 100
            print(f'Velocidade maxima atingida: {self.velocidade} km/h')
        if self._combustivel <= 0:
            self._combustivel = 0
            print('Sem combustivel!')

    def frear(self, quantidade):
        self.velocidade -= 10 * quantidade
        if self.velocidade <= 0:
            self.velocidade = 0
            print(f'o Veiculo parou: {self.velocidade} km/h')

    def info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Velocidade: {self.velocidade}')
        print(f'Combustivel: {self._combustivel}')

    def abastecer(self, quantidade):
        self._combustivel += 20 * quantidade
        print(f'Abastecido: {self._combustivel}')
        if self._combustivel >= 100:
            self._combustivel = 100
            print('Tanque cheio')

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def info(self):
        super().info()
        print(f'Portas: {self.portas}')

    def buzinar(self):
        print('Beep!!!')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada
        self.consumo = 5

    def info(self):
        super().info()
        print(f'Cilindrada: {self.cilindrada}')

    def acelerar(self, quantidade):
        super().acelerar(quantidade)
        self._combustivel -= self.consumo * quantidade

veiculo_1 = Carro('Ferrari', 'LaFerrari', 2014, 2)
veiculo_2 = Carro('Porsche', '911 Turbo S', 2022, 2)
veiculo_3 = Carro('Ford', 'Mustang GT', 2021, 2)
veiculo_4 = Carro('BMW', 'M3 Competition', 2023, 4)
veiculo_5 = Carro('Audi', 'RS6 Avant', 2022, 4)

veiculo_6 = Moto('Honda', 'CB 500F', 2023, 500)
veiculo_7 = Moto('Yamaha', 'MT-07', 2022, 689)
veiculo_8 = Moto('Kawasaki', 'Ninja 650', 2021, 649)
veiculo_9 = Moto('Ducati', 'Panigale V2', 2023, 955)
veiculo_10 = Moto('BMW', 'S1000RR', 2024, 999)

veiculo_1.info()
print()
veiculo_1.acelerar(11)
print(f'Velocidade atual: {veiculo_1.velocidade} km/h')
print()
veiculo_1.frear(5)
print(f'Velocidade atual: {veiculo_1.velocidade} km/h')
print()
veiculo_1.buzinar()
print()
veiculo_1.abastecer(2)
print()
veiculo_1.acelerar(5)
print()
print(f'Velocidade atual: {veiculo_1.velocidade} km/h')
print()
veiculo_1.abastecer(5)
