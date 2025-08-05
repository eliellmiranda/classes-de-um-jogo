# Classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Define o tipo de ataque baseado no tipo do herói
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo =='monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'um ataque desconhecido'

        # Exibe a mensagem final
        print(f'O {self.tipo} atacou usando {ataque}')

# Função principal
def iniciar_jogo():
    print('Bem-vindo ao criador de heróis!')
    herois = []

    # Pergunta quantos heróis serão criados
    qtd = int(input('Quantos heróis deseja criar?'))

    for i in range(qtd):
        print(f"\n Criando o herói #{i+1}")
        nome = input("Digite o nome do herói: ")
        idade = int(input("Digite a idade do herói: "))
        tipo = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ").lower()

        # Cria o objeto e adiciona à lista
        novo_heroi = Heroi(nome, idade, tipo)
        herois.append(novo_heroi)

    # Exibe os ataques de cada herói
    print("\n A BATALHA COMEÇOU!")
    for heroi in herois:
        heroi.atacar()

# Inicia o programa
iniciar_jogo()
