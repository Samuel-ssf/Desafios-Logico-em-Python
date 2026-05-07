'''valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: ")) 
soma = (valor1 + valor2)
print(f" soma dos valores é: {soma}")'''

contador = 0
resposta = 0
while resposta != 10:
    resposta =  int (input("Qual s soma de 5 + 5? Digite sua resposta: "))
    if resposta == 10:
        print("Resposta Correta!")
    else:
        print("Resposta Incorreta")
        contador = contador + 1
        print(contador)

        if contador == 3:
            print("Você Excedeu o limite de tentativas!")
            break














































