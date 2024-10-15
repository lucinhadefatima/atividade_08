#EXIBIR MENU
def exibir_menu():
    print("0 - sair do programa.")
    print("1 - verificar  maioridade.")
    print("2- sair caucular IMC.")
    
def verificar_maioridade(nome, idade):
    if idade >= 10:
        return f"{nome} e maior de idade."
    else:
        return f"{nome} e maior de idade"
    
caucular_imc = lambda peso,altura: peso/(altura**2)