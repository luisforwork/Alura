# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
print('Exercicio 1 - Resposta')

dict_ = {'nome': 'Luis Henrique', 'idade': '24', 'cidade': 'Sorocaba'}
nome = dict_['nome']
idade = dict_['idade']
cidade = dict_['cidade']

print(f'Nome: {nome}. Idade: {idade}. Cidade: {cidade}')

# 2 - Utilizando o dicionário criado no item 1:
print('Exercicio 2 - Resposta')
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
dict_['cidade'] = 'Sao Paulo'
# Adicione um campo de profissão para essa pessoa;
dict_['Profissão'] = 'Desenvolvedor'
# Remova um item do dicionário.
dict_.pop('idade')

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
print('Exercicio 3 - Resposta')

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
print('Exercicio 4 - Resposta')
dict_4 = {'Nome': 'Jorge', 'idade':'35', 'cidade':'Minas Gerais'}
valida = 'Chave existe' if 'profissao' in dict_4 else 'Chave não existe'
print(valida)

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

