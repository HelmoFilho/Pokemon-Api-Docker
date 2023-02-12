## -- Importing External Modules -- ##
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from aiohttp import ClientSession

## -- Importing Internal Modules -- ##
from app.interfaces.pokemon_interface import (
    Pokemon,
    ErrorResponse,
    SuccessResponse,
)

router = APIRouter(
    prefix = "/pokemon"
)

responses = {
    200: {"model": SuccessResponse},
    400: {"model": ErrorResponse},
}

@router.post("", responses = responses, summary = "Pokemon Info")
async def pokemon_info(request: Pokemon) -> dict:
    """
    Fetch the data of a pokemon with its name or national dex nº

    - Remenbering that "id" and "name" should not be provided at the same time
    """

    domain = "https://pokeapi.co"
    
    if request.name:
        url = f"/api/v1/pokemon/{request.name}"

    else:
        url = f"/api/v1/pokemon/{request.id}"
    
    async with ClientSession(domain) as session:
        async with session.post(url) as response:

            if response.status == 404:
                raise HTTPException(
                    status_code = 404,
                    detail = "Pokemon not found."
                )

            data = await response.json()

    rtn_data = {
        "status": "success",
        "message": "Pokemon info was found.",
        "data": {
            "name": data.get("name").capitalize(),
            "info": data,
        },
    }

    return JSONResponse(
        status_code = 200,
        content = jsonable_encoder(rtn_data),
    )