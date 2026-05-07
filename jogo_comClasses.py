import random
listaPaises = ["Brasil","Argentina","Canada","Estados Unidos","Mexico","Chile","Suiça"]

class Jogador():
    def __init__(self, nome, altura, idade, posicao, time, ovr, titulos, paisAleatorio): #Parametros da Classe jogador
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.posicao = posicao
        self.time = time
        self.ovr = ovr
        self.titulos = titulos
        self.paisAleatorio = paisAleatorio
    
    #Metodo para exibir as informações do Jogador
    def exibirJogador(self):
        print(f" Nome: {self.nome}\n Altura: {self.altura}\n Idade: {self.idade}\n Posição: {self.posicao}\n Time: {self.time}\n Ovr: {self.ovr}\n Titulos: {self.titulos}\n Pais: {self.paisAleatorio}\n")
    
    #Metodo para ver se o jogador está disponivel, sem um time fixo
    def disponivel(self):
        self.time = "Warriors"

    #Metodo para saber se o jogador está lesionado
    def lesionar(self, OveralPerdido):
        self.ovr = self.ovr - OveralPerdido
        print(f"{self.nome} perdeu {OveralPerdido} OVR e restou {self.ovr} OVR\n")

    #Metodo para Almentar o Ovr do Jogador
    def ganhar(self, OveralRecuperado):
        self.ovr = self.ovr + OveralRecuperado
        print(f"{self.nome} ganhou {OveralRecuperado} OVR e restou {self.ovr} OVR\n")

    #Metodo para mostrar quantos titulos o jogador tem
    def QuantidadeTitulos(self, QuantidadeTitulos):
        self.titulos = self.titulos + QuantidadeTitulos 
        print(f"{self.nome} Possui {QuantidadeTitulos} Titulos {self.titulos} OVR\n")
    
    def IdadeJogador(self):
        self.idade = self.idade


#Criamos o objeto: ou seja, os dados dos jogador 
curry = Jogador("Curry", 1.91, 25, "Ala", "Warriors", 95, 4, random.choice(listaPaises))

heberton = Jogador("Heberton", 1.81, 21, "Ala Armador", "Warriors", 75, 2, random.choice(listaPaises))

lebron = Jogador("LeBron James", 2.06, 38, "Ala", "Lakers", 97, 4, random.choice(listaPaises))

durant = Jogador("Kevin Durant", 2.11, 35, "Ala", "Suns", 96, 2, random.choice(listaPaises))

kyrie = Jogador("Kyrie Irving", 1.88, 31, "Armador", "Mavericks", 92, 1, random.choice(listaPaises))

giannis = Jogador("Giannis Antetokounmpo", 2.11, 29, "Ala-Pivô", "Bucks", 98, 1, random.choice(listaPaises))

jokic = Jogador("Nikola Jokic", 2.11, 29, "Pivô", "Nuggets", 97, 1, random.choice(listaPaises))

tatum = Jogador("Jayson Tatum", 2.03, 26, "Ala", "Celtics", 94, 0, random.choice(listaPaises))

luka = Jogador("Luka Doncic", 2.01, 25, "Armador", "Mavericks", 96, 0, random.choice(listaPaises))

booker = Jogador("Devin Booker", 1.98, 27, "Ala-Armador", "Suns", 91, 0, random.choice(listaPaises))

morant = Jogador("Ja Morant", 1.88, 24, "Armador", "Grizzlies", 90, 0, random.choice(listaPaises))

embiid = Jogador("Joel Embiid", 2.13, 30, "Pivô", "76ers", 96, 1, random.choice(listaPaises))

butler = Jogador("Jimmy Butler", 2.01, 34, "Ala", "Heat", 91, 0, random.choice(listaPaises))

trae = Jogador("Trae Young", 1.85, 25, "Armador", "Hawks", 89, 0, random.choice(listaPaises))

zion = Jogador("Zion Williamson", 1.98, 23, "Ala-Pivô", "Pelicans", 90, 0, random.choice(listaPaises))

anthony_davis = Jogador("Anthony Davis", 2.08, 31, "Pivô", "Lakers", 94, 1, random.choice(listaPaises))

kawhi = Jogador("Kawhi Leonard", 2.01, 32, "Ala", "Clippers", 93, 2, random.choice(listaPaises))

curry.exibirJogador()
heberton.exibirJogador()
lebron.exibirJogador()
durant.exibirJogador()
kyrie.exibirJogador()
giannis.exibirJogador()
jokic.exibirJogador()
tatum.exibirJogador()
luka.exibirJogador()
booker.exibirJogador()
morant.exibirJogador()
embiid.exibirJogador()
butler.exibirJogador()
trae.exibirJogador()
zion.exibirJogador()
anthony_davis.exibirJogador()
kawhi.exibirJogador()

"""heberton.disponivel()
heberton.lesionar(20)
heberton.exibirJogador()
heberton.ganhar(50)
heberton.exibirJogador()
heberton.QuantidadeTitulos(8)
curry.exibirJogador()"""





