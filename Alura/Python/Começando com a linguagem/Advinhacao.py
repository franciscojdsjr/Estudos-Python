
def jogar_advinhacao():

    import random

    print('\n*****************************')
    print('Bem vindo ao jogo advinhação!')
    print('***************************** \n')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    acertou = False
    dificuldade = int(input('Escolha a dificuldade e digite o numero relacionado \n 1. Facil \n 2. Médio \n 3. Dificil \n Digite a opção: '))
    pontuacao = 1000

    ##Define a Dificuldade
    if dificuldade == 1:
        total_de_tentativas = 10
    elif dificuldade == 2:
        total_de_tentativas = 5
    elif dificuldade == 3:
        total_de_tentativas = 3
    else:
        print('Digite uma opção valida\nPrograma Encerrado')
        quit()




    ##Laço de repetição do jogo
    ##while rodada <= total_de_tentativas: ## pode se usar While e o For
    for rodada in range(1,total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada,(total_de_tentativas)))
        palpite = int(input('Digite um número entre 1 e 100: '))
        if palpite < 1 or palpite > 100:
            print('\nVocê deve digitar um numero entre 1 e 100\n')
            continue
        acertou     = palpite == numero_secreto
        chute_maior = palpite > numero_secreto
        chute_menor = palpite < numero_secreto
        if acertou:
            print('Você digitou {}, Você Acertou!! Sua pontuação foi {}'.format(palpite,pontuacao))
            acertou = True
            break
        else:

            if chute_maior:
                print('Você digitou {}, Você Errou!!, Seu chute foi maior que o número secreto.'.format(palpite))
            elif chute_menor:
                print('Você digitou {}, Você Errou!!, Seu chute foi menor que o número secreto.'.format(palpite))
            pontos_perdidos = abs(numero_secreto - palpite)
            pontuacao = pontuacao - pontos_perdidos
    if acertou == False:
        print('\nVocê não conseguiu! o numero secreto era o {}\n'.format(numero_secreto))


    print('Fim do Jogo')
    
##chamar no console a func
if __name__ == '__main__':    
    jogar_advinhacao()
