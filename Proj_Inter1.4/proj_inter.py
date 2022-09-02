print (30 * '-')
print('\033[4;97;45m PROJETO INTERDISCIPLINAR 1.4 \033[m') 
print (30 * '-')
print ('        DEC CONVERT 1.4')
print (30 * '-')
print('Conversão da base Decimal para as bases Binária, octadecimal e Hexadecimal. \n') 


deci = "s"
while deci == "s" or deci == "S":   

    op =  input('Escolha uma opção: \n \033[0;41m[1] - Decimal para Binário \033[m  \n \033[0;31;47m[2] - Decimal para Octadecimal \033[m \n \033[0;30;44m[3] - Decimal para Hexadecimal \033[m \n \033[0;30;42m[4] - Sair/Sobre \033[m \n Digite aqui: ' )       #Menu com cores, o objetivo é alimentar variével "op", com intuito de entrar na estutura de decisão.

    if op == "1":          #Estrutura de decisão aninhada.

        decimal = int(input("Digite um valor em Decimal: ")) 
        def converter( dec, base, simbolos):                 #Parametros valor decimal, base, simbolos para Hexadecimal
            resul = []                                       #"Vetor" para amazenar caracteres
            while dec > 0:                                   #estrutura while para fazer processamento
                resul.insert(0, simbolos[dec % base])        #Processamento do vetor com insert, e resto da divisão
                dec //=  base                                #operação parte inteira do valor decimal pela base
            return ''.join(resul)                            #Retorna o resultado como string
    
        simbolos = '0123456789ABCDEF'                        
        print(35 * "-")
        print('O valor em Binário é: ',converter(decimal,2,simbolos))    #chamando a função,com parametros decimal, 2, simbolos
        print(35 * "-")

        a = input("Quer continuar ?\n[S] SIM [N] NÃO \nDigite: " )         #Pergunta para usuário se ele quer continuar com as operações
        if a == "s" or a == "S":                                         #Estrutura de decisão aninhada: if, elif e else
            deci = a
        elif a == "n" or a == "N":
            break
        else:
         print("             ----------------------------")
         print("                   Opção invalida!")
         print("             ----------------------------")
            
    
    
    elif op == "2":
        decimal = int(input("Digite um valor em Decimal: ")) #Entrada de dados (Número Decimal para octadecimal)
        def converter( dec, base, simbolos):
            resul = []
            while dec > 0:
                resul.insert(0, simbolos[dec % base])
                dec //=  base
            return ''.join(resul)
    
        simbolos = '0123456789ABCDEF'
        print(35 * "-")
        print('O valor em Octadecimal é: ',converter(decimal,8,simbolos))
        print(35 * "-")

        a = input("Quer continuar ?\n[S] SIM [N] NÃO \nDigite: " )
        if a == "s" or a == "S":
            deci = a
        elif a == "n" or a == "N":
            break
        else:
         print("             ----------------------------")
         print("                   Opção invalida!")
         print("             ----------------------------")
    
    
    elif op == "3":
        decimal = int(input("Digite um valor em Decimal: "))  #Entrada de dados (Número Decimal para Hexadecimal)
        def converter( dec, base, simbolos):
            resul = []
            while dec > 0:
                resul.insert(0, simbolos[dec % base])
                dec //=  base
            return ''.join(resul)
    
        simbolos = '0123456789ABCDEF'
        print(35 * "-")
        print('O valor em Hexadecimal é: ',converter(decimal,16,simbolos))
        print(35 * "-")

        a = input("Quer continuar? \n[S] SIM [N] NÃO \nDigite: " )
        if a == "s" or a == "S":
            deci = a
        elif a == "n" or a == "N":
            break
        else:
         print("             ----------------------------")
         print("                   Opção invalida!")
         print("             ----------------------------")
            

    elif op == "4":
        print()
        print( 20 * '-=-')
        print('                       DEC CONVERT 1.4       ')
        print(20 * '-=-')
        print(' Integrantes do Grupo: \n Bruno Rodrigues RGM: 25042686 \n Matheus Orzanqui RGM: 28775589 \n Kayky Candido RGM: 29239575 \n ')
        break
    
    else:
         print("             ----------------------------")
         print("                   Opção invalida!")
         print("             -----------------------------")
