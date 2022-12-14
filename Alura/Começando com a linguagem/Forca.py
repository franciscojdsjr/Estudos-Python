
def jogar_forca():
    
    import random
    print('\n*****************************')
    print('Bem vindo ao jogo Forca!')
    print('***************************** \n')
    
    arquivo = open('/home/francisco/Devlopment/Python Scripts/Alura/Começando com a linguagem/palavras.txt','r')
    palavra = []
    for linha in arquivo:
        palavra.append(linha.strip())
    arquivo.close()
    

    
    palavra_secreta = random.choice(palavra).upper().strip()
    letras_acertadas  = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    print('A Palavra possui {} Letras: {}'.format(len(palavra_secreta),letras_acertadas))

    #Designer tamanho da palavra secreta existe essa forma e a da linha 9
    #for letra in palavra_secreta:
    #   letras_acertadas.append('_')



    #enquanto não acerta ou não enforcou
    while not enforcou and not acertou:
        chute = input('Qual letra? ').upper().strip()
        palavra_secreta.find(chute)
        
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
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
        

if __name__ == '__main__':
    jogar_forca()