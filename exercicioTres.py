num = int(input("Digite um número inteiro: "))
div = num- 1
primo = True

while div > 1:
    if(num % div == 0):
        print("Não é um número primo")
        primo = False
        break
    
    div = div - 1
    
if primo:
    print("É um número primo")