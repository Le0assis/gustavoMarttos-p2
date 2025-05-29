# Sistema de Gerenciamento de Alunos e Cursos

**Nome:** Leonardo Ribeiro de Assis  
**RA:** 1995764  
**Turma:** 2° ADS - Turma C  


## Descrição do Projeto

Este projeto é um sistema de linha de comando (CLI) desenvolvido em Python com o objetivo de simular a administração básica de uma escola. O sistema permite gerenciar cursos, alunos e a relação entre eles através de um menu interativo e amigável no terminal.



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

    1. Será retornado a você uma lista de todos alunos cadastrados  
    2. Será retornado a você uma lista de todos os cursos cadastrados  
    3. Fará perguntas para cadastrar o curso, assim:

        **Qual a matéria do Curso:** Estrutura de Dados  
        **Qual a carga horária:** 80  
        **Qual o professor:** Gustavo Marttos  
        - Curso Estrutura de Dados de código 10 adicionado com sucesso!

    4. Fará perguntas para cadastrar o aluno, assim:  
        **Qual o nome do aluno:** Paulo  
        **Qual idade do aluno:** 17  
        **Qual série dele:** 3  
        **Qual período:** Manhã  
        - Aluno Paulo de código 9 adicionado com sucesso!

    > Perceba que sempre há a confirmação no final destas funções

    5. Entrará em um outro menu focado exclusivamente para edição de cursos:

        Selecione uma opção  
        [0] - Voltar menu  
        [1] - Matricular Curso  
        [2] - Excluir curso  
        [3] - Listar uma sala do curso

        1. Ira perguntar se quer uma listagem de alunos em seguida opedira informações
            **Listar Alunos? [S/N]:** n  
            **Qual aluno quer editar:** 2  
            **Aluno escolhido:** Bianca  
            **Qual curso quer adicionar (ou 'sair' para terminar)?** 5  
            **Curso '5' adicionado.**  
            **Qual curso quer adicionar (ou 'sair' para terminar)?** 6  
            **Curso '6' adicionado.**  
            **Qual curso quer adicionar (ou 'sair' para terminar)?** sair 

            >Sistema perguntara qual curso até usuario digitar sair, um numero errado ou um curso ja cadastrado no aluno
        
        2. Ira perguntar o código do curso que deseja excluir e após isso vai retornar todos os alunos desmatriculados

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
        
        3. Ira perguntar que curso deseja ver e em seguida retrnar os alunos matriculados nesse curso

            **digite o código do curso que quer ver:** 3

            Curso escolhido quimica
            Adriano está matriculado nesse curso
            Bianca está matriculado nesse curso
            Conceição está matriculado nesse curso
            Gabriela está matriculado nesse curso
            ------------------------------
            Pressione qualquer tecla para sair



## Principais funções

-   **Menu** Uma função que usando loop While e match case permite ao usuario escolher sua ação, usnica forma de sair é digitando 0
opção que a própria função mostra
    A função **edicaoCursos** é bem parecida também, tendo a mesma sintaxe, a diferença é que nessa função ao sair dela voltara ao menu inicial por ta hospedada nela
essa função serve para dar opções mais voltadas a edição de cursos

- **anima_pontos**, Essa função é usada para melhorar a estética e a imersão do programa. Ela imprime três pontos sequenciais com pequeno atraso entre eles, criando um efeito de "carregando" 

- **limpar_terminal**, outra unção só para estética, é chamada em toda escolha de funcionalidade no código, ela limpa todo o terminal então não fica um chat inteiro em cascata, fica bem melhor de se ver

- **msvcrt.getch()** uma função pronta de uma biblioteca no python, ela é a chave pra outras duas funções citadasantes, essa função congela todo o código até ter a entrada de alguma tecla do teclado (Qualquer uma), ja que usei uma função para limpar o terminal precisava de uma para "esperar liberação do usuario", assim fazendo ele ter que apertar uma tecla para prosseguir com o código

- **listagemCursos** e **listagemAlunos** outras duas funções principais, são chamadas diversas vezes no decorrer do código, sendo chaada pelo usuario ou não, serve para listar cursos e alunos respectivamente, como o próprio nome delas diz, por serem estrutura de dados como dicionarios, usei um for para percorrer cada item e value() para retornar o valor desses items, então com a desempacotação exibo os dados de cada um individualmente