
def artigos():
    mensagem = '''Linus teve poucas obras públicadas, as principais são:
    Principais obras publicadas: Just for fun: the story of na acidental revolutionary escrito por Linus Torvlds e David Diamond, 2001.
    The hacker ethic and the spirit of de information age, onde Linus participou/escreveu o prologo do livro.
    Além de participação em outras obras como Moody, Glyn: Rebel Code. Engl. the beginning of work: Rebel Code. Eng. Riikka Toivanen and Heikki Karjalainen. Nikkanen, Tuula: The Linux story. Satku, 2000.'''
    return mensagem


def citacoes():
    mensagem = "Linus teve algumas frases iconicas, as principais são:"
    "Na minha opinião, a Microsoft é muito melhor em fazer dinheiro do que Sistemas Operacionais."
    "Se a Microsoft faz aplicações para Linux que significa que eu ganhei."
    "Falar é fácil, me mostre o código."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
