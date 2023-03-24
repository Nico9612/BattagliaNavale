from random import randint
import sys
class Nave:
    
    def __init__(self,lenNave):
        self.nave=[1 for i in range(lenNave)]
        self.lenNave=lenNave

class Mappa:
    #creo la mappa vuota
    def __init__(self):
        self.mappa = [ [0 for i in range(10)]  for i in range(10)]

    #metodo per inserire una nave
    def inserisci_nave(self,nave):
        i=randint(0, (10-nave.lenNave))
        j=randint(0, (10-nave.lenNave))
        verso=randint(0, 1)
        #aggiungere i controlli per non far sovrapporre le navi
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
            print("Colpito!!")
    
    #metodo per stampare la mappa
    def stampa(self,game=True):

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
    mappa=Mappa()
    
    #creo le navi
    portaerei=Nave(5)
    Cacciatorpediniere= Nave(2)
    Sottomarino=Nave(3)

    #posiziono le navi nella mappa
    mappa.inserisci_nave(portaerei)
    mappa.inserisci_nave(Cacciatorpediniere)
    mappa.inserisci_nave(Sottomarino)
    
    #ciclo infinito per stampare la mappa e i colpi
    game=True
    while (game):
        
            mappa.stampa()
            mappa.spara(int(input("Inserire la coordinata X (da 1 a 10): ")),int(input("Inserire la coordinata Y (da 1 a 10): ")))
        
    