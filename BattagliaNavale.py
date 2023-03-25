#!/usr/bin/python3
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
        self.mappa = [ ["-" for i in range(self.intervallo)]  for i in range(self.intervallo)]

    #metodo per inserire una nave
    def inserisci_nave(self,nave):
        #!!!!! controlli per non far sovrapporre le navi !!!
       
        while True:
            sovrapposte = False
            #scelgo una posizione iniziale e un verso casuale
            i=randint(0, (self.intervallo-(nave.lenNave)))
            j=randint(0, (self.intervallo-(nave.lenNave)))
            verso=randint(0, 1)
            
            for s in range(nave.lenNave):
                
                if verso==0:
                    if j+s >= self.intervallo or self.mappa[i][j+s] != "-":
                        sovrapposte = True
                        break
                    
                    if i>0 and self.mappa[i-1][j+s] != "-":
                        sovrapposte = True
                        break
                    if i< self.intervallo-1 and self.mappa[i+1][j+s] != "-":
                        sovrapposte = True
                        break
                else:
                    if i+s >= self.intervallo or self.mappa[i+s][j] != "-":
                        sovrapposte = True
                        break
                    if j > 0 and self.mappa[i+s][j-1] != "-":
                        sovrapposte = True
                        break
                    if j < self.intervallo-1 and self.mappa[i+s][j+1] != "-":
                        sovrapposte = True
                        break
            #se non sono sovrapposte le inserisco nella mappa
            if not sovrapposte:

                if verso == 0:
                    for k in range(nave.lenNave):
                        self.mappa[i][j+k]="N"
                    break
                else:    
                    for k in range(nave.lenNave):
                        self.mappa[i+k][j]="N"
                    break
            
           
        
    #metodo per sparare un colpo
    def spara(self,x,y):
        self.x=x-1
        self.y=y-1
        
        if self.mappa[self.y][self.x] == "-":
            self.mappa[self.y][self.x]="M"
            print("Mancato =( ")
        else:
            self.mappa[self.y][self.x]="X"
            print("Colpita!!")
    
    #controllo se ci sono ancora pezzi di nave altrimenti stampo hai perso
    def game(self):
        #contatore per verificare che ci siano ancora pezzi di nave (gli 1 sulla griglia)
        cont=0
        for i in range(self.intervallo):
            for j in range(self.intervallo):

                if self.mappa[i][j]=="N":
                    cont+=1
                
        if cont > 0:
            return True        
        else:
            print("Non Hai Più Navi Mi Dispiace Hai Perso!!")
            return False

    #metodo per stampare la mappa
    def stampa(self):
        

        for riga in self.mappa:
            
            print(" ".join(riga))
       



if __name__=="__main__":
    
    #creo la mappa
    mappa=Mappa(10)
    
    #creo le navi

    portaerei=Nave(5)
    Cacciatorpediniere= Nave(2)
    Sottomarino=Nave(3)

    #posiziono le navi nella mappa

    mappa.inserisci_nave(portaerei)
    mappa.inserisci_nave(portaerei)
    mappa.inserisci_nave(Cacciatorpediniere)
    mappa.inserisci_nave(Sottomarino)
    mappa.inserisci_nave(Sottomarino)
    
    #ciclo infinito per stampare la mappa e i colpi
    game=True
    while (game):
        
            mappa.stampa()
            mappa.spara(int(input(f"Inserire la coordinata X (da 1 a {mappa.intervallo}): ")),int(input(f"Inserire la coordinata Y (da 1 a {mappa.intervallo}): ")))
        
            game = mappa.game()
    