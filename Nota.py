import os
os.system('cls')

print('Sistema de notas')

def Resultado(Nome, Notap1, Notap2):
    Media = (Notap1 + Notap2)/2
    os.system('cls')
    if Media >= 7:
        print('Nome:', Nome)
        print('Média:', Media)
        print('Situação: Aprovado')
        if Media >= 9:
            print('Conceito: A')
        elif 7 <= Media < 9:
            print('Coneito: B')
    elif Media < 6:
        print('Nome:', Nome)
        print('Média:', Media)
        print('Situação: Reprovado')
        print('Conceito: D')
    else:
        print('Nome:', Nome)
        print('Média:', Media)
        print('Situação: Recuperação')
        print('Conceito: C')
    return Media

#Isalpha serve para indicar que uma carcterie não é string.
while True:
    try:
        Nome = input('Digite o nome do aluno: ')
        if Nome.isalpha() == True:
            break
        else:
            print('o nome deve conter apenas letras. Digite novamente.')
    except ValueError:
        print('Digite apenas letras')

# Try funciona da mesma forma que o If e o except serve para especificar uma variavél.
while True:
    try:
        Notap1 = float(input('Digite a primeira nota: '))
        if 0 < Notap1 <= 10:
            break
        else:
            print('A nota deve ser entre 0 e 10. digite novamente.')
    except ValueError:
        print('Digite um valor númerico')

#ValueError é usada para indicar algo "anormal".
while True:
    try:
        Notap2 = float(input('Digite a segunda nota: '))
        if 0 < Notap2 <= 10:
            break
        else:
            print('A nota deve ser entre 0 e 10. digite novamente.')
    except ValueError:
        print('Digite um valor númerico')

os.system('cls')

Resultado(Nome, Notap1, Notap2)
