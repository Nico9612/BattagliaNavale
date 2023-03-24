from random import randint

area=10
#area=int(input("Inserire la dimensione della griglia: "))
def campo(area):
    campo={}
    l="ABCDEFGHIJKLMNOPQRSTUVZ"
    x=[i for i in range(1,area+1)]
    y=[i for i in l]


    for i in range(0,area):
        for j in range(0,area):
            
            campo[f"{y[i]}{x[j]}"]=0
    return campo

print(campo(10))