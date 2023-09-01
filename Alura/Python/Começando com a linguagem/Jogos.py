import Forca
import Advinhacao

def escolhe_jogo():

    print('\n*****************************')
    print('Escolha o seu jogo!')
    print('***************************** \n')


    print('(1) Forca (2) Advinhação')

    opcao = int(input('Qual Jogo? '))

    if opcao == 1:
        print('Jogando Forca')
        Forca.jogar_forca()
    elif opcao == 2:
        print('Jogando Advinhacao')
        Advinhacao.jogar_advinhacao()
    else:
        print('Digite uma opção valida')

if __name__ == '__main__':
    escolhe_jogo()
        