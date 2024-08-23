import os
import csv


class Lista:
    contatos = []

    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.email = email.lower()
        self.telefone = telefone
        Lista.contatos.append(self)

    def __str__(self):
        return f"{self.nome} | {self.sobrenome} | {self.email} | {self.telefone}"

    @classmethod
    def list_contacts(cls):
        os.system("cls" if os.name == "nt" else "clear")
        print('Nome Completo           | Email                     | Telefone')
        for contato in cls.contatos:
            print(
                f'{(contato.nome + " " + contato.sobrenome).ljust(25)}| {contato.email.ljust(25)} | {contato.telefone}')

    @classmethod
    def load_contacts(cls, file_path):
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                Lista(linha['nome'], linha['sobrenome'], linha['email'], linha['telefone'])


    @classmethod
    def save_contacts(cls, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['nome', 'sobrenome', 'email', 'telefone'])
            for contato in cls.contatos:
                writer.writerow([contato.nome, contato.sobrenome, contato.email, contato.telefone])

    @classmethod
    def find_contact(cls, nome, sobrenome=None):
        for contato in cls.contatos:
            if contato.nome.lower() == nome.lower() and (
                    sobrenome is None or contato.sobrenome.lower() == sobrenome.lower()):
                return contato

    @classmethod
    def remove_contact(cls, nome, sobrenome=None):
        contato = cls.find_contact(nome, sobrenome)
        if contato:
            cls.contatos.remove(contato)
            return True
        return False

    def update_contact(self, nome=None, sobrenome=None, email=None, telefone=None):
        if nome:
            self.nome = nome.title()
        if sobrenome:
            self.sobrenome = sobrenome.title()
        if email:
            self.email = email.lower()
        if telefone:
            self.telefone = telefone
