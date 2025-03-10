from fastapi.responses import JSONResponse

def respuesta_exitosa(mensaje: str):
    return JSONResponse(status_code=200, content={"mensaje": mensaje})

def respuesta_error(mensaje: str, status_code: int = 400):
    return JSONResponse(status_code=status_code, content={"error": mensaje})
