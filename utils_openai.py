import openai

# API OPENAI ================================================
def retorna_resposta_modelo(mensagens,
                            openai_key,
                            modelo='gpt-4',
                            temperatura=0,
                            stream=False):
    # Cria uma instância do cliente OpenAI com a chave de API fornecida
    client = openai.OpenAI(api_key=openai_key)
    
    # Faz a chamada para criar a conclusão de chat
    response = client.chat.completions.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
        stream=stream
    )
    
    return response