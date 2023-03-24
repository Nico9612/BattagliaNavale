from random import randint
import sys

class Nave:
    
    def __init__(self,lenNave):
        self.nave=[1 for i in range(lenNave)]
        self.lenNave=lenNave

class Mappa:
    #creo la mappa vuota
    def __init__(self,intervallo):
        self.intervallo=intervallo
        self.mappa = [ [0 for i in range(self.intervallo)]  for i in range(self.intervallo)]

    #metodo per inserire una nave
    def inserisci_nave(self,nave):
        #creo un offset di una casella per semplificare i controlli
        i=randint(1, (self.intervallo-(nave.lenNave+1)))
        j=randint(1, (self.intervallo-(nave.lenNave+1)))
        verso=randint(0, 1)
        #!!!!! Aggiungere i controlli per non far sovrapporre le navi !!!!
        if verso == 0:
            for k in range(nave.lenNave):
                self.mappa[i][j+k]=1
        else:    
            for k in range(nave.lenNave):
                 self.mappa[i+k][j]=1
    
    #metodo per sparare un colpo
    def spara(self,x,y):
        self.x=x-1
        self.y=y-1
        
        if self.mappa[self.y][self.x] == 0:
            self.mappa[self.y][self.x]="M"
            print("Mancato =( ")
        else:
            self.mappa[self.y][self.x]="X"
            if self.mappa[self.y+1][self.x]!= 1 and self.mappa[self.y-1][self.x]!= 1 and self.mappa[self.y][self.x+1]!= 1 and self.mappa[self.y][self.x-1]!= 1:  
                print("Affondata!!!!")
            else:
                print("Colpita!!")
    
    #controllo se ci sono ancora pezzi di nave altrimenti stampo hai perso
    def game(self):
        cont=0
        for i in range(self.intervallo):
            for j in range(self.intervallo):

                if self.mappa[i][j]==1:
                    cont+=1
                
        if cont > 0:
            return True        
        else:
            print("Hai Perso")
            return False

    #metodo per stampare la mappa
    def stampa(self):

        for riga in self.mappa:
            for elemento in riga:
                #stampo 0 per il mare
                if elemento == 0:
                    sys.stdout.write(str(0)+" ")
                #stampo 1 per le navi
                
                elif elemento == 1:
                    sys.stdout.write(str(1)+" ")
                #stampo M per il colpo mancato
                
                elif elemento == "M":
                    sys.stdout.write("M"+" ")
                else:
                    sys.stdout.write("X"+" ")


            sys.stdout.write("\n")
       



if __name__=="__main__":
    
    #creo la mappa
    mappa=Mappa(10)
    
    #creo le navi

    #portaerei=Nave(5)
    Cacciatorpediniere= Nave(2)
    #Sottomarino=Nave(3)

    #posiziono le navi nella mappa

   # mappa.inserisci_nave(portaerei)
    mappa.inserisci_nave(Cacciatorpediniere)
    #mappa.inserisci_nave(Sottomarino)
    
    #ciclo infinito per stampare la mappa e i colpi
    game=True
    while (game):
        
            mappa.stampa()
            mappa.spara(int(input(f"Inserire la coordinata X (da 1 a {mappa.intervallo}): ")),int(input(f"Inserire la coordinata Y (da 1 a {mappa.intervallo}): ")))
            game = mappa.game()
    