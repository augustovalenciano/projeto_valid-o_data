print("o ano é bisesto?: ")
v = input()
print("informe o mes: ")
mes = int(input())
print("informe o dia: ")
dia = int(input())
print("informe o ano que você nasceu: ")
ano = int(input())

def verifica_mes(b,m,d):
    if b == "sim":
        if m == 2:
            if d > 29:
                print("nao existe!!!")
            else:
                print("data correta")
                tira_idade(ano)
        elif m > 12 or d > 31:
            print("data incorreta")
        else:
            print("data correta")
            tira_idade(ano)
    elif b == "nao":
        if m == 2 and d > 28:
            print("nao existe")
        elif m > 12 or d > 31:
            print("nao existe")
        else:
            print("data correta")
            tira_idade(ano)

def tira_idade(a):
    global mes,dia
    idade = 2022 - a
    print(f"você nasceu no ano de {a} no mes {mes} no dia {dia} e você possui {idade} anos")

verifica_mes(v,mes,dia)