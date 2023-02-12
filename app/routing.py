## -- Importing External Modules -- ##
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from timeit import default_timer as timer

## -- Importing Internal Modules -- ##
from app.resources import pokemon
from app.server import app

app.include_router(pokemon.router)

## Middlewares

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    # Before request
    start_time = timer()

    response = await call_next(request)
    
    # After request
    process_time = timer() - start_time

    response.headers["X-Process-Time"] = str(process_time)
    return response

## Handlers
@app.exception_handler(Exception)
async def universal_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code = 500,
        content = {
            "status": "error",
            "message": "Internal Server Error",
        },
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):

    return JSONResponse(
        status_code = exc.status_code,
        content = {
            "status": "error",
            "message": str(exc.detail).capitalize(),
        },
    )