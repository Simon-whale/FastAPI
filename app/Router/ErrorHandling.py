from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.Models.Message import Message
from app.Models.Item import Item


router = APIRouter()


@router.get('/blowsup/{item_no}', tags=["Errors"])
def she_gonna_blow(item_no: int):
    if item_no >= 100:
        # Here on purpose we raise an exception if the ID is equal
        # or greater too 100
        raise HTTPException(status_code=404, detail="Id is not found")

    return {"It didn't break it": id}


@router.get("/break/{item_id}", response_model=Item, responses={404: {"model": Message}}, tags=["Errors"])
def it_go_boom(item_no: int):
    """
    This endpoint is showing that you can set a format for the response message and an error message
    """
    if item_no == 100:
        return {"id": "foo", "value": "It didn't go BOOM"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
