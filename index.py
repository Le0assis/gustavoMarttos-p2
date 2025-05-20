import time
import os
import msvcrt

cursos ={
    "1":{
        "materia": "matematica",
        "cargahoraria": 40,
        "professor": "Mauricio",
    },
    "2":{
        "materia": "portugues",
        "cargahoraria": 55,
        "professor": "prof",  
    },
    "3":{
        "materia": "quimica",
        "cargahoraria": 40,
        "professor": "prof",
    },
}

alunos = {
    "1":{
        "nome": "Adriano",
        "idade": 13,
        "serie": 6,
        "periodo": "Manhã",
    },
    "2":{
        "nome": "Bianca" ,
        "idade": 13 ,
        "serie": 7,
        "periodo": "Manhã",
        "matricula": []
    },
    "3":{
        "nome": "Conceição" ,
        "idade": 12,
        "serie": 6,
        "periodo": "Tarde",
        "matricula": [1, 2, 3]
    },
    

}

# atribuir cursos a alunos
# citar cursos de um aluno
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def anima_pontos():
    for i in range(3):
        print("." * (i+1), end='\r') # imprime os pontos e sobrescreve na linha
        time.sleep(0.5) # espera 0.5 segundos

def menu(alunos:dict, cursos: dict ) -> None:
    while True:
        print(
            "-" *30 ,
            "\n Selecione um item \n" \
            "[1] - Listar Alunos \n" \
            "[2] - Listar Cursos \n" \
            "[3] - Adicionar um Curso \n" \
            "[4] - Adicionar um Aluno \n" \
            "[0] - Encerrar o programa")
        
        
        resposta = int(input())
        match(resposta):

            case 0:
                anima_pontos()
                time.sleep(0.5)
                print("Encerrando programa")
                time.sleep(1)
                break

            case 1:
                anima_pontos()
                print("Listagem de alunos")
                time.sleep(1.5)
                limpar_terminal()
                listagemAlunos(alunos)

            case 2:
                anima_pontos()
                print("Listagem Cursos")
                time.sleep(1.5)
                listagemCursos(cursos)
            
            case 3:
                anima_pontos
                print("Adicionar um curso")
                time.sleep(1.5)
                adicionarCurso(cursos)
                
            case 4:
                anima_pontos()
                print("Adicionar um Aluno")
                time.sleep(1.5)
                adicionarAluno(alunos)


            case _:
                print("Numero invalido!")
                continue

        
            

#Lista todos os alunos
def listagemAlunos(lista: dict) -> None:
    limpar_terminal()
    for dados in lista.values():
        nome = dados["nome"]
        idade = dados["idade"]
        serie = dados["serie"]
        periodo = dados["periodo"]

        print("-" * 30)
        print(f"O nome é: {nome}")
        print(f"Tem {idade} anos")
        print(f"Está na {serie}ª série")
        print(f"Estuda de {periodo}")

    print("-" * 30)
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

# Adiciona um aluno
def adicionarAluno(lista:dict) -> None:
    id = str(len(lista) + 1)

    limpar_terminal()

    print("Qual o nome do aluno: ")
    nome = str(input())
    print("Qual idade do aluno: ")
    idade = int(input())
    print("Qual serie dele: ")
    serie = int(input())
    print("Qual periodo: ")
    periodo = str(input())

    lista.update({
        id:{
            "nome": nome,
            "idade": idade,
            "serie": serie,
            "periodo": periodo,
        }
    })
    print(f"Aluno {nome} de codigo {id} adicionado com sucesso! \n")
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Lista todos os cursos
def listagemCursos(lista: dict) -> None:
    limpar_terminal()
    for dados in lista.values():
        materia = dados["materia"]
        cargaHoraria = dados["cargahoraria"]
        professor = dados["professor"]


        print("-" * 30)
        print(f"A materia do curso é: {materia}")
        print(f"Tem {cargaHoraria} horas de aula")
        print(f"Com o professor {professor}")

    print("-" * 30)
    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Adicionar um Curso
def adicionarCurso(lista:dict ) -> None:

    id = str(len(lista) + 1)

    limpar_terminal()

    print("Qual a materia do Curso: ")
    materia = str(input())
    print("Qual a carga horaria: ")
    cargahoraria = int(input())
    print("Qual o professor: ")
    professor = str(input())

    lista.update({
        id: {
            "materia": materia,
            "cargahoraria": cargahoraria,
            "professor": professor,
        }
    })
    print(f"Curso {materia} de codigo{id} adicionado com sucesso! \n")

    print("Pressione qualquer tecla para sair")
    msvcrt.getch()

#Menu Cursos
def edicaoCursos(alunos:dict, cursos:dict):

    while True:

        resposta = int(input(
            "Selecione uma opção" \
            "[0] - Voltar menu" \
            "[1] - Matricular Curso" \
            "[2] - desmatricular do Curso" \
            "[3] - Excluir curso" \
            "[4] - Listar cursos e seus alunos"))
        
        match (resposta):
            case 0 :
                break

            case 1:
                anima_pontos()
                print("Matricular Curso")
                time.sleep(1.5)
                limpar_terminal()
                matricularCurso(alunos, cursos)

            case _:
                print("Escolha invalída")
                pass

#Mastricular cursos
def matricularCurso(alunos, cursos):
    
    #Listar Alunos
    while True:
        print("Listar Alunos? [S/N]: ")
        resposta = str(input()).upper()

        if resposta == 'N':
            break
        elif resposta== 'S':
            listagemAlunos(alunos)
            break
        else:
            print("Resposta invalida!")
    #Escolha de Aluno
    while True:
        print("Qual aluno quer editar: ")
        idAluno = str(input())
        if idAluno not in alunos:
            print("Numero invalido")
            pass
        else:
            escolhido = alunos.get(idAluno)
            print(escolhido)
            print(f"Aluno escolhido {escolhido["nome"]} \n")
            time.sleep(1)
            break
    #Adicionar Cursos
    while True:
        idCurso = str(input("Qual curso quer adicionar (ou 'sair' para terminar)? ").strip())
        if idCurso.lower() == 'sair':
            break
        elif idCurso not in cursos:
            print("Numero invalido")
            break

        # Se matricula ja tem um curso existente o programa não consegue ler
        escolhido.setdefault('matricula', [])
        escolhido["matricula"].append(idCurso)
        print(f"curso '{idCurso}' adicionado.")
        print(escolhido["matricula"])
        break

def removerCurso (alunos:dict, cursos:dict):
    idCurso = str(input("Digite o código do curso: "))

    valor_removido = cursos.pop('idCurso')

    print(f"Curso {idCurso} de matéria {valor_removido["materia"]} foi deletado")
    

# listagemAlunos(alunos)
# listagemCursos(cursos)
# adicionarCurso(cursos)
# adicionarAluno(alunos)

menu(alunos, cursos)

# matricularCurso(alunos, cursos)

# removerCurso(alunos, cursos)