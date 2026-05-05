import pyperclip
import random
import string
while True:
    senha = ""

    # Escolha do usuario --
    while True:
        escolha = input("Deseja utilizar apenas letras na geração da senha? S/N : ").upper()
        if escolha in ["S", "N"]:
                break
        print("ERRO! ESCOLHA S/N")
        
    while True:
        try:
            caracteres = int(input("Quantos caracteres deseja que a senha possua (1 - 20) : "))
            if 1 <= caracteres <= 20:
                break
            else:
                print("ERRO! DIGITE UM NUMERO MENOR QUE 20")
        except ValueError:
            print("ERRO! DIGITE UM NUMERO INTEIRO MENOR QUE 20")
             

    # Atribui uma variavel valores aleatorios de digitos, letras e pontuações de acordo com a escolha do usuario --
    if escolha == "N":
            conjunto = string.ascii_letters + string.digits + string.punctuation
            for i in range(caracteres):
                senha += random.choice(conjunto)
    elif escolha == "S":
            conjunto = string.ascii_letters
            for i in range(caracteres):
                senha += random.choice(conjunto)

        # Valor de saida da senha --
    print("Sua senha de {} caracteres é : {}".format(caracteres, senha))
    pyperclip.copy(senha)
    print("Senha copiada para área de transferência!")
    continuar = input("Deseja gerar mais uma senha? S/N : ").upper()
    if continuar == "N":
        print("FIM DO PROGRAMA!")
        print("OBRIGADO POR UTILIZAR!")
        break
   