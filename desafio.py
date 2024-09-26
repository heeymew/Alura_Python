'''
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
else:
    print('Adulto')

nome_cadastrado = 'Lucas'
senha_cadastrada = '1234'
nome = input('Digite o seu nome: ')
senha = input('Digite sua senha: ')


if nome != nome_cadastrado and senha != senha_cadastrada:
    print('Acesso negado!')
else:
    print(f'Bem vindo ao sistema {nome}!')

x = int(input('Digite o x das suas coordenadas: '))
y = int(input('Digite o y das suas coordenadas: '))

if x > 0 and y > 0:
    print('Primeiro quadrante!')
elif x < 0 and y > 0:
    print('Segundo quadrante!')
elif x < 0 and y < 0:
    print('Terceiro quadrante!')
elif x > 0 and y < 0:
    print('Quarto quadrante!')
else:
    print('O Ponto localizado está localizado no eixo ou origem')

'''