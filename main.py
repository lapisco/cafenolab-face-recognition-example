from cadastro_novos import cadastrar
from bancos import gerar_bancos
from frames_crops import imagens
from teste_local import teste
from treinar_descritores import treinar

def main():
    func = int(input('O que vc deseja fazer\n(1)Se cadastrar\n(2)Gerar os pesos e alimentar o banco\n(3)Testar\n(4)Sair\n\n'))
    if func == 1:
        cadastrar()
        main()

    if func == 2:
        imagens()
        gerar_bancos()
        treinar()
        main()

    if func == 3:
        teste() 
        main()
        
    if func == 4:
        exit()


if __name__ == '__main__':
    main()