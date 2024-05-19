class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}' 

    def aniversario(self):
        print(f'Feliz aniversário {self.nome}!! Parábens pelos {self.idade + 1}')
    
    def saudacao(self):
        print(f'Saudações {self.nome}. Fico feliz em parabenizar um {self.profissao} tão competente!')

pessoa1 = Pessoa('Luis', 24, 'Desenvolvedor')
pessoa1.aniversario()
pessoa1.saudacao()
print(pessoa1)
