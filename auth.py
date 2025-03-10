from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

# 📌 Definir la API Key secreta
API_KEY = "secret123"
api_key_header = APIKeyHeader(name="X-API-Key")

# 📌 Función para validar la API Key
def validar_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida")
    return api_key
