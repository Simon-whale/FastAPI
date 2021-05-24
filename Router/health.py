from fastapi import APIRouter

router = APIRouter()


@router.get('/health/', tags=["Health"])
def is_alive():
    return {"Alive": True}
