Funções Python>
IF>  se isso for verdade, faz isso
ELIF>senão, se isso outro for verdade, faz isso
ELSE >se nenhuma das anteriores, faz isso
INPUT()>Recebe informação do usuário

Para o programa e espera o usuário digitar algo. O que o usuário digitar vira uma variável que o programa usa.

Sem input → você muda o código para testar
Com input → o usuário controla o programa

WHILE >Mantém o programa rodando

Repete um bloco de código enquanto uma condição for verdadeira. while True significa rodar para sempre.

Sem while → programa roda uma vez e fecha
Com while → programa fica vivo esperando o próximo comando

BREAK>Sai do loop

Encerra o while quando uma condição específica acontece. No seu código foi quando o usuário digitou sair.

Sem break → programa nunca fecha
Com break → programa fecha quando você mandar

Resumo — Dia 3 e Dia 4
FUNÇÕES DO DIA 3
import

Carrega uma biblioteca externa para usar no seu código.

python
from google import genai

Sem isso o Python não sabe o que é genai.

genai.Client()

Cria a conexão com a API do Gemini. É como abrir uma linha telefônica com a IA.

python
cliente = genai.Client(api_key="sua_chave")

Sem isso você não consegue falar com a IA.

cliente.models.generate_content()

Envia uma mensagem para a IA e recebe a resposta.

python
resposta = cliente.models.generate_content(
    model="gemini-3.6-flash",
    contents="sua pergunta aqui"
)

É o equivalente a digitar uma mensagem no chat.

resposta.text

Pega só o texto da resposta da IA.

python
print(resposta.text)

A resposta completa tem muita informação técnica. O .text filtra só o que interessa.

FUNÇÕES DO DIA 4
SYSTEM_PROMPT

Variável que guarda as instruções do agente. Define quem ele é e o que ele sabe.

python
SYSTEM_PROMPT = """
Você é atendente da Barbearia LaVi.
Horário: segunda a sábado das 9h às 19h.
"""

Sem isso a IA inventa informações. Com isso ela responde só o que você definiu.

f"{SYSTEM_PROMPT}\n\nCliente perguntou: {pergunta}"

Junta o system prompt com a pergunta do cliente antes de enviar para a IA.

python
contents=f"{SYSTEM_PROMPT}\n\nCliente {nome} perguntou: {pergunta}"

O \n\n pula duas linhas para separar o contexto da pergunta.

CONCEITO MAIS IMPORTANTE DA SEMANA
System prompt → o que o agente SABE e como ele SE COMPORTA
Mensagem      → o que o cliente PERGUNTOU

Agente sem system prompt = atendente sem treinamento
Agente com system prompt = atendente bem instruído

Salva isso como resumo_dia3_dia4.txt na sua pasta de estudos.
