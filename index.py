import time
import os

cursos ={
    "01":{
        "materia": "matematica",
        "cargahoraria": 40,
        "professor": "Mauricio",
    },
    "02":{
        "materia": "portugues",
        "cargahoraria": 55,
        "professor": "prof",  
    },
    "03":{
        "materia": "quimica",
        "cargahoraria": 40,
        "professor": "prof",
    },
}

alunos = {
    "01":{
        "nome": "Adriano",
        "idade": 13,
        "serie": 6,
        "periodo": "Manhã"
    },
    "02":{
        "nome": "Bianca" ,
        "idade": 13 ,
        "serie": 7,
        "periodo": "Manhã",
    },
    "03":{
        "nome": "Conceição" ,
        "idade": 12,
        "serie": 6,
        "periodo": "Tarde",
    },
    

}
# Adicionar: alunos e cursos
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

            case 1:
                anima_pontos()
                print("Listagem de alunos")
                time.sleep(1)
                limpar_terminal()
                listagemAlunos(alunos)


            case _:
                print("Numero invalido!")
                continue

        
            


def listagemAlunos(lista: dict) -> None:
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

def adicionarAluno(lista:dict) -> None:
    id = str(len(lista) + 1)

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
    print(f"Aluno {nome} adicionado com sucesso!")

def listagemCursos(lista: dict) -> None:
    for dados in lista.values():
        materia = dados["materia"]
        cargaHoraria = dados["cargahoraria"]
        professor = dados["professor"]


        print("-" * 30)
        print(f"A materia do curso é: {materia}")
        print(f"Tem {cargaHoraria} horas de aula")
        print(f"Com o professor {professor}")

def adicionarCurso(lista:dict ) -> None:
    id = str(len(lista) + 1)

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
    print(f"Curso {materia} adicionado com sucesso!")

# listagemAlunos(alunos)
# listagemCursos(cursos)
# adicionarCurso(cursos)
# adicionarAluno(alunos)

menu(alunos, cursos)