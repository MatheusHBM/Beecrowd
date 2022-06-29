def posicaoRobo(n,m,matriz):#Função usada para pegar a posição do robo no circuito
    posL=0
    posC=0
    i=0
    j=0
    while (i<n): 
        while (j<m):
            if(matriz[i][j]=='N' or matriz[i][j]=='S' or matriz[i][j]=='L' or matriz[i][j]=='O'):#O robo será identificado com  a inicial de sua orientação
                posL=i
                posC=j
            j=j+1
        i=i+1
        j=0
    i=0 
    robo = matriz[posL][posC]#Identificação do robô. Ex: N
    posRobo = [posL,posC]#Posição onde o robô está
    return robo, posRobo 

def percorrer():
    entrada = input().split(" ")#Pega a entrada e transforma em uma lista
    n=int(entrada[0])#converte para int e atribui as variaveis
    m=int(entrada[1])
    s=int(entrada[2])
    figurinha = 0        
    matriz = []
    comandos = []
    i=0
    while (i<n):
        matriz.append([a for a in (input())])#popula a matriz com os elementos da entrada
        i=i+1
    comandos.append([a for a in (input())])#popula a lista de comandos com os elementos da entrada
    if(len(comandos[0])>s):
        exit()#caso haja mais comandos que o permitido, encerra a execução
    i=0
    while(i<len(comandos[0])):#Aqui o robô começa a percorrer o circuito
        robo, posRobo = posicaoRobo(n,m,matriz)#Em cada iteração, a orientação e a posição do robô é atualizada
        #Caso o comando seja virar à Esquerda ou Direita
        if (comandos[0][i]=='D'):
            if(robo=='N'):
                robo = 'L'#O robô recebe a nova orientação
                matriz[posRobo[0]][posRobo[1]]=robo #Grava o robô na posição atual do circuito
            elif(robo=='S'):
                 robo = 'O'
                 matriz[posRobo[0]][posRobo[1]]=robo
            elif(robo=='L'):
                 robo = 'S'
                 matriz[posRobo[0]][posRobo[1]]=robo
            elif(robo=='O'):
                 robo = 'N'
                 matriz[posRobo[0]][posRobo[1]]=robo
        elif (comandos[0][i]=='E'):
            if(robo=='N'):
                robo = 'O'
                matriz[posRobo[0]][posRobo[1]]=robo
            elif(robo=='S'):
                 robo = 'L'
                 matriz[posRobo[0]][posRobo[1]]=robo
            elif(robo=='L'):
                 robo = 'N'
                 matriz[posRobo[0]][posRobo[1]]=robo
            elif(robo=='O'):
                 robo = 'S'
                 matriz[posRobo[0]][posRobo[1]]=robo
        #Caso o comando dado seja ir pra Frente
        elif (comandos[0][i]=='F'):
            if(robo=='N'):
                if(posRobo[0]!=0):#verifica se não é um limite de circuito
                    if(matriz[posRobo[0]-1][posRobo[1]]!="#"):#Verifica se a posição que o robô está tentando se deslocar não é uma pilastra
                        matriz[posRobo[0]][posRobo[1]] = "."#Atribui um lugar limpo à posição atual do robô
                        posRobo[0]=posRobo[0]-1 #Desloca o robô para a posição desejada
                        if(matriz[posRobo[0]][posRobo[1]]=="*"): #Caso encontre uma figurinha
                            figurinha = figurinha +1
            elif(robo=='S'):
                if(posRobo[0]<n):
                    if(matriz[posRobo[0]+1][posRobo[1]]!="#"):
                        matriz[posRobo[0]][posRobo[1]] = "."
                        posRobo[0]=posRobo[0]+1
                        if(matriz[posRobo[0]][posRobo[1]]=="*"):
                            figurinha = figurinha +1
       #         
            elif(robo=='L'):
                 if(posRobo[1]<m):
                    if(matriz[posRobo[0]][posRobo[1]+1]!="#"):
                        matriz[posRobo[0]][posRobo[1]] = "."
                        posRobo[1]=posRobo[1]+1
                        if(matriz[posRobo[0]][posRobo[1]]=="*"):
                            figurinha = figurinha +1
            elif(robo=='O'):
                 if(posRobo[1]!=0):
                    if(matriz[posRobo[0]][posRobo[1]-1]!="#"):
                        matriz[posRobo[0]][posRobo[1]] = "."
                        posRobo[1]=posRobo[1]-1
                        if(matriz[posRobo[0]][posRobo[1]]=="*"):
                            figurinha = figurinha +1
        matriz[posRobo[0]][posRobo[1]] = robo #Coloca o robô na posição atual do circuito
        i=i+1
    print(figurinha)#imprime o numero de figurinhas que o robô coletou
    
percorrer()





