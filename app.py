from modulo import *

#inicio do programa
if__name__ == "__main__": # insira este comando para proteger o codigo
while True:

    nome = input("imforme seu nome:")
    exibir_menu()
    opcao = input("opcao desejada:")
    match opcao:

        case "0":
            break
        case "1":
                idade = int(input("imforme sua idade:"))
                print(verificar_maioridade(nome,idade))
                continue
        case "2":
            peso = float(input("imforme o peso em kg:").reaplace(",","."))
            altura = float(input("informe a altura em metros:").reaplace(",","."))
            print(caucular_imc(peso,altura))
            continue
        case _:
            print("opcao invalida.")

            continue




