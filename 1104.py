
def trocaCartas(entrada):
    quantidade =  entrada
    quantidade = quantidade.split(" ") #remove o espaço da string
    qtdAlice = int(quantidade[0]) #pega o primeiro numero da lista e converte para inteiro, é a quantidade máxima de cartas que Alice poderá ter  
    qtdBeatriz = int(quantidade[1]) #pega o segundo numero da lista e converte para inteiro, é a quantidade máxima de cartas que Beatriz poderá ter
    cartasAlice = input().split(" ")#Remove os espacos da string de numeros passada
    cartasAlice = [int(a) for a in cartasAlice]#converte os numeros da string passada para inteiros
    cartasBeatriz = input().split(" ")
    cartasBeatriz = [int(a) for a in cartasBeatriz]
    condicao = (len(cartasAlice) > qtdAlice) or (len(cartasBeatriz) > qtdBeatriz)#condição: cada criança não pode exceder seu numero máximo de cartas
    if(condicao): #caso exceda:
        exit() #termina o programa
    cartasValidasAlice = set(cartasAlice)#o objeto set não permite itens duplicados. portanto, se houver uma carta duplicada no montante, ele removerá e o numero de cartas trocaveis será menor
    cartasValidasBeatriz = set(cartasBeatriz)
    if(len(cartasValidasAlice)>len(cartasValidasBeatriz)): #o numero de cartas trocaveis tem que ser, no maximo, igual ao menor numero de cartas entre as duas
        cartasTrocaveis = len(cartasValidasBeatriz)
    else:
        cartasTrocaveis = len(cartasValidasAlice)#caso o numero seja igual, também entra nesse else.
    repetidas = set(cartasAlice) & set(cartasBeatriz)#cria um objeto apenas com as cartas repetidas entre as duas
    if(bool(repetidas)): #verifica se o objeto não está vazio
        cartasTrocaveis = cartasTrocaveis - len(repetidas) #caso nao esteja vazio
    if(cartasTrocaveis < 0): #não há como trocar um numero negativo de cartas, esse if garante que isso não vai acontecer
            cartasTrocaveis = 0            
    print (cartasTrocaveis)

def execucao():
    entrada = input() #pega a entrada do numero de cartas
    if(entrada != "0 0"): #se for diferente que a condição de parada:
        trocaCartas(entrada)
        execucao()
    else:
        exit()#termina o programa

        
execucao()