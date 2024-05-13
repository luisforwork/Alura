class Restaurante:
    nome = ''
    categoria = 'Teste'
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

restaurante_praca.categoria = 'Italiana'
print(f'Atribuido o valor: {restaurante_praca.categoria} para o atributo CATEGORIA')

#2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

print(f'Atribudo nome da instância restaurante_praca: {restaurante_praca.nome}')

#3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

if restaurante_praca.ativo is True:
    print('Restaurante está Ativo.')
else:
    print("Restaurante esta Inativo.")

#4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

categoria = Restaurante().categoria
print(f'A categoria armazenado na classe Restaurante() é: {categoria}')

#5 - Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'
print(f'Nome alterado para {restaurante_praca.nome}')

#6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(vars(restaurante_pizza))

#7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print(f'A categoria do restaurante é {restaurante_pizza.categoria}')
else:
    print('A categoria do restaurante não é Fast Food')

#8 - Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.categoria = True

if restaurante_pizza.categoria is True:
    print('O Restaurante pizza está ativo.')
else:
    print('O Restaurante Pizza está inativo.')

#9 - Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'Nome: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria}')