class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def atualizar_telefone(self, telefone):
        self.telefone = telefone

    def atualizar_email(self, email):
        self.email = email

contato = Contato('Dolores', '991237514', 'dolores.gatinha@mail.com')
print(f'Este é o telefone de {contato.nome}: {contato.telefone}\n')
print(f'Este é o email de {contato.nome}: {contato.email}\n')
contato.atualizar_telefone('11991237514')
contato.atualizar_email('dolores.gatinha@gmail.com')
print(f'Este é o telefone atualizado de {contato.nome}: {contato.telefone}\n')
print(f'Este é o email atualizado de {contato.nome}: {contato.email}\n')
