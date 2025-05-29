# Sistema de Gerenciamento de Alunos e Cursos

**Nome:** Leonardo Ribeiro de Assis  
**RA:** 1995764  
**Turma:** 2° ADS - Turma C  


## Descrição do Projeto

Este projeto é um sistema de linha de comando (CLI) desenvolvido em Python com o objetivo de simular a administração básica de uma escola. O sistema permite gerenciar cursos, alunos e a relação entre eles através de um menu interativo no terminal.



## Como Executar o Sistema

-   **Requisitos**  
    Python 3.10 ou superior instalado  
    Terminal funcionando corretamente  
    Editor de texto/IDE  
    Permissão para executar arquivos .py no terminal  

1. Abra o terminal na pasta do projeto.

2. Execute o arquivo principal com:  
-   `python index.py` ou `py index.py`

3. Com o sistema agora iniciado você terá essas opções:

    Selecione um item  
    [1] - Listar Alunos  
    [2] - Listar Cursos  
    [3] - Adicionar um Curso  
    [4] - Adicionar um Aluno  
    [5] - Edição de Curso  
    [0] - Encerrar o programa  

    As funções serão chamadas de acordo com sua escolha

4. Escolha sua função:

    [1] Será retornado a você uma lista de todos alunos cadastrados  
    [2] Será retornado a você uma lista de todos os cursos cadastrados  
    [3] Fará perguntas para cadastrar o curso, assim:

        Qual a matéria do Curso: Estrutura de Dados  
        Qual a carga horária: 80  
        Qual o professor: Gustavo Marttos  
        - Curso Estrutura de Dados de código 10 adicionado com sucesso!

    [4] Fará perguntas para cadastrar o aluno, assim:  
        **Qual o nome do aluno:** Paulo  
        **Qual idade do aluno:** 17  
        **Qual série dele:** 3  
        **Qual período:** Manhã  
        - Aluno Paulo de código 9 adicionado com sucesso!

    > Perceba que sempre há a confirmação no final destas funções

    [5] Entrará em um outro menu focado exclusivamente para edição de cursos:

        Selecione uma opção  
        [0] - Voltar menu  
        [1] - Matricular Curso  
        [2] - Excluir curso  
        [3] - Listar uma sala do curso

        [1] **Ira perguntar se quer uma listagem de alunos em seguida opedira informações**

            Listar Alunos? [S/N]: n  
            **Qual aluno quer editar:** 2  
            Aluno escolhido: Bianca  
            **Qual curso quer adicionar (ou 'sair' para terminar)?** 5  
            Curso '5' adicionado.  
            **Qual curso quer adicionar (ou 'sair' para terminar)?** 6  
            Curso '6' adicionado.  
            **Qual curso quer adicionar (ou 'sair' para terminar)?** sair  

            >Sistema perguntara qual curso até usuario digitar sair, um número errado ou um curso já cadastrado no aluno
        
        [2] Irá perguntar o código do curso que deseja excluir e após isso vai retornar todos os alunos desmatriculados

           **Digite o código do curso:** 2  

            Curso 2 de matéria portugues foi deletado  
            Aluno Adriano desmatriculado do curso 2  
            Aluno Bianca desmatriculado do curso 2  
            Aluno Conceição desmatriculado do curso 2  
            Aluno Eduarda desmatriculado do curso 2  
            Aluno Hugo desmatriculado do curso 2  
            ------------------------------  
            Curso 2 desmatriculado com sucesso  
            ------------------------------
        
        [3] Irá perguntar que curso deseja ver e em seguida retornar os alunos matriculados nesse curso

            **Digite o código do curso que quer ver:** 3  

            Curso escolhido quimica  
            Adriano está matriculado nesse curso  
            Bianca está matriculado nesse curso  
            Conceição está matriculado nesse curso  
            Gabriela está matriculado nesse curso  
            ------------------------------  
            Pressione qualquer tecla para sair



## Principais funções

- **Menu**  
  Uma função que usa loop `while` e `match case` pra deixar o usuário escolher o que quer fazer. A única forma de sair é digitando 0, e isso já é mostrado ali direto no menu.  
  A função `edicaoCursos` é parecida também, segue a mesma lógica, mas é focada só na parte de edição de cursos. Quando sai dela, volta pro menu inicial porque ela tá dentro dele.  

- **anima_pontos**  
  Essa função é só pra dar um toque visual mais legal. Ela mostra três pontinhos com um tempinho entre eles, tipo "carregando...".

- **limpar_terminal**  
  Também é só pra deixar o visual melhor. Ela apaga tudo do terminal antes de mostrar a nova parte, assim não vira uma bagunça com tudo empilhado.  

- **msvcrt.getch()**  
  Essa é uma função pronta da biblioteca `msvcrt`. Ela trava o código até o usuário apertar alguma tecla. Eu usei isso junto com o limpar terminal, pra dar tempo da pessoa ler antes de mudar a tela.  

- **listagemCursos** e **listagemAlunos**  
  São usadas várias vezes no código, tanto quando o usuário chama como quando o sistema precisa mostrar alguma coisa. Elas percorrem os dicionários e usam `.values()` com um `for` pra listar certinho cada item cadastrado.

## Justificativa das Estruturas de Dados

- **Dicionários (`dict`)**  
  Usei dicionários pra representar tanto os cursos quanto os alunos, porque com eles dá pra guardar tudo usando um código como chave, tipo o ID. Isso facilita muito na hora de buscar, editar ou listar, já que eu acesso direto o que preciso.

- **Deque (collections.deque) dentro dos dicionários**  
  No lugar de listas comuns, usei o deque do Python dentro dos dicionários dos alunos pra guardar os cursos que cada um tá matriculado. O motivo disso é que o deque tem melhor performance quando precisa adicionar ou remover elementos, especialmente se for no começo ou no meio da estrutura, o que pode acontecer quando um aluno entra ou sai de um curso. Então é uma estrutura mais eficiente pra esse tipo de operação.

- **Laços `for` e `.values()`**  
  Quando vou listar os alunos ou os cursos, uso `for` com `.values()` pra pegar só os valores dos dicionários e poder mostrar certinho no terminal. Uso também a técnica de desempacotar, pra puxar todos os dados de uma vez e mostrar um por um.

- **Funções separadas**  
  Separei tudo em funções diferentes (tipo listar, adicionar, editar), porque isso deixa o código mais limpo, organizado, e bem mais fácil de mexer depois se quiser melhorar alguma parte. Também posso usar essas funções várias vezes sem ter que repetir código.
