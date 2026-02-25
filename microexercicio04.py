opcao = int(input("Informe a opção desejada: "))

match opcao:
    case 1:
        print("Café")
    case 2: 
        print("Chá")
    case 3:
        print("Suco")
    case _:
        print("Opção inválida")