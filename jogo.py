#python2.7

from random import randint

class Computador(object):
	
    def __init__(self):
	self.computador = "computador criado"
	self.jogo1 = Jogo()
	self.counts = 0
	
    def jogar(self, jogo):
	self.jogo1.urna1.medaBola(self.jogo1.urna1.bola1)
	self.jogo1.alvo1.medaValor(self.jogo1.urna1)
	self.jogo1.medaAlvo(self.jogo1.alvo1)
	
	print "A urna sorteou uma bola " + str(self.jogo1.urna1.valor) + " , qual o valor do alvo?"
	
	palpite = raw_input("> ")

	if str(palpite) == str(self.jogo1.acerto):
	   print "Ganhou"
	   
	else:
   	   print "Errou - " + "Alvo: " + str(self.jogo1.acerto) + " " + " Palpite: " + str(palpite)
	   if self.jogo1.acerto <= 100:
	      self.jogo1.alvo1.soma = self.jogo1.acerto
	      self.jogar(self.jogo1)	
	   else:
	      print "Perdeu!"
	      return   

class Jogo(object):

    def __init__(self):
        self.jogo = "jogo criado"
	self.urna1 = Urna()
	self.alvo1 = Alvo()

    def medaAlvo(self, alvo):
	self.acerto = alvo.alvoValor

class Alvo(object):
    
    def __init__(self):
	self.alvo = "alvo criado"
	self.soma = 0
	
    def medaValor(self, urna):
	if self.soma == 0:
	   self.alvoValor = urna.valor
	else:
	   self.alvoValor = urna.valor + self.soma

class Urna(object):

    def __init__(self):
	self.urna = "urna criada" 
	self.bola1 = Bola()

    def medaBola(self, bola):
	self.valor = bola.random()

class Bola(object):
      
    def __init__(self):
	self.bola = "bola criada"

    def random(self):
	numero = randint(1, 20)
	return numero

	

   
