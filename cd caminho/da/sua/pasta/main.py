from finance import FinanceManager

def menu():
    print("\n💰 RASTREADOR DE DESPESAS")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")
    print("4 - Listar transações")
    print("5 - Sair")

def main():
    finance = FinanceManager()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Valor da receita: "))
            descricao = input("Descrição: ")
            finance.add_income(valor, descricao)

        elif escolha == "2":
            valor = float(input("Valor da despesa: "))
            descricao = input("Descrição: ")
            finance.add_expense(valor, descricao)

        elif escolha == "3":
            print(f"\n💵 Saldo atual: R$ {finance.get_balance():.2f}")

        elif escolha == "4":
            finance.list_transactions()

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
