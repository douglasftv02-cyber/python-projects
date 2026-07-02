# Calculadora Simples

print("=" * 30)
print("     CALCULADORA")
print("=" * 30)

while True:
    print("\nEscolha uma operação:")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")

    opcao = input("Digite a opção: ")

    if opcao == "5":
        print("Calculadora encerrada.")
        break

    if opcao in ("1", "2", "3", "4"):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {num1 + num2}")

        elif opcao == "2":
            print(f"Resultado: {num1 - num2}")

        elif opcao == "3":
            print(f"Resultado: {num1 * num2}")

        elif opcao == "4":
            if num2 == 0:
                print("Erro: Não é possível dividir por zero.")
            else:
                print(f"Resultado: {num1 / num2}")

    else:
        print("Opção inválida!")
