#Exercicio 4

nome=input("Digite seu nome: ")
materias=5
soma = 0
for i in range(materias):
    nota=int(input(f"Digite sua {i+1}° nota: "))
    soma += nota
media =(soma) / (materias)

if media >=5:
    print(f"Sua média é: {media}, e você está APROVADO!")
elif media >= 2.5 and media <= 5:
    print(f"Sua média é: {media}, e você está de RECUPERAÇÃO!")
elif media < 2.5:
    print(f"Sua média é: {media}, e você está REPROVADO!")
else:
    print("Digite um valor correto.")
