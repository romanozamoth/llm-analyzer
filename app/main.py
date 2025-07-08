from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.llm_client import analisar_texto

app = FastAPI()

class TextoEntrada(BaseModel):
    texto: str
    pergunta: str

@app.post("/analisar")
async def analisar(input: TextoEntrada):
    resposta = analisar_texto(input.texto, input.pergunta)
    return {"resposta": resposta}
