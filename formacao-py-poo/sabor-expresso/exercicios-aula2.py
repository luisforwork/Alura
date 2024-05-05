# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
print('Exercicio 1 - Resposta\n')

num = int(input('Insira um número: \n'))

if (num % 2) == 0:
    print(f'O numero informado: {num}, é par')
else:
    print(f'O numero informado: {num}, é impar')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print('Exercicio 2 - Resposta\n')

idade = int(input('Informe sua idade: \n'))

if idade >= 0 and idade <= 12:
    print(f'A idade informada: {idade} te categoriza como uma criança.')
elif idade >= 13 and idade <= 18:
    print(f'A idade informada: {idade} te categoriza como um adolescente.')
elif idade >= 18:
    print(f'A idade informada: {idade} te categoriza como um adulto.')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
print('Exercicio 3 - Resposta\n')

inf_user = input('Informe seu usuario: \n')
inf_pass = input('Informe sua senha: \n')

user = 'Joaozinho123'
pass_ = 'AluraCurso'

if inf_user == user and inf_pass == pass_:
    print('Login bem-sucedido. Bem vindo!')
else:
    print('Usuário ou senha incorretos')

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

print('Exercicio 4 - Resposta\n')

coordx = int(input('Informe as coordenadas X: \n'))
coordy = int(input('Informe as coordenadas Y: \n'))

if coordx > 0 and coordy > 0:
    print(f'As coordenadas informadas (x: {coordx}, y: {coordy}) encontram-se no primeiro quadrante.')
elif coordx < 0 and coordy > 0:
    print(f'As coordenadas informadas (x: {coordx}, y: {coordy}) encontram-se no segundo quadrante.')
elif coordx < 0 and coordy < 0:
    print(f'As coordenadas informadas (x: {coordx}, y: {coordy}) encontram-se no terceiro quadrante.')
elif coordx > 0 and coordy < 0:
    print(f'As coordenadas informadas (x: {coordx}, y: {coordy}) encontram-se no quarto quadrante.')
else:
    print('O ponto está localizado no eixo ou origem.')