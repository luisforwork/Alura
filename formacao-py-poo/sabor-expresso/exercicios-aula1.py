# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Exercicio 1 - Resposta')
print('Python na Escola de Programação da Alura.')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
print('\nExercicio 2 - Resposta')
nome = 'Luis Henrique'
idade = 24

print(f'Meu nome é {nome} e tenho {idade} anos.')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
# A
# L
# U
# R
# A
print('\nExercicio 3 - Resposta')
print('A', 'L', 'U', 'R', 'A', sep='\n')
# print('A\nl\nu\nr\na')


# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o 
# valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
print('\nExercicio 4 - Resposta')

pi = 3.14159
# pi_arredondado = round(pi, 2)
# print(f'O valor arredondado de pi é: {pi}')
print(f'O valor arredondado de pi é: {pi:.2f}')