from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from auth import validar_api_key
from middleware import LoggingMiddleware
from responses import respuesta_exitosa, respuesta_error

# Inicializa
app = FastAPI()

# Configuramos la carpeta de templates
templates = Jinja2Templates(directory="templates")

# Agregamos el middleware de logging
app.add_middleware(LoggingMiddleware)

# Ruta principal: Devuelve HTML en "/"
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "mensaje": "¡Hola desde FastAPI!"})

# Ruta JSON en "/json"
@app.get("/json")
def api_root():
    return respuesta_exitosa("Hola, FastAPI en JSON!")

# Ruta protegida con API Key en "/items/{item_id}"
@app.get("/items/{item_id}")
def obtener_item(item_id: int, api_key: str = Depends(validar_api_key)):
    if item_id < 1:
        return respuesta_error("ID inválido", 400)
    return respuesta_exitosa(f"Item {item_id} encontrado.")