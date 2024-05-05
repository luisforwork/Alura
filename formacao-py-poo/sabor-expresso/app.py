import os

restaurantes = ['Bar e Restaurante do Noia', 'Roberio Salgados']

def exibir_nome_do_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def menu_opcoes():
    print("""
        1. Cadastrar Restaurante
        2. Listar Restaurante
        3. Ativar Restaurante
        4. Sair
        
        """)

def cadastro_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')

    voltar_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Listando os restaurantes\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_menu_principal()

def ativa_restaurante():
    exibir_subtitulo('Ativar restaurante')

def finalizar_app():
    exibir_subtitulo('Encerrando programa\n')

def opcao_invalida():
    print('Opcão inválida!\n')

    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurante()
        elif opcao_escolhida == 3:
            ativa_restaurante()
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
    os.system('clear')
    exibir_nome_do_programa()
    menu_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()