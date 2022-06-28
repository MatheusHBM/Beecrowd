def somaAlgarismos(num):
    soma = [int(a) for a in str(num)]#transforma um numero em uma lista de caracteres, converte os caracteres para int
    i=1
    aux = soma[0] #o aux recebe o elemento 0 (primeiro) da lista
    while i<=len(soma)-1: #o iterador começa no segundo elemento, assim ele pode receber o elemento anterior
        aux=aux+soma[i] # o numero atual é somado com o total até agora
        i=i+1 #incremento de iterador
    if(aux>9): #verifica se o numero possui mais de um digito
        aux=somaAlgarismos(aux) #caso possua, a função é executada novamente
        return aux 
    else: # caso não possua
        return aux
    

def maiorNumero(entrada):
    aux = entrada.split(" ")
    n = int(aux[0])
    m = int(aux[1])
    m=somaAlgarismos(m)# reduz o numero da entrada a apenas um digito
    n=somaAlgarismos(n)

    #faz as comparações para a saida
    if(n>m):
        print(1)
    elif (n<m):
        print (2)
    else:
        print(0)



def execucao():
    entrada = input()
    #as variaves recebem as strings de entrada e convertem para int 
    if (entrada != "0 0"):#verifica se a condição é válida
        #se a condição for true:
        maiorNumero(entrada)        
        execucao()
        
execucao()

    