from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

# Include_in_schema attribute when set to false will ensure that endpoint is not included in the documentation
@router.get('/', include_in_schema=False)
async def get_root():
    return RedirectResponse("/docs")
