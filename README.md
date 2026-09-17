NotaFácil 📚✅

Uma calculadora simples e prática para ajudar professores a calcular médias, identificar situação de recuperação e organizar as notas de todos os alunos em um único lugar.

✨ Funcionalidades
Cálculo automático da média entre duas notas
Identificação da situação do aluno: Aprovado, Recuperação ou Reprovado
Cálculo da média final após a recuperação
Validação de entradas (impede notas inválidas ou fora do intervalo de 0 a 10)
Suporte para calcular vários alunos na mesma execução
Armazenamento das notas em um arquivo CSV (notas_alunos.csv), funcionando como um pequeno banco de dados que preserva o histórico entre execuções
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   git clone https://github.com/Maxwell80214/NotaFacil.git
   cd NotaFacil
-----------------------------------------------------------------------------
   python calculadora_notas.py
-------------------------------------
Olá, professor(a)! Bem-vindo(a) à calculadora de notas!

Digite o nome do aluno: Maxwell de Oliveira
Digite a primeira nota (0 a 10):8
Digite a segunda nota (0 a 10):7
Parabéns, Maxwell de Oliveira! Você foi aprovado(a) com média 7.50.

Deseja calcular a nota de outro aluno? (s/n): s

Digite o nome do aluno: Ana Beatriz
Digite a primeira nota (0 a 10):5
Digite a segunda nota (0 a 10):6
Ana Beatriz, Você está de recuperação com média 5.50.
Digite a nota da recuperação (0 a 10):8
Parabéns, Ana Beatriz! Você foi aprovado(a) com média final 6.80.

Deseja calcular a nota de outro aluno? (s/n): n

--- Alunos cadastrados ---
Maxwell de Oliveira = 7.50 (Aprovado(a))
Ana Beatriz = 6.80 (Aprovado(a) na recuperação)
--------------------------

Dados salvos em "notas_alunos.csv". Encerrando a calculadora de notas. Até a próxima!
