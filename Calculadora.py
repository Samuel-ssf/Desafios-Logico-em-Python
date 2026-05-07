'''print("Seja bem Vindo ao Sozia Club\n")

altura = float(input("Digite sua altura: "))
if altura >= 2.05:
    print("Aprovado")
else:
    print("Você não foi aprovado")'''

print("Bem vindo Calculadora!\nEscolha uma opção: ")

while True:
    opcao = int(input(" 1: Somar:\n 2: Subtrair:\n 3: Multiplicar:\n 4: Dividir:\n"))
    if opcao in (1,2,3,4):
        break
    print("Digite uma Opção valida!")

a = float(input("Digite a primeira valor: "))
b = float(input("Digite a segunda valor: "))

if opcao == 1:
    resultado = a + b
    print(f"O valor da sua soma é: {resultado}")
elif opcao == 2:
    resultado = a - b
    print(f"O valor da subtração é: {resultado}")
elif opcao == 3:
    resultado = a * b 
    print(f"O valor da Multiplicação é: {resultado}")
elif opcao == 4:
    resultado = a / b 
    print(f"O valor da Divisão é: {resultado}")
else:
    print("Opção Invalida")





    









