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

def run():
    ex_1(input('Digite o tamanho desejado em centímetros: '))
    ex_2(input('Digite o raio do círculo que deseja calcular sua área: '))
    ex_3(input('Digite o lado do quadrado: '))
    ex_5()
    ex_6(input('Digite o grau Farenheit que deseja converter: '))
    ex_7()

    