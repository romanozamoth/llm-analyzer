from fastapi import FastAPI, Request, File, UploadFile
from pydantic import BaseModel
from app.llm_client import analisar_texto, extrair_texto_ocr
from tempfile import NamedTemporaryFile
from fastapi.responses import JSONResponse

app = FastAPI()

class TextoEntrada(BaseModel):
    texto: str
    pergunta: str

@app.post("/analisar")
async def analisar(input: TextoEntrada):
    resposta = analisar_texto(input.texto, input.pergunta)
    return {"resposta": resposta}

@app.post("/analisar-imagem")
async def analisar_imagem(file: UploadFile = File(...), pergunta: str = ""):
    try:
        # Salva a imagem temporariamente
        with NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(await file.read())
            caminho_img = tmp.name

        texto_img = extrair_texto_ocr(caminho_img)
        resposta = analisar_texto(texto_img, pergunta)

        return {
            "texto_extraido": texto_img.strip(),
            "resposta": resposta.strip()
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
