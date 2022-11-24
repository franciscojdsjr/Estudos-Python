import random

print('\n*****************************')
print('Bem vindo ao jogo advinhação!')
print('***************************** \n')

numero_secreto = round(random.random() * 100)
total_de_tentativas = 5
acertou = False


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
        print('Você digitou {}, Você Acertou!!'.format(palpite))
        acertou = True
        break
    else:
        if chute_maior:
            print('Você digitou {}, Você Errou!!, Seu chute foi maior que o número secreto.'.format(palpite))
        elif chute_menor:
            print('Você digitou {}, Você Errou!!, Seu chute foi menor que o número secreto.'.format(palpite))
            
if acertou == False:
    print('\nVocê não conseguiu! o numero secreto era o {}\n'.format(numero_secreto))
            

print('Fim do Jogo')
    
