from random import randint

#area=int(input("Inserire la dimensione della griglia: "))
area=10
def campo(area):
    griglia=[]
    for i in range(0,area):
        riga=[]
        for j in range(0,area):
            riga.append(0)

        griglia.append(riga)
    return griglia
   #if i  == 0 or i==len(matrice)) and not (j == 0 or j==len(matrice)):
def nave(matrice,lenNave):
    r=randint(0, 1)
    i=randint(0, (len(matrice)-lenNave))
    j=randint(0, (len(matrice)-lenNave))
    try:
        if (i  == 0 or j == 0) and not (i==len(matrice) or j==len(matrice) ):
            if not matrice[i][j] == 1: #or not matrice[i+1][j] == 1 or not matrice[i][j+1] == 1:
                if r == 0:     
                #nave orizzontale
                    matrice[i][j]=1
                    matrice[i][j+1]=1
                #nave verticale
                else:
                    matrice[i][j]=1
                    matrice[i+1][j]=1
        else:

            if not matrice[i][j] == 1 or not matrice[i+1][j] == 1 or not matrice[i][j+1] == 1 or not matrice[i-1][j] == 1 or not  matrice[i][j-1] == 1:

                if r == 0:     
                #nave orizzontale
                    matrice[i][j]=1
                    matrice[i][j+1]=1
                #nave verticale
                else:
                    matrice[i][j]=1
                    matrice[i+1][j]=1      
                
    except:
        nave(matrice, lenNave)
    
    return matrice



if __name__=="__main__":
    z=campo(area)
    nave(z, 2)
    nave(z, 2)
    nave(z, 2)

    print(nave(z,2))
