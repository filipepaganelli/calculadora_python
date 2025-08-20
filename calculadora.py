
#Funções da operações
def somar(a,b):
    print(f" O resultado é: {round((a+b),2)}")

def subtrair(a,b):
    print(f" O resultado é: {round((a-b),2)}")

def dividir(a,b):
    print(f" O resultado é: {round((a/b),2)}")

def multiplicar(a,b):
    print(f" O resultado é: {round((a*b),2)}")

def raiz(a,b):
    print(f" O resultado é: {round(b**(1/a))}")

while True:
    try:
        opcao = int(input("""
Qual operação deseja fazer? 
1-Somar
2-Substrair
3-Multiplicar
4-Dividir
5-Raiz                          
0-Sair
>>> """))
    except ValueError:
        print('Letras não são aceitáveis. Digite uma opção válida!')
        continue
    if opcao ==0:
        print("\nObrigado por usar nossa calculadora!")
        break


    if opcao not in (1,2,3,4,5):
        print(f"\n {opcao} não é está no menu. Digite uma opção válida!")
        continue


        

    if opcao in (1,2,3,4):
        v1 = int(input("Insira o primeiro valor:"))
        v2 = int(input("Insira o segundo valor:"))  
        while opcao == 4 and v2 ==0:
            print('Não é possível devidir por 0.')
        v2 = int(input("Insira o segundo valor:"))  
        if opcao == 1:
            somar(v1,v2)
        elif opcao ==2:
            subtrair(v1,v2)
        elif opcao ==3:
            multiplicar(v1,v2)
        elif opcao ==4:
            dividir(v1,v2)
    elif opcao == 5:
            while True:
                v1 = int(input("Insira o coeficiente da raiz(Ex:2,3,4...): "))
                if v1<0:
                    print("O coeficiente deve ser maior do que 0! ")
                    continue
                break
            while True:
                v2 = int(input("Insira o número que deseja descobrir a raiz: "))
                if v2<0:
                    print("O coeficiente deve ser maior do que 0! ")
                    continue
                break
            raiz(v1,v2)
    

print()



