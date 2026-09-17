#Projeto Desenvolvido para ajudar professores com notas de alunos, calculando médias e notas finais.
#Versão melhorada: validação de entradas + suporte a múltiplos alunos.


def ler_float(mensagem, minimo=0, maximo=10):
    """Lê um número float do usuário, validando o formato e o intervalo permitido."""
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
        except ValueError:
            print(f'Entrada inválida! Digite um número (ex: 7.5).')
            continue

        if valor < minimo or valor > maximo:
            print(f'A nota deve estar entre {minimo} e {maximo}. Tente novamente.')
            continue

        return valor


def calcular_situacao(nome_aluno):
    """Calcula a situação final de um aluno com base nas notas informadas."""
    nota1 = ler_float('Digite a primeira nota (0 a 10):')
    nota2 = ler_float('Digite a segunda nota (0 a 10):')
    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f'Parabéns, {nome_aluno}! Você foi aprovado(a) com média {media:.2f}.')
    elif media >= 5:
        print(f'{nome_aluno}, Você está de recuperação com média {media:.2f}.')
        nota_recuperacao = ler_float('Digite a nota da recuperação (0 a 10):')
        media_final = (media + nota_recuperacao) / 2

        if media_final >= 7:
            print(f'Parabéns, {nome_aluno}! Você foi aprovado(a) com média final {media_final:.2f}.')
        else:
            print(f'{nome_aluno}, sinto muito! Você foi reprovado(a), repetindo o ano, com média final {media_final:.2f}.')
    else:
        print(f'{nome_aluno}, sinto muito! Você foi reprovado(a) direto, com média {media:.2f}.')


def main():
    print('Olá, professor(a)! Bem-vindo(a) à calculadora de notas!\n')

    continuar = True
    while continuar:
        nome_aluno = input('Digite o nome do aluno: ').strip()
        while nome_aluno == '':
            print('O nome não pode ficar em branco.')
            nome_aluno = input('Digite o nome do aluno: ').strip()

        print()  # linha em branco pra organizar a leitura
        calcular_situacao(nome_aluno)
        print()

        resposta = input('Deseja calcular a nota de outro aluno? (s/n): ').strip().lower()
        continuar = resposta == 's'
        print()

    print('Encerrando a calculadora de notas. Até a próxima!')


if __name__ == '__main__':
    main()


#Projeto desenvolvido por Maxwell De Oliveira Carvalho, Estudante de Engenharia de Software na Universidade Potiguar.