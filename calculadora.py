import os
import time
import sys



#Funções da operações
class Calculadora():
    @staticmethod
    def somar(a,b):
        return print(f" O resultado é: {round((a+b),2)}")
    @staticmethod
    def subtrair(a,b):
        return print(f" O resultado é: {round((a-b),2)}")
    @staticmethod
    def dividir(a,b):
        return print(f" O resultado é: {round((a/b),2)}")
    @staticmethod
    def multiplicar(a,b):
        return print(f" O resultado é: {round((a*b),2)}")
    @staticmethod
    def raiz(a,b):
        return print(f" O resultado é: {round(b**(1/a),2)}")
        
    @staticmethod  
    def validar_input(mensagem, valor_minimo):
        while True:
            try:
                numero = int(input(mensagem))
                if numero > 0:
                    return numero
           
                else:
                    print(f"O número digitado deve ser maior do que {valor_minimo}! ")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro!")

def efeito_digitacao(texto):
    """
    Simula o efeito de digitação em uma linha de texto.
    """
    for caractere in texto:
        sys.stdout.write(caractere)  # Imprime um caractere sem pular linha
        sys.stdout.flush()           # Força a impressão imediata
        time.sleep(0.05)  

def menu():
    while True:       
        try:
            os.system("cls")
            opcao = int(input("""
            Qual operação deseja fazer?\n                 
            1-Somar
            2-Substrair
            3-Multiplicar
            4-Dividir
            5-Raiz                          
            0-Sair\n
            >>>Digite aqui: """))

            if opcao not in (0,1,2,3,4,5):
                efeito_digitacao("\n ATENÇÃO!! Digite apenas um dos números do menu!")
                time.sleep(0.5)
                continue
            
            else:
                return opcao
                
        except ValueError:
            print('Letras ou caracteres não são aceitáveis. Digite uma opção válida!')
            os.system("cls")
            continue


def rodar_calculadora():
    while True:
        opcao = menu()
        if opcao ==0:
            efeito_digitacao("\nObrigado por usar nossa calculadora! ;)")
            return 0
        #Pedindo os valore que serão calculados 
        v1 = Calculadora.validar_input("Insira o primeiro valor:", 0)
        v2 = Calculadora.validar_input("Insira o segundo valor:", 0)  

        if opcao == 1:
            Calculadora.somar(v1,v2)
        elif opcao ==2:
            Calculadora.subtrair(v1,v2)
        elif opcao ==3:
            Calculadora.multiplicar(v1,v2)
        elif opcao ==4:
            while v2 ==0:
                print('Não é possível devidir por 0.')
                v2 = int(input("Insira o segundo valor novamente: "))  
            Calculadora.dividir(v1,v2)
        elif opcao == 5:
                while True:
                    v1 = int(input("Insira o coeficiente da raiz(Ex:2,3,4...):\n "))
                    if v1<=0:
                        print("O coeficiente deve ser maior do que 0!\n ")
                        continue
                    break
                while True:
                    v2 = int(input("Insira o número que deseja descobrir a raiz: \n"))
                    if v2<=0:
                        print("O número deve ser maior do que 0!\n ")
                        continue
                    break
                Calculadora.raiz(v1,v2)

        

if __name__ == "__main__":

 
    rodar_calculadora()

