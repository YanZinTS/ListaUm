num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))
result = int(input("Escolha a operação desejada:\n\n 1 - soma\n 2- subtração\n 3- divisão\n 4- multiplicação\n 5- potência\n\n Digite aqui: "))

def soma(a,b):
    return a + b

def subtrai(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiplica(a,b):
    return a * b

if result == 1:
    print(soma(num1,num2))
    print ("É valido")
elif result == 2:
    print(subtrai(num1,num2))
    print ("É valido")
elif result == 3:
    print(divide(num1,num2))
    print ("É valido")
elif result == 4:
    print(multiplica(num1,num2))
    print ("É valido")
else:
    print("Opção inválida")