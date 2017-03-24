from random import randint

class Jogo(object):

    def __init__(self):
        self.jogo = "jogo"
	#medaalvo()
	#atualizabola() -> alvo

class Alvo(object):
    
    def __init__(self):
	self.alvo = "alvo"
	#medavalor() soma

class Urna(object):

    def __init__(self):
	self.urna = "urna" 

    def medaBola(self, bola):
	self.valor = bola.random()
	#criabola -> Jogo

class Bola(object):
    
    
    def __init__(self):
	self.bola = "bola"

    def random(self):
	numero = randint(0, 20)
	return numero


bola1 = Bola()
urna1 = Urna()
alvo1 = Alvo()

urna1.medaBola(bola1)

print "A urna sorteou uma bola, qual o valor do alvo?"
	
palpite = raw_input("> ")
		
if palpite == urna1.valor:
   print "Ganhou"
	   
else:
   print "Perdeu - " + "Alvo: " + str(urna1.valor) + " " + " Palpite: " + str(palpite)
	

   
