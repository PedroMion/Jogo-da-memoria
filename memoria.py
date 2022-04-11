import random

def geraMatriz():
    valores = [0,0,1,1,2,2,3,3,4,4,5,5,6,6]
    i = 12
    matriz = []
    temp = []
    while i>0:
        rand = random.randint(0,i)
        temp.append(valores[rand])
        valores.remove(valores[rand])
        if(len(temp) == 4):
            matriz.append(temp)
            temp = []
        i -= 1
    return matriz

def printaMatriz(matriz):
    for i in range(3):
        print(matriz[i][0],"",matriz[i][1],"",matriz[i][2],"",matriz[i][3])

def geraMatrizIdentidade():
    matriz = []
    temp = []
    for i in range(3):
        for j in range(4):
            temp.append("*")
        matriz.append(temp)
        temp = []
    return matriz




