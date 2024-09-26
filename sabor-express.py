import os

restaurante = []

def exibir_greeting():
    print('Bem Vindo ao 𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔\n')

def exibir_opcoes():
        print('1. Cadastrar Restaurante')
        print('2. Listar restaurantes')
        print('3. Ativar restaurante')
        print('4. Sair')

def finalizar_app():
    print('𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔 agradece. Volte sempre!')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_um_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurante.append(nome_restaurante)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcoes():
    try:
        cadastro = int(input('Escolha uma opção: '))

        if cadastro == 1:
            cadastrar_um_restaurante()
        elif cadastro == 2:
            print('Listar restaurantes')
        elif cadastro == 3:
            print('Ativar restaurante')
        elif cadastro == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    # os.system('clear') no MAC
    exibir_greeting()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()