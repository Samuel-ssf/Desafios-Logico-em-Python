def validar_cpf(): # exemplo: eu criei uma maquina, quando eu usar essa função, ela vai chamr tudo que está dentro dela

    tentativas = 3  # número máximo de tentativas

    while tentativas > 0: #enquanto tiver tentativas, ele vai repetir
        cpf = input("Digite seu CPF (apenas números): ").strip() # esse strip ele tira os espaços 

        # valida tamanho e se não é tudo igual
        if len(cpf) != 11 or not cpf.isdigit() or cpf == cpf[0] * 11: # Aqui ele perguta, tem 11 números?, Só tem números?, É tudo igual?
            print("CPF inválido! Tente novamente.\n")

            tentativas -= 1 # a cada erro do usuário, diminui uma tentaiva

            print(f"Tentativas restantes: {tentativas}\n")
            continue #Volta pro começo do loop, tenta de novo

        # PRIMEIRO NÚMERO
        soma = 0  # inicia a variável soma com 0 (vai acumular os cálculos)
        peso = 10  # peso inicial usado na multiplicação (começa em 10)

        for numero in cpf[:9]:  # percorre os 9 primeiros dígitos do CPF
            soma += int(numero) * peso  # multiplica o número atual pelo peso e soma ao total
            peso -= 1  # diminui o peso a cada repetição (10, 9, 8... até 2)

        resto = soma % 11  # pega o resto da divisão da soma por 11
        primeiro_numero = 11 - resto  # calcula o primeiro dígito verificador

        if primeiro_numero >= 10:  # se o resultado for 10 ou 11
            primeiro_numero = 0  # o dígito vira 0 (regra do CPF)

        # SEGUNDO NÚMERO
        soma = 0  # reinicia a soma para calcular o segundo dígito
        peso = 11  # agora o peso começa em 11

        for numero in cpf[:9]:  # percorre novamente os 9 primeiros dígitos
            soma += int(numero) * peso  # multiplica cada número pelo peso
            peso -= 1  # diminui o peso (11, 10, 9... até 3)

        soma += primeiro_numero * 2  # adiciona o primeiro dígito verificador multiplicado por 2

        resto = soma % 11  # calcula o resto da divisão por 11
        segundo_numero = 11 - resto  # calcula o segundo dígito verificador

        if segundo_numero >= 10:  # se for 10 ou 11
            segundo_numero = 0  # ajusta para 0 (regra do CPF)

        #  VERIFICAÇÃO FINAL
        if int(cpf[9]) == primeiro_numero and int(cpf[10]) == segundo_numero: 
            print("CPF válido!")
            return  # sai da função quando acerta
        else:
            print("CPF inválido!")
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}\n")

    # se acabar as tentativas
    print("Você excedeu o limite de tentativas!")

validar_cpf()