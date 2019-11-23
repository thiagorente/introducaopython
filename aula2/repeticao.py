def ex_29():
    #29. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
    # continue pedindo até que o usuário informe um valor válido.
    numero = input('Digite um número entre 0 e 10: ')

    while (float(numero) < 0 or float(numero) > 10 or numero.isnumeric == False):
        print('Número inválido.')
        numero = input('Digite um número entre 0 e 10: ')

    print('A nota digitada foi {}'.format(numero).replace('.', ','))

def ex_45():
    #45. Faça um programa que calcule o valor total investido por um colecionador em sua coleção
    # de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de
    # CDs e o valor para em cada um.
    quantidade_cd = int(input('Digite a quantidade de CDs que você possui: '))
    valor_total_cd = 0

    for cont_cd in range(1, quantidade_cd + 1): #range vai ate o valor anterior ao ultimo
        valor_total_cd += (float(input('Digite o valor do CD {}: '.format(cont_cd))))

    print('Você já investiu R${:.2f} em CDs'.format(valor_total_cd).replace('.', ','))
    print('O valor médio de cada CD é R${:.2f}'.format(valor_total_cd/cont_cd).replace('.', ','))

def ex_47(numero_inteiro):
    #47. Os números primos possuem várias aplicações dentro da Computação, por exemplo na
    # Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
    # Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
    numero = int(numero_inteiro)
    valid_primo = True

    for num_valid_primo in range(numero - 1, 1, -1):
        #se o resto da divisao do numero informado pelo usuario e o numero da sequencia for 0 o numero informado nao e primo
        if(numero % num_valid_primo == 0):
            valid_primo = False 

    print('O número {} é primo.'.format(numero)) if valid_primo == True else print('O número {} não é primo.'.format(numero))


def run():
    ex_29()
    ex_45()
    ex_47(input('Digite um número inteiro: '))
