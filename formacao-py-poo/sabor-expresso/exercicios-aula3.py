# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
print('Exercicio 1 - Resposta')

lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = ['Luis', 'Henrique', 'Jessica', 'Maria']
lista_3 = ['1999', '2024']

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

print('Exercicio 2 - Resposta')
lista_loop = [1, 2, 3, 4, 5, 6]

for num in lista_loop:
    print(num)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
print('Exercicio 3 - Resposta')

num = 0
for x in range(10):
    if x%2 == 1:
        num = x + num

print(num)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
print('Exercicio 4 - Resposta')

num = 11
for x in range(1, 11):
    print(num - x)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
print('Exercicio 5 - Respostas')

num = int(input('Informe um número para visualizar sua Tabuada: '))

for x in range(1, 11):
    valor_tabuada = num * x
    print(f'{num} x {x}: {valor_tabuada}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 0

try: 
    for x in lista:
        num += x
    print(f'A soma dos valores da lista é: {num}')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
