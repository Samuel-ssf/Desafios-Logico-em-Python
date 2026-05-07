nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >=7:
    print(f"Sua média é: {media}, Meus parabéns, você foi aprovado!")
elif media >= 5:
    print(f"Sua média é: {media}, Você está de Recuperação!")
else:
    print(f"Sua média é: {media}, Infelismente voce foi reprovado, preciso que se esforce mais!")
