def ex_16():    
    #16. Faça um Programa que peça dois números e imprima o maior deles.
    primeiro_numero = float(input('Digite um número: '))
    segundo_numero = float(input('Digite outro número: '))

    if(primeiro_numero > segundo_numero):
        print('O número {} é maior.'.format(primeiro_numero))  
    elif(segundo_numero > primeiro_numero): 
        print('O número {} é maior.'.format(segundo_numero))
    else:
        print('Os números {0} e {1} são iguais.'.format(primeiro_numero, segundo_numero))

def ex_17(numero):
    #17. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
    if (float(numero) < 0):
        print('O número {} é negativo.'.format(numero))
    elif(float(numero) > 0):
        print('O número {} é positivo.'.format(numero))
    else:
        print('Você digitou {}.'.format(numero))

def ex_19(letra):
    #19. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
    if(letra.isalpha()):
        vogais = ['A', 'E', 'I', 'O', 'U']

        print('{} é uma vogal.'.format(letra)) if letra.upper() in vogais else print('{} é uma consoante.'.format(letra))
    else:
        print('Letra inválida.')


def run():
    ex_16()
    ex_17(input('Digite um número: '))
    ex_19(input('Digite uma letra: '))
