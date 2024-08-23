import os
import time

from modelos.options import Lista


def title(text):
    os.system("cls" if os.name == "nt" else "clear")
    linha = "*" * (len(text))
    print(linha)
    print(text)
    print(linha)
    print()


def options():
    title("Aplicação CRUD para CSV")
    print("1.  Inserir local do arquivo.")
    print("2.  Mostrar o que contém.")
    print("3.  Procurar informação.")
    print("4.  Editar.")
    print("5.  Sair.\n")


def main():
    local_arquivo = ""
    while True:
        options()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            try:
                os.system("cls" if os.name == "nt" else "clear")
                local_arquivo = input("Digite o caminho do arquivo CSV: ")
                Lista.load_contacts(local_arquivo)
                print("Arquivo carregado com sucesso!")
            except:
                print("Arquivo não encontrado.")
        elif escolha == '2':
            Lista.list_contacts()
        elif escolha == '3':
            nome = input("Digite o primeiro nome para procurar: ")
            sobrenome = input("Digite o sobrenome: ")
            contato = Lista.find_contact(nome, sobrenome)
            if contato:
                print(f"Contato encontrado: {contato}")
            else:
                print("Contato não encontrado.")
        elif escolha == '4':
            nome = input("Digite o primeiro nome do contato a ser editado: ")
            sobrenome = input("Digite o sobrenome do contato: ")
            contato = Lista.find_contact(nome, sobrenome)
            if contato:
                print(f"Editando contato: {contato}")
                novo_nome = input("Novo primeiro nome (ou Enter para manter): ")
                novo_sobrenome = input("Novo sobrenome (ou Enter para manter): ")
                novo_email = input("Novo email (ou Enter para manter): ")
                novo_telefone = input("Novo telefone (ou Enter para manter): ")
                contato.update_contact(novo_nome, novo_sobrenome, novo_email, novo_telefone)
                print("Contato atualizado com sucesso!")
            else:
                print("Contato não encontrado.")
        elif escolha == '5':
            opcao = input(f"Deseja salvar as alterações ? \n(S/N): ").lower()
            if local_arquivo:
                if opcao == "s":
                    Lista.save_contacts(local_arquivo)
            print("Saindo da aplicação...")
            time.sleep(3)
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
