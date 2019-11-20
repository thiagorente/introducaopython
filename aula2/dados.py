def ex_1():
    #1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
    
    vetor = input('Digite 5 numeros inteiros separados por um espaco: ').split()
    for v in vetor :
        numero_inteiro = int(v)
        print(numero_inteiro)

def ex_2(nome):
    #2. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    for n in nome :
        print(n)

def ex_3():
    #3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

    primeira_nota = float(input('Digite a primeira nota: '))
    segunda_nota = float(input('Digite a segunda nota: '))
    terceira_nota = float(input('Digite a terceira nota: '))
    quarta_nota = float(input('Digite a quarta nota: '))

    print('Suas notas são: {0:.1f}, {1:.1f}, {2:.1f} e {3:.1f}'.format(primeira_nota, segunda_nota, terceira_nota, quarta_nota))
    print('Sua média é: {:.1f}'.format((primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4))

def ex_4(caracteres):
    #4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram
    # lidas. Imprima as consoantes.

    cadeia = caracteres.split()
    vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    qtd_consoantes = 0
    consoantes = []

    for c in cadeia:
        caractere = str(c)
        if(len(caractere) > 1):
            return print('Você digitou um caractere incorreto')

        if(caractere not in vogais):
            qtd_consoantes = qtd_consoantes + 1
            consoantes.append(c)

    print('Quantidade de consoantes digitadas: {}'.format(qtd_consoantes))
    if(len(consoantes) > 0):
        print('As consoantes digitadas foram: {}'.format(consoantes))

def ex_5(numeros_inteiros):
    #5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
    # números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

    vetor_total = []
    for numeros in numeros_inteiros.split(' '):
        vetor_total.append(int(numeros))

    if(len(vetor_total) != 20):
        return print('Você digitou mais ou menos que 20 números inteiros')

    numeros_pares = []
    numeros_impares = []
    print('Você digitou os números: {}'.format(vetor_total))

    for num in vetor_total:
        int_num = num
        if(int_num % 2 == 0):
            numeros_pares.append(int_num)
        else:
            numeros_impares.append(int_num)

    if(len(numeros_pares) > 0):
        print('Os números {} são pares'.format(numeros_pares))
    else:
        print('Você não digitou nenhum número par')

    if(len(numeros_impares) > 0):
        print('Os números {} são ímpares'.format(numeros_impares))
    else:
        print('Você não digitou nenhum número ímpar')

def ex_6(data_nascimento):
    #6. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a
    # data com o nome do mês por extenso.

    meses = { 1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março', 4 : 'Abril', 5 : 'Maio', 6 : 'Junho', 7 : 'Julho', 8 : 'Agosto', 9 : 'Setembro', 10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro' }
    data_quebrada = data_nascimento.split('/')
    dia = data_quebrada[0]
    mes = meses[int(data_quebrada[1])]
    ano = data_quebrada[2]
    print(dia + '/' + mes + '/' + ano)

def run():
    #ex_1()
    ex_2(input('Digite seu nome: '))
    ex_3()
    #ex_4(input('Digite 10 caracteres separados por um espaco: '))
    #ex_5(input('Digite 20 números inteiros: '))
    ex_6(input('Digite a sua data de nascimento (DD/MM/AAAA): '))