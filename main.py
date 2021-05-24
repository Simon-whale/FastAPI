import textwrap

import uvicorn
import Router

from fastapi import FastAPI

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
    }
]

app = FastAPI(
    title="Fast Api Learning",
    openapi_tags=tags_metadata,
    docs_url="/swagger",
    redoc_url="/docs"
)

app.include_router(Router.route_v3)

# Automatically start the server on port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
