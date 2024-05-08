import os

restaurantes = [{'nome':'Bar e Restaurante do Noia', 'categoria':'Brasileira', 'ativo':False}, 
                {'nome':'Roberio Salgados', 'categoria':'Buteco', 'ativo':True},
                {'nome':'Bar do Sulin', 'categoria':'Buteco', 'ativo':False}]

def exibir_nome_do_programa():
    '''Essa função é responsável por imprimir o nome do app para o usuário.'''
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def menu_opcoes():
    '''Essa função é responsável por imprimir o menu de ações para o usuário.'''
    print("""
        1. Cadastrar Restaurante
        2. Listar Restaurante
        3. Alternar estado Restaurante
        4. Sair
        
        """)

def cadastro_restaurante():
    '''Essa função é responsável por cadastrar novos restaurantes na lista de restaurantes. 
        Input - Nome do restaurante, categoria
        Output - Restaurante cadastrado na lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')

    voltar_menu_principal()

def lista_restaurante():
    '''Essa função é responsável por listar os restaurantes cadastrados e suas informações, como categoria e status.
        Output - Nome, categoria e status (ativo ou desativado) do restaurante
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

    voltar_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alterar o estado do restaurante - Ativo ou Desativado
        Input - Nome do restaurante
        Output - Alteração do status do restaurante na lista de restaurantes
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_menu_principal()

def finalizar_app():
    '''Essa função é responsável por encerrar o programa'''
    exibir_subtitulo('Encerrando programa')

def opcao_invalida():
    '''Essa função é responsável por identificar o input de uma alternativa invalida ou inexistente no menu
    '''
    print('Opcão inválida!')

    voltar_menu_principal()

def voltar_menu_principal():
    '''Essa função é responsável por direcionar o usuário para o menu inicial'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por limpar o menu e exibir a mensagem da alternativa escolhida.
        Input - String contendo as informações da alternativa escolhida
        Output - Limpeza do prompt e exibição da opção escolhida
    '''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    ## Teste match - Python 3.10
    # match opcao_escolhida:
    #     case 1:
    #         cadastro_restaurante()
    #     case _:
    #         finalizar_app()

def main():
    '''Função principal que inicia o programa'''
    os.system('clear')
    exibir_nome_do_programa()
    menu_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()