import random    

def jogar_forca():
    
    mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas  = carregar_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0
    print('A Palavra possui {} Letras: {}'.format(len(palavra_secreta),letras_acertadas))

    while not enforcou and not acertou:
        chute = solicitar_chute()
        
        palavra_secreta.find(chute)
        
        if chute in palavra_secreta:
            inserir_letra_acertada(chute,palavra_secreta,letras_acertadas)
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print('A Palavra possui {} Letras: {}'.format(len(palavra_secreta),letras_acertadas))
        
        if acertou == True:
            print('Você acertou!')
        elif enforcou == True:
            print('Você errou! a palavra secreta era: {}'.format(palavra_secreta))
    
    print('Fim de Jogo')
        
 #Funções do Jogo   
        
def mensagem_abertura ():
   print('\n*****************************')
   print('Bem vindo ao jogo Forca!')
   print('***************************** \n')       
        
def carregar_palavra_secreta():
    arquivo = open('/home/francisco/Devlopment/Python Scripts/Alura/Começando com a linguagem/palavras.txt','r')
    palavra = []
    for linha in arquivo:
        linha = linha.strip() ##tratando retirando espaços
        palavra.append(linha)
    arquivo.close()
    palavra_secreta = random.choice(palavra).upper().strip()
    return palavra_secreta

def carregar_letras_acertadas(palavra):
    return ['_' for letra in palavra]        
        
def solicitar_chute():
    chute = input('Qual letra? ').upper().strip()
    return chute

def inserir_letra_acertada(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

if __name__ == '__main__':
    jogar_forca()
    
    
        #Designer tamanho da palavra secreta existe essa forma e a da linha 9
    #for letra in palavra_secreta:
    #   letras_acertadas.append('_')

    #enquanto não acerta ou não enforcou