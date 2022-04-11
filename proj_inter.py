
#Menu/ Entrada de dados
print (30 * '-')
print('\033[30;41mPROJETO INTERDISCIPLINAR 1.0 \033[30;41m') 
print (30 * '-')

print ('DEC CONVERT 1.0')
print (30 * '-')
print('Conversão da base decimal, para a base binário, octadecimal e hexadecimal. \n')  #"Dec Convert 1.0" Nome do programa"

op =  input('Escolha uma opção: \n [1] - Decimal para Binário \n [2] - Decimal para Octadecimal \n [3] - Decimal para Hexadecimal \n [4] - Sobre \n Digite aqui: ' )



#Processamento

if op != "1" and op != "2" and op != "3" and op != "4":
    print ("Opção invalida! ")
else:
    dec = int(input("Digite um valor em Decimal: ")) #Entrada de dados (Número Decimal)
    if op == "1":
       resul = dec+5                            #processamento para teste
       print("A conversão de decimal para binário é: ", resul)
    elif op == "2":
         resul = dec+3                          #processamento para teste
         print("A conversão de decimal para octadecimal é: ", resul)
    elif op == "3":
         resul = dec+6                          #processamento para teste
         print("A conversão de decimal para hexadecimal é: ", resul)




