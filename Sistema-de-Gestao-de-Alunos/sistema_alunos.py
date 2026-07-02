import os

# Lista que armazenará os alunos
alunos = []

# Carregar alunos do arquivo
if os.path.exists("alunos.txt"):
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 3:
                aluno = {
                    "nome": dados[0],
                    "idade": dados[1],
                    "curso": dados[2]
                }
                alunos.append(aluno)

while True:
    print("\n" + "=" * 40)
    print("     SISTEMA DE GESTÃO DE ALUNOS")
    print("=" * 40)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Procurar aluno")
    print("4 - Editar aluno")
    print("5 - Excluir aluno")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # Cadastrar aluno
    if opcao == "1":

        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")

        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso
        }

        alunos.append(aluno)

        print("\n✅ Aluno cadastrado com sucesso!")

    # Listar alunos
    elif opcao == "2":

        if len(alunos) == 0:
            print("\nNenhum aluno cadastrado.")

        else:
            print("\n===== LISTA DE ALUNOS =====")

            for i, aluno in enumerate(alunos, start=1):
                print(f"\nAluno {i}")
                print(f"Nome : {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Curso: {aluno['curso']}")
                print("-" * 30)

    # Procurar aluno
    elif opcao == "3":

        nome_procurado = input("\nDigite o nome do aluno: ")

        encontrado = False

        for aluno in alunos:

            if aluno["nome"].lower() == nome_procurado.lower():

                print("\n✅ Aluno encontrado!")
                print(f"Nome : {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Curso: {aluno['curso']}")

                encontrado = True
                break

        if not encontrado:
            print("\n❌ Aluno não encontrado.")

    # Editar aluno
    elif opcao == "4":

        nome_procurado = input("\nDigite o nome do aluno que deseja editar: ")

        encontrado = False

        for aluno in alunos:

            if aluno["nome"].lower() == nome_procurado.lower():

                print("\nAluno encontrado!")

                aluno["nome"] = input("Novo nome: ")
                aluno["idade"] = input("Nova idade: ")
                aluno["curso"] = input("Novo curso: ")

                print("\n✅ Aluno atualizado com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("\n❌ Aluno não encontrado.")

    # Excluir aluno
    elif opcao == "5":

        nome_procurado = input("\nDigite o nome do aluno que deseja excluir: ")

        encontrado = False

        for aluno in alunos:

            if aluno["nome"].lower() == nome_procurado.lower():

                alunos.remove(aluno)

                print("\n✅ Aluno excluído com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("\n❌ Aluno não encontrado.")

    # Sair
    elif opcao == "6":

        with open("alunos.txt", "w", encoding="utf-8") as arquivo:

            for aluno in alunos:
                arquivo.write(
                    f"{aluno['nome']};{aluno['idade']};{aluno['curso']}\n"
                )

        print("\n💾 Dados salvos com sucesso!")
        print("👋 Sistema encerrado.")
        break

    else:
        print("\n❌ Opção inválida! Tente novamente.")
