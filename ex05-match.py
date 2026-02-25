dia_da_semana = int(input("Informe um dia da semana entre 1 e 7: "))
mes = int(input("Informe o mês do ano: "))

match dia_da_semana:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("Dia de semana do mês de Abril")
    case 6 | 7 if mes == 2:
        print("Fim de semana do mês de Fevereiro")
    case _:
        print("Dia inválido")
        