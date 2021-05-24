from fastapi import APIRouter
from fastapi.routing import  APIRoute

from . import health
from . import root
from . import Results

route_v3 = APIRouter()

# Add each route to this router which we will then add into the
# main applications router so that we can create a structured layout
# visually and in code
route_v3.include_router(health.router, prefix="/health")
route_v3.include_router(root.router, prefix="")
route_v3.include_router(Results.router, prefix="/results")