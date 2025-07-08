![Work in Progress](https://img.shields.io/badge/status-in--progress-orange)

# llm-analyzer
Practical local LLM automation for analyzing texts – from course exercises to personal experiments.

# 📁 Estrutura do Projeto
```bash
llm-analisador/
├── app/
│   ├── main.py            # FastAPI app com endpoint de análise
│   └── llm_client.py      # Cliente para se comunicar com o modelo (Ollama)
├── Dockerfile             # Container com FastAPI
├── requirements.txt       # Dependências Python
└── README.md              # Instruções de uso
```

# 🔧 Instalar o Ollama localmente (apenas 1 vez)
Ollama roda os modelos com aceleração por GPU e cria uma API local automaticamente.

## ✅ Comando para instalar:

Linux/macOS:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Windows:
```
Baixe em: https://ollama.com/download
```

## ⚙️ Rodar o modelo (exemplo com phi3)
```bash
ollama run phi3
```
Ollama vai baixar o modelo e criar um servidor local na porta 11434.

___________

# 🧪 Testando localmente
1. Rode o Ollama com o modelo:
```bash
ollama run phi3
```
2. Rode a API (fora do Docker):
```bash
python -m uvicorn app.main:app --reload
```
3. Teste a API (exemplo via cURL ou Python):
```bash
curl -X POST http://localhost:8000/analisar \
  -H "Content-Type: application/json" \
  -d '{"texto": "A empresa XPTO apresentou proposta com o modelo Impressora LaserJet 1200 por R$ 1.500,00.", "pergunta": "Quais as propostas do texto contendo Fornecedor/Autor, marca/modelo e valor?"}'
```
# 🐳 Dockerizar (opcional, depois de testar)

Build:
```bash
docker build -t llm-analisador .
```
Run:
```bash
docker run -p 8000:8000 llm-analisador
```

_________________________