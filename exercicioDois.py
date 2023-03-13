mes = int(input("Digite o número do mês entre 1 e 12: "))
    
while True:
    if mes == 1:
        print("janeiro")
    elif mes == 2:
        print("fevereiro")
    elif mes == 3:
        print("março")
    elif mes == 4:
        print("abril")
    elif mes == 5:
        print("maio")
    elif mes == 6:
        print("junho")
    elif mes == 7:
        print("julho")
    elif mes == 8:
        print("agosto")
    elif mes == 9:
        print("setembro")
    elif mes == 10:
        print("outubro")
    elif mes == 11:
        print("novembro")
    elif mes == 12:
        print("dezembro")
    else:
        mes >= 13
        print("Mês inválido.")
        
    repita = int(input("\nQuer verificar outro mês?\n\n 1-sim\n 2-não\n\n Digite aqui: "))
    
    if repita == 2:
        break