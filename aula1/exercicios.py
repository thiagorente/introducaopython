def ex_1(numero_cm):
    #1.	Faça um Programa que converta metros para centímetros.
    return print('{0} centímetros é igual a {1:.2f} metro(s)'.format(str(numero_cm), int(numero_cm) / 100).replace('.', ','))


def ex_2(raio_circulo):
    #2.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    pi = 3.14
    area_circulo = (float(raio_circulo)**2) * pi
    return print('A área do círculo de raio igual a {0} é {1}'.format(raio_circulo, area_circulo).replace('.', ','))


def ex_3(lado_quadrado):
    #3.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
    area_quadrado = float(lado_quadrado)**2
    return print('O dobro da área do quadrado com lado {0} é {1}'.format(lado_quadrado, area_quadrado * 2).replace('.', ','))


def calcula_salario(horas, ganho_hora):
    return horas * ganho_hora

def ex_5():
    #5.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    #Calcule e mostre o total do seu salário no referido mês.
    ganho_hora = float(input('Quanto você ganha por hora? '))
    horas_trabalhadas = float(input('E quantas horas você trabalha por mês? '))

    return print('Seu salário no mês é {:.2f}'.format(calcula_salario(horas_trabalhadas, ganho_hora)).replace('.', ','))


def converte_graus(farenheit):
    return (5 * (float(farenheit) -32)) / 9

def ex_6(graus_farenheit):
    #6.	Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
    # C = (5 * (F-32) / 9).
    return print('{0:.1f} graus Farenheit é igual a {1:.1f} graus Celsius'.format(float(graus_farenheit), converte_graus(graus_farenheit)))


def calculo_a(primeiro_numero, segundo_numero):
    return (int(primeiro_numero) * 2) * (int(segundo_numero) / 2)

def calculo_b(primeiro_numero, segundo_numero):
    return (int(primeiro_numero) * 3) + float(segundo_numero)

def calculo_c(primeiro_numero):
    return (float(primeiro_numero)**3)

def ex_7():
    #7.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # a.	o produto do dobro do primeiro com metade do segundo .
    # b.	a soma do triplo do primeiro com o terceiro.
    # c.	o terceiro elevado ao cubo.
    primeiro_numero = int(input('Digite um número inteiro: '))
    segundo_numero = int(input('Digite o segundo número inteiro: '))
    terceiro_numero = float(input('Digite um número real: '))

    return print('Cálculo a: {0}\nCálculo b: {1:f}\nCálculo c: {2:f}'.format(calculo_a(primeiro_numero, segundo_numero), calculo_b(primeiro_numero, terceiro_numero), calculo_c(terceiro_numero)).replace('.', ','))


def calcula_peso_ideal(sexo, altura):
    peso_ideal = 0

    if(str(sexo).upper() == 'M'):
        peso_ideal = ((72.7 * (int(altura)/100)) - 58)
    elif(str(sexo).upper() == 'F'):
        peso_ideal = ((62.1 * (int(altura)/100)) - 44.7)
    else:
        peso_ideal = 'erro'

    return peso_ideal

def ex_8():
    #8.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
    # que calcule seu peso ideal, utilizando as seguintes fórmulas:
    #a.	Para homens: (72.7*h) - 58
    #b.	Para mulheres: (62.1*h) - 44.7
    #Obs: o programa deverá perguntar o sexo da pessoa
    sexo = input('Qual seu sexo (digite M ou F): ')
    altura = input('Digite a sua altura em centímetros: ')

    calculo_peso_ideal = calcula_peso_ideal(sexo, altura)

    if(calculo_peso_ideal == 'erro'):
        return print('Insira um sexo válido (M ou F).')
    else:
        return print('Seu peso idela é {:.2f}kg'.format(calculo_peso_ideal).replace('.', ','))


def calcula_peso_excedente_dia(peso):
    peso_maximo = 50
    peso_excedente_dia = float(peso) - peso_maximo

    return peso_excedente_dia if peso_excedente_dia > 0 else 0

def calcula_multa(peso_excedente):
    multa_peso = 4
    calculo_multa = float(peso_excedente) * multa_peso

    return calculo_multa

def ex_9(peso_dia):
    #9.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
    # o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
    # que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
    # deve pagar uma multa de R$ 4,00 por quilo excedente. 
    # João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
    # calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
    # na variável multa o valor da multa que João deverá pagar. 
    # Imprima os dados do programa com as mensagens adequadas.

    peso_excedente = calcula_peso_excedente_dia(peso_dia)
    multa_dia = calcula_multa(peso_excedente)

    return print('Você excedeu {0:.2f}kg e deverá pagar uma multa de R${1:.2f}.'.format(peso_excedente, multa_dia).replace('.', ','))

def calcula_descontos(salario_bruto):
    porcentagem_ir = 0.11
    porcentagem_inss = 0.08
    porcentagem_sindicato = 0.05

    return [(salario_bruto * porcentagem_ir), 
            (salario_bruto * porcentagem_inss),
            (salario_bruto * porcentagem_sindicato)]

def ex_10():
    #10.	Faça um Programa que pergunte quanto você ganha por hora e 
    # o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
    # no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
    # 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # a.	salário bruto.
    # b.	quanto pagou ao INSS.
    # c.	quanto pagou ao sindicato.
    # d.	o salário líquido.
    # Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    # + Salário Bruto : R$
    # - IR (11%) : R$
    # - INSS (8%) : R$
    # - Sindicato ( 5%) : R$
    # = Salário Liquido : R$
    # Obs.: Salário Bruto - Descontos = Salário Líquido.

    ganho_hora = float(input('Informe quanto você ganha por hora: '))
    qtd_horas = int(input('Informe a quantidade de horas trabalhadas no mês: '))
    
    salario_bruto = float(calcula_salario(qtd_horas, ganho_hora))

    return print('Seu salário bruto é R${0:.2f}\nVocê paga R${1:.2f} de INSS\nVocê paga R${2:.2f} para o sindicato\nSeu salário líquido é de R${3:.2f}'.format(salario_bruto, 
                                                                                                                                                               calcula_descontos(salario_bruto)[1], 
                                                                                                                                                               calcula_descontos(salario_bruto)[2],
                                                                                                                                                               (salario_bruto - float(calcula_descontos(salario_bruto)[0]) - float(calcula_descontos(salario_bruto)[1]) - float(calcula_descontos(salario_bruto)[2]))).replace('.', ','))


def run():
    ex_1(input('Digite o tamanho desejado em centímetros: '))
    ex_2(input('Digite o raio do círculo que deseja calcular sua área: '))
    ex_3(input('Digite o lado do quadrado: '))
    ex_5()
    ex_6(input('Digite o grau Farenheit que deseja converter: '))
    ex_7()
    ex_8()
    ex_9(input('Digite o peso (em kg) dos peixes adquiridos hoje: '))
    ex_10()