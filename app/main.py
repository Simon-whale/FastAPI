import textwrap

from app.Router import health, ErrorHandling, Results, root

from fastapi import FastAPI, APIRouter

tags_metadata = [
    {
        "name": "Health",
        "description": "This is a simple health check"
    },
    {
        "name": "Results",
        "description": textwrap.dedent(
            """These endpoints are simply used to return a list of numbers, one endpoint is
               default set to 0 to 100 and hte other is set dynamically set by the caller""")
    },
    {
        "name": "Errors",
        "description": textwrap.dedent(
            """This section is to show how parts will return a https status code for something
               that will on purpose throw an exception
            """
        )
    }
]

app = FastAPI(
    title="Fast Api Learning",
    openapi_tags=tags_metadata,
    docs_url="/swagger",
    redoc_url="/docs"
)

route_v3 = APIRouter()

# Add each route to this router which we will then add into the
# main applications router so that we can create a structured layout
# visually and in code
route_v3.include_router(health.router, prefix="/health")
route_v3.include_router(root.router, prefix="")
route_v3.include_router(Results.router, prefix="/results")
route_v3.include_router(ErrorHandling.router, prefix="/errors")

app.include_router(route_v3)
