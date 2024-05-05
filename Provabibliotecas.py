alunos_dict = {}  

def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    

    alunos_dict[matricula] = nome
    print(f"Aluno adicionado com sucesso!\n")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno que deseja remover: ")

    if matricula in alunos_dict:
        del alunos_dict[matricula]
        print("Aluno removido com sucesso!\n")
    else:
        print("Matrícula não encontrada. Nenhum aluno removido.\n")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")

    if matricula in alunos_dict:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos_dict[matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso!\n")
    else:
        print("Matrícula não encontrada. Nenhum aluno atualizado.\n")

def VerAlunos():
    if not alunos_dict:
        print("Nenhum aluno cadastrado.\n")
    else:
        print("Lista de alunos:")
        for matricula, nome in alunos_dict.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
        print()  

