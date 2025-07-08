import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi3"  # ou "mistral", se preferir

def analisar_texto(texto: str, pergunta: str) -> str:
    prompt = (
        f"A seguir está um texto. Sua tarefa é responder à pergunta no final com base no conteúdo do texto.\n\n"
        f"TEXTO:\n{texto}\n\n"
        f"PERGUNTA:\n{pergunta}\n"
    )

    response = requests.post(OLLAMA_URL, json={
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Erro ao consultar o modelo: {response.text}"
