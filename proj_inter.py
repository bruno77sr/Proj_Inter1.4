#Menu/ Entrada de dados

print("PROJETO INTERDISCIPLINAR. \n         Dec Convert \nConversão da base decimal para as bases binário, hexadecimal e octadecimal \n")  #"Dec Convert" é para ser o nome do programa"

op =  input("Escolha uma opção: \n B - Decimal para Binário; \n H - Decimal para Hexadecimal \n O - Decimal para Octadecimal \n Digite aqui: " )

#Processamento

if op != "B" and op != "b" and "H" and op != "h" and op != "O" and op != "o":
    print ("Opção invalida! ")
else:
    dec = int(input("Digite um valor em Decimal: ")) #Entrada de dados (Número Decimal)
    if op == "B" or op == "b":
       resul = dec+5                            #processamento para teste
       print("O resultado é: ", resul)
    elif op == "H" or op == "h":
         resul = dec+3                          #processamento para teste
         print("O resultado é: ", resul)
    elif op == "O" or op == "o":
         resul = dec+6                          #processamento para teste
         print("O resultado é: ", resul)




