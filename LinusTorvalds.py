def resumo():
    mensagem = """
    Linus Benedict Torvalds é um programador e engenheiro de software finlandês, nascido no dia 28 de dezembro de 1969, em Helsinque, na Finlândia.
    Ele é mais conhecido por ser o criador do sistema operacional Linux, um dos projetos de código aberto mais importantes da história da computação. 
    Torvalds é considerado uma das figuras mais influentes no mundo da tecnologia, devido ao impacto do Linux no desenvolvimento de servidores, dispositivos móveis e sistemas de computação em geral.
    """
    return mensagem


def doutorado():
    mensagem = """
    Linus Torvalds não completou um doutorado formal, mas teve uma trajetória acadêmica notável. Ele estudou ciência da computação na Universidade de Helsinque, onde iniciou o desenvolvimento do Linux.
    Durante sua graduação, Torvalds foi inspirado pela falta de um sistema operacional gratuito para PCs. O Linux começou como um projeto pessoal, e com o tempo, tornou-se um sistema utilizado por empresas e indivíduos ao redor do mundo.
    Mesmo sem um doutorado, sua contribuição à ciência da computação foi revolucionária e é considerada uma das mais significativas da história recente.
    """
    return mensagem


def contribuicoes():
    mensagem = """
    Linus Torvalds é mais conhecido por ter criado o Linux, um sistema operacional de código aberto que serve como base para milhões de servidores, dispositivos móveis e sistemas em todo o mundo.
    Sua contribuição vai além do código, pois ele criou uma comunidade global de desenvolvedores que trabalham colaborativamente no Linux, garantindo que ele continuasse a evoluir.
    Além do Linux, Torvalds também é responsável pelo desenvolvimento do sistema de controle de versão Git, que revolucionou o modo como os desenvolvedores colaboram e gerenciam o código.
    Sua influência na forma como o software é desenvolvido, distribuído e utilizado continua a moldar a indústria de tecnologia até hoje.
    """
    return mensagem


def artigos():
    mensagem = """
    Linus teve poucas obras publicadas, as principais são:
    - Just for Fun: The Story of an Accidental Revolutionary (Linus Torvalds e David Diamond, 2001).
    - The Hacker Ethic and the Spirit of the Information Age (participação no prólogo).
    - Rebel Code: Linux and the Open Source Revolution (Glyn Moody).
    - Além de outras contribuições para artigos e projetos acadêmicos.
    """
    return mensagem


def citacoes():
    mensagem = """
    Linus teve algumas frases icônicas, as principais são:
    - "Na minha opinião, a Microsoft é muito melhor em fazer dinheiro do que sistemas operacionais."
    - "Se a Microsoft faz aplicações para Linux, isso significa que eu ganhei."
    - "Falar é fácil, me mostre o código."
    """
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Linus Torvalds.\n")

continuar = True
while continuar:

    try:
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
            print("\n1 - Resumo")
            mensagem = resumo()

        elif opcao == 2:
            print("\n2 - Doutorado")
            mensagem = doutorado()

        elif opcao == 3:
            print("\n3 - Contribuições")
            mensagem = contribuicoes()

        elif opcao == 4:
            print("\n4 - Principais Artigos")
            mensagem = artigos()

        elif opcao == 5:
            print("\n5 - Citações")
            mensagem = citacoes()

        elif opcao == 6:
            mensagem = sair()
            continuar = False

        else:
            mensagem = erro()

        print(mensagem)

    except ValueError:
        print("\nPor favor, digite um número válido!")
