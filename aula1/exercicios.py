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

def ex_6():
    #6.	Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
    # C = (5 * (F-32) / 9).


def run():
    ex_1(input('Digite o tamanho desejado em centímetros: '))
    ex_2(input('Digite o raio do círculo que deseja calcular sua área: '))
    ex_3(input('Digite o lado do quadrado: '))
    ex_5()
