from dotenv import load_dotenv
load_dotenv()

nome = input("qual é o seu nome? ")
contador = 0
while True:
    servico = input("Digite o serviço desejado (corte, barba, corte_barba, hidratacao, progressiva, escova, sair): ")
    if servico == "sair":
        print("Encerrando o atendimento.")
        if contador == 1:
            print(f"{nome}, você solicitou {contador} serviço.")
        else:
            print(f"{nome}, você solicitou {contador} serviços.")
        break
    elif servico == "corte":
        contador += 1
        print(f"{nome}, o preco do corte é R$35")
    elif servico == "barba":
        contador += 1
        print(f"{nome}, o preco da barba é R$25")
    elif servico == "corte_barba":
        contador += 1
        print(f"{nome}, o preco do corte e barba é R$55")
    elif servico == "hidratacao":
        contador += 1
        print(f"{nome}, o preco da hidratação é R$40")
    elif servico == "progressiva":
        contador += 1
        print(f"{nome}, o preco da progressiva é R$100")
    elif servico == "escova":
        contador += 1
        print(f"{nome}, o preco da escova é R$30")
    else:
        print("Servico nao encontrado")


