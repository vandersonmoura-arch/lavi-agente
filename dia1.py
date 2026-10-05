from dotenv import load_dotenv
load_dotenv()

def apresentar_agente(sistema_agendamento):
    return f"Agente da {sistema_agendamento} online e pronto"

def calcular_preco(servico):
    precos = {
        "corte": 35,
        "barba": 25,
        "corte_barba": 55
    
    }
    return precos[servico]

def resumo_atendimento(cliente, servico):
    preco = calcular_preco(servico)
    return f"Cliente: {cliente} | Serviço: {servico} | Total: R${preco}"

def listar_servicos():
    servicos = {
        "corte": 35,
        "barba": 25,
        "corte_barba": 55
    }
    print("Servicos disponiveis:")
    for servico, preco in servicos.items():
        print(f" {servico}: R${preco}")
print(apresentar_agente("LaVi"))
print(f"Corte custa R${calcular_preco('corte')}")
print(f"Barba custa R${calcular_preco('barba')}")
print(f"Corte e barba custa R${calcular_preco('corte_barba')}")
print(resumo_atendimento("João", "corte"))
print(resumo_atendimento("Pedro", "corte_barba"))
listar_servicos()