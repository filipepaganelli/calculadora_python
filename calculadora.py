import os
import time
import sys



#Funções da operações
class Calculadora():

    #Funções de operações matemáticas
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
    
    #Função de validação de input   
    @staticmethod  
    def validar_input(pergunta: str, valor_minimo: int):
        while True:
            
            try:
                
                valor = int(input(pergunta))
                if valor < valor_minimo:
                    print(f"Digite um valor maior que {valor_minimo}")
                    
                    continue
                else:
                    return valor
            except ValueError:
                print('Letras ou caracteres não são aceitáveis. Digite uma opção válida!')
                
                     

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
        if opcao == 0:
            efeito_digitacao("\nObrigado por usar nossa calculadora! ;)")
            return 0

        # Para soma, subtração e multiplicação, mínimo é 0
        if opcao in (1, 2, 3):
            v1 = Calculadora.validar_input("Insira o primeiro valor: ", 0)
            v2 = Calculadora.validar_input("Insira o segundo valor: ", 0)
            if opcao == 1:
                Calculadora.somar(v1, v2)
            elif opcao == 2:
                Calculadora.subtrair(v1, v2)
            elif opcao == 3:
                Calculadora.multiplicar(v1, v2)

        elif opcao == 4:
            v1 = Calculadora.validar_input("Insira o primeiro valor: ", 0)
            v2 = Calculadora.validar_input("Insira o segundo valor: ", 1)
            Calculadora.dividir(v1, v2)

        elif opcao == 5:
            v1 = Calculadora.validar_input("Insira o coeficiente da raiz: ", 1)
            v2 = Calculadora.validar_input("Insira o número que deseja descobrir a raiz: ", 1)
            Calculadora.raiz(v1, v2)

if __name__ == "__main__":

 
    rodar_calculadora()

